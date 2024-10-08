import os

import pandas as pd
from git import Repo

from settings import BLACK_WORDS, ORG_DIR_SERVICE


def _get_tasks_df(start, end) -> pd.DataFrame:
    path = os.path.dirname(os.getcwd())

    res = []
    for org, dir_service in ORG_DIR_SERVICE.items():
        for service_dir, service in dir_service:
            directory = os.path.join(path, service_dir)
            if directory:
                repo = Repo(directory)
                commits_last_month = list(repo.iter_commits(since=start, until=end))
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
    return df


def save_tasks(start, end):
    file_name = f'app/tasks/{start.strftime("t_%m_%Y")}.csv'
    if os.path.exists(file_name):
        print(f'File {file_name} already exists')
        return
    df = _get_tasks_df(start, end)
    df.to_csv(file_name, index=False)