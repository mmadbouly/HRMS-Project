# HRMS-Project

Human Resources system for individuals and companies to manage their own human resources. The system should be able to manage the following points:          
* Time tracking for employees and projects
* Depending on the clearance degree the system functionality will be available
  * Logged in as normal team member is different when logged in as team leader

### Prerequisites
* Install Django here we are using django==2.2 (April 2019)
  * for a better separation we recommend using a virtual environment *see down (Getting started step 2)*
  * if you have a ```virtenv``` then activate it before installing django
  ```
  pip install django==2.2
  ```
  
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
1. clone the repo
2. create a project folder
    2. create virtual env with python3 ***(recommended)***
    2. activate the venv
3. go to src/ folder
4. run with python 3:
    ```bash
    python manage.py runserver
    ```
* Follow the terminal message and go to your local host on any browser--> if you see django's message that it's working then you are good to go
5. because the database is not pushed on the repo for safety purposes you need to make your own local database
    go ahead and run:
    ```bash
    python manage.py makemigrations
    ```
    followed by:
    ```bash
    python manage.py migrate
    ```
    now create a superuser with:
    ```bash
    python manage.py createsuperuser
    ```
    now you can type in your browser 
    ```
    http://127.0.0.1:8000/admin/
    ```
    and check out the admin built in app
6. Now if you know how django works you can start developing the site by adding to ```views.py``` or ```models.py``` 
  6. if not then check any django tutorial to get a good understanding how it works and how it is built
