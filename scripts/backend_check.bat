(pipenv run isort -rc ./backend && ^
pipenv run yapf -dr ./backend && ^
pipenv run pylint --errors-only ./backend && ^
pipenv run flake8 ./backend && ^
goto :EOF) || goto :error


:error
exit /b %errorlevel%
