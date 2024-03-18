import calendar
import importlib
from datetime import datetime

from commits import save_tasks
from docs import create_documents

YEAR = 2024
MONTH = 1


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
    save_tasks(start, end)

    tasks_module = importlib.import_module(f'tasks.t_{MONTH}_2023')
    for org, tasks in tasks_module.done.items():
        create_documents(org, tasks, tasks_module.todo[org], MONTH)


if __name__ == "__main__":
    main()