from flask import render_template
from models import courses

def index():
    return render_template('index.html', courses=courses)

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