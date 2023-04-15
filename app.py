import os
from flask import Flask, render_template, request, send_file
from planner import create_html_map

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_map', methods=['POST'])
def generate_map():
    start_input = request.form['starting_point']
    dest_input = request.form['destination_point']

    create_html_map(start_input, dest_input)
    return send_file('route_map.html', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
