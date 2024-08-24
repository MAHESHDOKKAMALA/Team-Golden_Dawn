Python 3.12.5 (v3.12.5:ff3bc82f7c9, Aug  7 2024, 05:32:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request, redirect, url_for
... 
... app = Flask(__name__)
... 
... @app.route('/')
... def index():
...     return render_template('index.html')
... 
... @app.route('/submit-course', methods=['POST'])
... def submit_course():
...     course_name = request.form.get('course-name')
...     course_duration = request.form.get('course-duration')
...     course_category = request.form.get('course-category')
...     
...     # Process the form data here (e.g., save to database or perform some action)
...     print(f"Course Name: {course_name}")
...     print(f"Course Duration: {course_duration}")
...     print(f"Course Category: {course_category}")
... 
...     # Redirect or respond as needed
...     return redirect(url_for('index'))
... 
... @app.route('/login', methods=['POST'])
... def login():
...     username = request.form.get('username')
...     password = request.form.get('password')
...     
...     # Process login logic here
...     print(f"Username: {username}")
...     print(f"Password: {password}")
... 
...     # Redirect or respond as needed
...     return redirect(url_for('index'))
... 
... if __name__ == '__main__':
...     app.run(debug=True)
