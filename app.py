from flask import Flask, render_template
from flask import jsonify


app = Flask(__name__,static_url_path='/assets',static_folder='assets',template_folder='assets/templates')

@app.route("/ping/")
def ping():
	data = {}
	data["text"]="pong"
	return jsonify(data),200

@app.route("/")
def hello():
	service = {}
	service["text"]="Hello, Racer!"	
	return render_template("index.html", service=service)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
