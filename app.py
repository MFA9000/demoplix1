from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# To run python file without re-running the flask command
def before_request():
    app.jinja_env.cache = {}
app.before_request(before_request)


# Routes
@app.route('/')  
def home():
    # fetch username
    first_name = ''
    try:
        session_id = request.args.get('session_id')
        raw_url = "https://micro-okta.herokuapp.com/api/name?session_id=%s"%(session_id)
        username_re = requests.get(raw_url)
        first_name, *rest_username = username_re.text.split()
    except Exception as e:
        print(e)
    return render_template('home.html', username=first_name)

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/login_callback')
def otp():
    return render_template('otp.html')
    

# init
if __name__ == '__main__':
    app.run(debug=True)

