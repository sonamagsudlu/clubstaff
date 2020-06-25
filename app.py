import datetime
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
	return render_template("authentication.html")

@app.route('/dashboard', methods=["POST"])
def dashboard():
	name=request.form.get('username')
	if(name == 'Admin'):
		activities=['Youth-Swimming', 'Senior Practice', 'Cook-out', 'Open-Bar']
		date=datetime.date.today()
		return render_template("dashboard.html", activities=activities, date=date, name=name)
	else:
		return render_template("authentication.html")