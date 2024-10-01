#!/usr/bin/env python3

from flask import Flask
#initialize the flask app
app = Flask(__name__)

#route for index page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print the console
    return parameter # to display in the web browser

#route to count from 0 to a specified parameter
@app.route('/count/<int:parameter>')
def count(parameter):
    # Join numbers from 0 to parameter into a string with newlines, and add a trailing newline
    return '\n'.join(str(i) for i in range(parameter)) + '\n'
    
#Route for math operation
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform the appropriate math operation based on the specified operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        #Handle division by zero
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation.' # Return an error for invalid operations
    return str(result)#Return the result as a string

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True) #Start the Flask development server on port 5555
