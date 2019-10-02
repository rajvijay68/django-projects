## Errors encountered

1) Table user does not exist
    Sol - `python manage.py migrate`
    You need to create the user tables before creating a superuser

2) Permission denied while running `python manage.py runserver`
    Sol - Ensure that you have activated the virtual environment