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
5. Create a app.py  file in the project root and configure your SQLAIchemy:
   ```bash
   from flask import Flask, request, jsonify
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
   db = SQLAlchemy(app)
   ```
   ```
6. Create a app.py  file in the project root and configure your SQLAIchemy:
   ```bash
  class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
with app.app_context():
    db.create_all()
   ```
   ```
7. creating a route to add a new person:
   ```bash
   @app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'Name is required'}), 400

    name = data['name']
    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

   ```

5. Run the following command to start the server:
   ```bash
   python app.py
   ```

Your Flask server should now be running at http://localhost:5000.
