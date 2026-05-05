---
name: project_repo_paths
description: Пути к git-репозиториям и email автора для генерации актов
type: project
---

Репозитории `salary` и `internal-client` находятся внутри `salary-back-front/`:
- `salary-back-front/salary` — основной репозиторий зарплатного сервиса
- `salary-back-front/internal-client` — внутренний клиент

В settings.py они прописаны именно так (относительно `W:\Projects`).

Email Камиля в git-коммитах — `jestenok1@gmail.com` (не `jestenok@gmail.com`).
В `PERSONS` и при вызове `save_tasks` нужно использовать `jestenok1@gmail.com`.

**Why:** репозитории переехали в монорепо `salary-back-front`, старой папки `salary` и `internal-client` на верхнем уровне больше нет. Email в коммитах отличается от того что был в старых настройках.
**How to apply:** при обновлении `settings.py` (ORG_DIR_SERVICE и PERSONS) использовать эти пути и email.
