from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', )

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		return redirect(url_for('index'))

		# do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else


	# show the form, it wasn't submitted
	return render_template('login.html', )

if __name__ == '__main__':
	app.run(debug=True)
