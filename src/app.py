from flask import Flask, render_template
from views import index, course, get_course_api, contact

app = Flask(__name__)

# Register URL rules
app.add_url_rule('/', endpoint='index', view_func=index)
app.add_url_rule('/course/<course_id>', endpoint='course', view_func=course)
app.add_url_rule('/contact', endpoint='contact', view_func=contact)
app.add_url_rule('/api/course/<int:course_id>', endpoint='get_course_api', view_func=get_course_api)

if __name__ == '__main__':
    # Run the application in debug mode on port 5001
    app.run(debug=True, host='0.0.0.0', port=5001)