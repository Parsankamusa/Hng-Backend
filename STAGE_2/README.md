## HNG TASK 2
# REST API for Managing Persons

This is a simple REST API bult using Flask framework for managing persons. It allows to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [UML Diagram](#database-modeling-)
- [Documentation](#documentation-)
- [Testing](#testing-)

## Prerequisites
Before getting started, ensure you have the following installed on your system:
- The latest python version
- An editor such as Vs code or Pycharm

## Installation
Follow these steps to set up and run the project:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Parsankamusa/Hng-Backend.git
   ```
   
2. Navigate to the project directory 
   ```bash
   cd Hng-backend
   ```
3. Run the following command to set up virtual environment:
   ```bash
   python -m venv env
   ```
   ```bash
   env/Scripts/activate
   ```
4. Run the following command to install dependencies:
   ```bash
   pip install flask_sqlalchemy
   ```
   ```bash
   pip install request
   ```
4. Create a app.py  file in the project root and configure your SQLAIchemy:
   ```bash
   from flask import Flask, request, jsonify
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
   db = SQLAlchemy(app)
   ```

5. Run the following command to start the server:
   ```bash
   python app.py
   ```

Your Flask server should now be running at http://localhost:5000.
