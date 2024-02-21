from flask import Flask, render_template, request, send_file
import model  # Import your ML model module
import model2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST'])
def display_map():
    query = request.form['query']  # Get user input from the form
    # Pass the user input to your ML model and get the result
    result=model.process_query(query)
    result.save('map.html')
    # Process the result as needed
    # Save the result to a file (e.g., map.html)
    
    return send_file('map.html')

@app.route('/map2', methods=['POST'])
def display_map2():
    text = request.form['language-origin']  # Get user input from the form
    # Call the predict function from model2.py with the user input
    result2= model2.Predict(text)
    result2.save('map2.html')
    return send_file('map2.html')


if __name__ == '__main__':
    app.run(debug=True)
