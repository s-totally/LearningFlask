from flask import Flask, render_template

#Create a new usable instance of the Flask class and save it into the variable app
app = Flask(__name__)

#Map the URL "/" to the Python function index.
#The Python function uses the Flask function render_template to render index.html. 
#So now when a user types in the URL "/", the function index will run and return the page index.html. 

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")	
	

#app.run runs the app on a local server, the debug=True flag here is set so that we'll see any error messages along the way.
if __name__ == "__main__":
    app.run(debug=True)
	
