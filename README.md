# Exos code task
This repo was created for hosting the code task for the [upwork jobpost](https://www.upwork.com/jobs/~01cf49bc32e44284be)

## Features:
- [x] Set up a basic django 1.9 installation using a sqlite database in the same folder as the
source
- [x] Add two fields to the User model using a migration:
  - [x] birthday field of type date
  - [x] random number field of type integer that is assigned a value from 1-100 on
creation
- [x] Create views for listing all users, viewing, adding, editing and deleting a single user
- [x] Create two template tags:
  - [x] A tag that will display "allowed" if the user is > 13 years old otherwise display
"blocked"
  - [x] A tag that will display the BizzFuzz result of the random number that was
generated for the user. The BizzFuzz specification is that for multiples of three
print "Bizz" instead of the number and for the multiples of five print "Fuzz". For
numbers which are multiples of both three and five print "BizzFuzz"
  - [x] Add a column to the list view after the birthday column that uses the
allowed/blocked tag
  - [x] Add a column to the list view after the random number column that uses the
BizzFuzz tag
- [x] Unit test what you feel is appropriate to test.
- [x] Time permitting, create a download link on the list view that would allow the list to be exported
to excel.

## Screenshots

### List users
![List users](https://i.imgur.com/mblDEYF.png)

### User detail
![User detail](http://i.imgur.com/LKtjzQm.png)

### Edit user
![Edit user](http://i.imgur.com/Ymi4pbq.png)

### Delete user
![Delete user](http://i.imgur.com/FLFBkvP.png)

### Create user
![Create user](http://i.imgur.com/CE4vR9M.png)

### List users csv file
![List user csv](https://i.imgur.com/hhTUfZY.png)

## System Requirements
* Python 3.6+
* sqlite 3.13
* pip 9.0.1

## Dependencies
See [requirements.txt](https://github.com/juliankmazo/exos_code_task/blob/master/requirements.txt) for more information.

## Build Instructions
### Application
For Linux and OSX users, run these commands:

1. First clone the project locally and then go into the directory
  ```shell
  $ git clone https://github.com/juliankmazo/exos_code_task.git
  $ cd exos_code_task
  ```

2. Setup our virtual environment
  ```shell
  $ python3 -m venv env
  ```

3. Now lets activate virtual environment
  ```shell
  $ source env/bin/activate
  ```

5. Now lets install the libraries this project depends on.
  ```shell
  $ pip install -r requirements.txt
  ```

### Application + Database
Run the following commands to make the database migrations
  ```shell
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

## Usage
To run the web-app, you’ll need to run the server instance and access the page from your browser.

Start up the web-server:
  ```shell
  $ cd exos_code_task
  $ python manage.py runserver
  ```

In your web-browser, load up the following url
  ```
  http://127.0.0.1:8000/
  ```

## Tests
To run the tests, you need to run the following command.

Start up the web-server:
  ```shell
  $ cd exos_code_task
  $ python manage.py test
  ```
You should get something like:
![Tests](https://i.imgur.com/U9ruupt.png)
