from flask import Flask
from flask import render_template
import wikipedia
from flask import request
app = Flask(__name__)


@app.route('/')
def index():	
	user=request.args.get('user');
	strk=wikipedia.summary(user);
	return render_template('index.html',body=strk,user=user)

	
if __name__ == "__main__":
	app.run()