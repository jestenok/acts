from datetime import datetime
import importlib

from commits import save_tasks
from docs import create_documents


def main():
    MONTH = 12

    start = datetime(2023, MONTH, 1)
    end = datetime(2023, MONTH, 30).replace(hour=23, minute=59, second=59)
    save_tasks(start, end)

    tasks_module = importlib.import_module(f'tasks.t_{MONTH}_2023')
    for org, tasks in tasks_module.done.items():
        create_documents(org, tasks, tasks_module.todo[org], MONTH)


if __name__ == "__main__":
    main()