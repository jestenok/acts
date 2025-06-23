import calendar
import importlib
from datetime import datetime

import pandas as pd

from commits import save_tasks
from docs import create_documents

YEAR = 2025
MONTH = 3


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
    file_name_dones = f'app/dones/{start.strftime("t_%m_%Y")}.csv'
    save_tasks(start, end, file_name_dones)

    dones = pd.read_csv(file_name_dones)
    tasks = pd.read_csv(file_name_dones.replace('dones', 'tasks'))
    for org in tasks['Организация'].unique():
        tasks_org = tasks[tasks['Организация'] == org]
        dones_org = dones[dones['Организация'] == org]

        tasks_dict = tasks_org.groupby('Сервис')['Задача'].apply(list).to_dict()
        dones_dict = dones_org.groupby('Сервис')['Задача'].apply(list).to_dict()

        create_documents(org, tasks_dict, dones_dict, MONTH)


if __name__ == "__main__":
    main()