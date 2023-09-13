from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # SQLite for simplicity
db = SQLAlchemy(app)
'''
creating the database model
'''
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
with app.app_context():
    db.create_all()
'''
creating a route to add a new person
'''
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

'''
creating another route that will perform the methods=['GET', 'PUT', 'DELETE'])
'''
@app.route('/api/<string:name>', methods=['GET', 'PUT', 'DELETE'])
def manage_person(name):
    person = Person.query.filter_by(name=name).first()

    if request.method == 'GET':
        if person:
            return jsonify({'id': person.id, 'name': person.name})
        else:
            return jsonify({'message': 'Person not found'}), 404

    if request.method == 'PUT':
        data = request.get_json()
        if 'name' not in data:
            return jsonify({'message': 'Name is required'}), 400
        person.name = data['name']
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'})

    if request.method == 'DELETE':
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': 'Person deleted successfully'})
        else:
            return jsonify({'message': 'Person not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

