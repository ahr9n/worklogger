# Worklogger

A website where I could sign in and log my hours for the day

## Description

After signing in, there is a form where I could input a new time log, and below it is a list of all my logs for the day.

* Administrators can;
  * Add/edit/remove projects through Django admin.
  * Add/edit/delete users through Django admin.
  * Modify hours already logged through Django admin.
  * Delete projects should not delete hours logged for that project. 
    * The project assigned for those hours can be `NULL`.
  * See total logged hours for any project.

* Users can:
  * Log hours for any selected day.
  * See logs for the day.
  * See total logged hours for the week and month based on selected day.
  * Select a day and load logs for that day.

* More Features:
  * Use a calendar layout to select the day.
  * Late logs with red text (a log for the selected day is late if it was created after the given day).

## Getting Started

Requires Python3 and [Poetry](https://python-poetry.org/docs/#installation) installation.

After cloning the repository, refer to the project folder and:
 * Create a `.env` file based on the `.env.example` file and add the needed parameters.
 * Install the needed packeges: `poetry install`
 * Activate a virtual environment: `poetry shell`
 * Create new migrations based on any changes in models: `python3 manage.py makemigrations`
 * Apply the migrations to the database: `python3 manage.py migrate`
 * Create a superuser to be able to use Django Admin interface: `python3 manage.py createsuperuser`
 * Run the app locally: `python3 manage.py runserver`
 
_Implemented with poetry@1.2.2_
