## HNG TASK 2
# REST API for Managing Persons

This is a simple REST API bult using Flask framework for managing persons. It allows to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [UML-DIAGRAM](UML-DIAGRAM)
- [Documentation](#documentation)
- [Testing](#testing)
- [Deployment](#Deployment)

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
6. Creating a database model:
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

 ## Documentation
* The documentation include test  using postman or curl to verify the API's functionality.
    https://www.baeldung.com/curl-rest
  here is a link  for post documentation [postman](https://documenter.getpostman.com/view/24185831/2s9YC2zZAG)
  
## UML-DIAGRAM 
 * link to the UML diagram :https://app.creately.com/d/WGjpwxpemqJ/edit
* An Image to explain CRUD operation in an api
  ![UML Diagram](<hngx uml diagram.png>)
   
## Testing 
  * CURL TESTING
 * Run the following commands to query your api:
     1. POST
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "John Odoyo"}' http://127.0.0.1:5000/api
   Musa@DESKTOP-RPBI479 MINGW64 ~/Desktop/hngx
   $ curl -X POST -H "Content-Type: application/json" -d '{"name": "John Odoyo"}' http://127.0.0.1:5000/api
   {
   "message": "Person created successfully"
   }
   ```
     2. GET
   ```bash
   curl http://localhost:5000/api/<person_name>
   Musa@DESKTOP-RPBI479 MINGW64 ~/Desktop/hngx
   $   curl http://localhost:5000/api/John%20Odoyo
   {
   "id": 7,
   "name": "John Odoyo"
   }
   ```
     3. DELETE
   ```bash
    curl -X DELETE http://localhost:5000/api/<person_name>
   Musa@DESKTOP-RPBI479 MINGW64 ~/Desktop/hngx
   $   curl -X DELETE http://localhost:5000/api/John%20Odoyo
   {
   "message": "Person deleted successfully"
   }

   ```
## Deployment
https://parsanka.pythonanywhere.com/api/Musa%20Parsanka

  
