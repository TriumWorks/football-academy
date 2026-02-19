# Milos Academy - Claude Code Guide

## Project Overview

A Django web application for managing a sports academy. It handles player management, play scheduling, attendance tracking, and caretaker (parent/guardian) management.

## Tech Stack

- **Framework**: Django 5.2
- **Database**: SQLite (development)
- **Auth**: Custom user model (`account.User`) using email as username
- **Static files**: Served from `/static/`, collected to `staticfiles/`

## Project Structure

```
academy-web/
├── academy/          # Django project config (settings, urls, wsgi, asgi)
├── account/          # Main app (models, views, urls, forms, templates)
├── common/           # Shared utilities (base models, middleware, push_id)
├── static/           # Static assets (CSS, JS, images)
├── templates/        # Top-level templates
└── manage.py
```

## Apps

### `account`
The primary app containing all business logic:
- **Models**: `User`, `Player`, `UserPlayer`, `PlaySchedule`, `PlayerAttendance`
- **Views**: Registration, login, logout, player CRUD, schedule CRUD, attendance, caretaker management
- **Auth**: Custom `AbstractBaseUser` with email-based login

### `common`
Shared base classes:
- `BaseModel` — uses `push_id` for string primary keys (not integer auto-increment)
- `AuditableModel` — extends `BaseModel` with `created_at`, `updated_at`, `created_by`, `updated_by`, soft-delete fields
- `get_current_user()` middleware — injects the current request user into model `save()`

## Key Conventions

- **Primary keys** are string-based (`push_id`), not integers. Never assume integer PKs.
- **All models** should inherit from `AuditableModel` (not Django's base `Model` directly).
- **Soft deletes** use the `deleted` boolean field. Filter with `deleted=False` when querying active records.
- **Auth user** is `account.User` (set via `AUTH_USER_MODEL`). Always use `get_user_model()` when referencing it.
- **Templates** live in `account/templates/` (app-level) and `templates/` (project-level).

## Common Commands

```bash
# Run dev server
python manage.py runserver

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

## URL Structure

| Pattern | Name | Description |
|---|---|---|
| `/` | `account:home` | Dashboard |
| `/login/` | `account:login` | Login |
| `/register/` | `account:register` | Registration |
| `/players/` | `account:players` | Player list |
| `/players/create` | `account:players-create` | Create player |
| `/players/<pk>` | `account:player-details` | Player detail |
| `/play-schedule` | `account:scheduling` | Schedule list |
| `/play-schedule/create` | `account:scheduling-create` | Create schedule |
| `/play-schedule/<pk>` | `account:scheduling-details` | Schedule detail |
| `/attendance/<pk>/confirm` | `account:confirm-attendance` | Confirm attendance |
| `/care-takers` | `account:care-takers` | Caretaker list |
| `/care-takers/<pk>` | `account:care-takers-details` | Caretaker detail |
| `/care-takers/assign/` | `account:care-takers-assign-player` | Assign player to caretaker |
