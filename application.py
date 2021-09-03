from flask import Flask, render_template, jsonify

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

    
@application.route("/", methods=['POST', 'GET'])
def index():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')

@application.route('/users', methods=['GET'])
def users():
    data = {'users': [{'name': 'Jerry', 'age': 21, 'email': 'jerry@gmail.com'}, 
    {'name': 'Jerry', 'age': 21, 'email': 'jerry@gmail.com'}]}
    return data

@application.route('/new', methods=['POST'])
def new():
    data = request.json
    return {
        "message": "Success",
        "status": 200,
        "data": data
    }
  
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0')