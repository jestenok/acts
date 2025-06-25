import os

import numpy as np
import pandas as pd
from git import Repo

from settings import BLACK_WORDS, ORG_DIR_SERVICE


def _get_tasks_df(start, end, emp, author=None) -> pd.DataFrame:
    path = os.path.dirname(os.path.dirname(os.getcwd()))

    res = []
    for org, dir_service in ORG_DIR_SERVICE[emp].items():
        for service_dir, service in dir_service:
            directory = os.path.join(path, service_dir)
            if directory:
                repo = Repo(directory)
                if service_dir == 'salary':
                    branch = repo.heads.main
                else:
                    branch = repo.active_branch
                commits_last_month = list(repo.iter_commits(branch, since=start, until=end, author=author))
                for c in commits_last_month:
                    msg = c.message
                    msg = msg.replace('\n', ' ').replace('/', '')

                    if msg.split(' ')[0].lower() in BLACK_WORDS:
                        continue

                    if msg.split('.')[0].lower() in BLACK_WORDS:
                        continue

                    if msg.split(':')[0].lower() in BLACK_WORDS:
                        continue

                    res.append((org, service, msg))

    df = pd.DataFrame(res, columns=['Организация', 'Сервис', 'Задача'])
    df = df.drop_duplicates()

    df['Время'] = 1
    amount = 80 - df.shape[0]

    if amount > 0 and not df.empty:
        distribution = np.random.multinomial(amount, [1 / len(df)] * len(df))
        df['Время'] += distribution

    return df


def save_tasks(start, end, file_name, emp, author=None):
    if os.path.exists(file_name):
        print(f'File {file_name} already exists')
        return
    df = _get_tasks_df(start, end, emp, author=author)
    df.to_csv(file_name, index=False)

