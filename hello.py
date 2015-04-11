# To run, fire up a shell, cd to correct directory, and type: $ python hello.py
# Head over to http://127.0.0.1:5000/ to see your hello world greeting. 


from flask import Flask  		 # Imports the Flask class.
app = Flask(__name__)			 # Creates an instance of the Flask class, which is our WSGI app.

@app.route('/')					 # Tells Flask what URL should trigger my function.
def hello_world():				 # My function, which holds ...
	return 'Hello world!'		 # ... the message I want to display in my browser. 

if __name__ == '__main__':		 # Makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module. 
	app.run()			 		 # Runs the local server with my app. 

