from flask import Blueprint, jsonify, request
from .models import User, Course
from . import db

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'})

@main.route('/courses', methods=['GET'])
def courses():
    courses = Course.query.all()
    course_data = [{'title': course.title, 'description': course.description} for course in courses]
    return jsonify(course_data)

#TODO - Login Route: Create a route to handle the login logic and user session management.

