from flask import render_template, jsonify
from models import courses

# View for the index page that displays all courses
def index():
    return render_template('index.html', courses=courses)

# View for a specific course page
def course(course_id):
    # course_id is passed as a string from the URL, convert to int for indexing
    try:
        idx = int(course_id) - 1
        if 0 <= idx < len(courses):
            course_obj = courses[idx]
        else:
            course_obj = None
    except ValueError:
        course_obj = None
        
    return render_template('course.html', course=course_obj)

# API view to return course details as JSON
def get_course_api(course_id):
    # Convert course_id to index (1-based to 0-based)
    idx = course_id - 1
    if 0 <= idx < len(courses):
        course_obj = courses[idx]
        # Return course data as a JSON dictionary
        return jsonify({
            'title': course_obj.title,
            'description': course_obj.description,
            'instructor': course_obj.instructor,
            'duration': course_obj.duration
        })
    # If not found, return 404 error as JSON
    return jsonify({'error': 'Course not found'}), 404