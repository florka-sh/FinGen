# FinGen

*Financial Genius*

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/sYysBPd6)


## Table of contents

- [Description](#description)
- [Installation](#installation-and-setup)
    - [Prerequisites](#prerequisites)
    - [Setup instructions](#setup-instructions)
        + [API Setup](#api-setup)
        + [Frontend setup](#frontend-setup)


## Description

Fullstack project build on Django/Django REST Framework along with PostgreSQL on backend side and with ReactJS(Typescript) for frontend side.

## Installation and setup

If you want to install project in your local environment you have to follow these steps:

### Prerequisites

Setup process assume that you have installed following on your machine:

- Python3 (any version you like above Python3.9)
- PostgreSQL database installed and running
- Latest version of Node.js and Vite

### Setup instructions

#### API Setup

1. Create Postgres user and database called `moneyflow`. Alter your user with command:
    ```
    ALTER ROLE username WITH ENCRYPTED PASSWORD 'your-password';
    ```
2. Grant permissions on that database to newly created user.
3. Open the Terminal app you like or have and git clone the repository. After that cd into repository folder and then into backend.
4. Create python virtual environment with command:
    ```bash
    python3 -m venv venv 
    ``` 
5. Use your new venv with command:
    ```bash
    source venv/bin/activate
    ``` 
6. Install Python dependencies with command:
    ```bash
    pip3 install -r requirements.txt
    ``` 
7. Create .env file with nano or any text-editor of your choise. \
    .env file structure:
    ```ini
    DB_USER=<your_database_user>
    DB_PASSWORD=<password_for_your_database_user>
    ```
8. Migrate database with command:
    ```bash
    python3 manage.py migrate
    ```
9. Run development server with following command and enjoy the API!
    ```bash
    python3 manage.py runserver
    ``` 

#### Frontend setup

To setup your frontend development server we will use `npm`. Follow next steps to configure your ReactJS environment:

1. Navigate into repository folder and then into frontend folder in new terminal instance.
2. Install dependencies with following command:
    ```bash
    npm install
    ```
3. Next you are good to go, so go ahead and run development server with command:
    ```bash
    npm run dev
    ```
