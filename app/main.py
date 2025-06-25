import calendar
import importlib
from datetime import datetime

import pandas as pd

from settings import PERSONS
from commits import save_tasks
from docs import create_documents

YEAR = 2025
MONTH = 5


def main():
    start = datetime(YEAR, MONTH, 1)
    end = datetime(
        YEAR,
        MONTH,
        calendar.monthrange(YEAR, MONTH)[1],
        hour=23,
        minute=59,
        second=59
    )

    for person in PERSONS:
        name = person['name']
        email = person['email']

        file_name_dones = f'{name}/dones/{start.strftime("t_%m_%Y")}.csv'
        save_tasks(start, end, file_name_dones, name, email)

        file_name_tasks = file_name_dones.replace('dones', 'tasks')
        save_tasks(start, end, file_name_tasks, name, email)

        dones = pd.read_csv(file_name_dones)
        tasks = pd.read_csv(file_name_tasks)
        for org in tasks['Организация'].unique():
            tasks_org = tasks[tasks['Организация'] == org]
            dones_org = dones[dones['Организация'] == org]

            tasks_dict = tasks_org.groupby('Сервис')[['Задача', 'Время']].apply(
                lambda df: list(zip(df['Задача'], df['Время']))
            ).to_dict()
            dones_dict = dones_org.groupby('Сервис')[['Задача', 'Время']].apply(
                lambda df: list(zip(df['Задача'], df['Время']))
            ).to_dict()

            create_documents(org, tasks_dict, dones_dict, MONTH, name)


if __name__ == "__main__":
    main()
