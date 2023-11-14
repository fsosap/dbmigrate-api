# dbmigrate-api

This repository allocates the development of a short project to make available an API (with Flask micro framework) for a dummy db migration and further SQL analysis.

API Design and data integration is modeled as follows:

![API requests](modeling/API%20request%20design.jpg)

To install this project please do as follows:

## previous requierements

make sure you have already installed python and its version is the same or higher than mine:

```text
Python 3.9.6
```

and version control tool

```text
git version 2.39.2
```

## ⚙️ INSTALLATION STEPS

1. Copy the current repository into your system with

    ```bash
    git clone https://github.com/fsosap/dbmigrate-api.git
    ```

2. Make sure you are on the right folder

    ```bash
    # to realize in which folder you're at
    pwd 
    # to move to the main hierarchy of the project
    cd dbmigrate-api/
    ```

3. Create a virtual environment to run the project and avoid downloads on your global python environment

    ```bash
    python -m venv <venv_name>
    ```

4. Activate your virtual environment so you can start downloading packages

    ```bash
    # for UNIX based systems
    source <venv_name>/bin/activate

    # for windows users
    C:\> <venv_name>\Scripts\activate.bat
    ```

5. Download the dependencies from 'requirements.txt' file with the following command

    ```bash
    pip install -r requirements.txt
    ```

6. Make the service available by running the trigger for flask

    ```bash
    flask run
    ```

Now you can navigate from the browser to the route <http://127.0.0.1:5000>
and interact with the different routes.
