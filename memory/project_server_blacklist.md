---
name: project_server_blacklist
description: Репозиторий server содержит только registry-коммиты — они все фильтруются BLACK_WORDS
type: project
---

В репозитории `server` все коммиты Камиля за 2026 имеют формат `registry.gof.dental/root/salary:1.1.XXXX-main`.
Они отфильтровываются по правилу `msg.split('.')[0].lower() in BLACK_WORDS` (слово `registry` есть в BLACK_WORDS).

**Why:** server-репо используется для CI/CD тегов, а не для фича-коммитов.
**How to apply:** не ожидать задач из server-репо при генерации актов. Если нужно добавить server-задачи — их надо вносить вручную в tasks CSV.
