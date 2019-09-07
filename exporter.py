#!/usr/bin/python

# Import libs
from flask import Flask,render_template
from subprocess import call

# Call another python file
called_file = '/Users/victorcamargo/Desktop/metrics-exporter/called/call.py' # sera substituida pelo hieradata
call(["python", called_file])

# Flask class object instanced
app = Flask(__name__)

# Endpoint defined
@app.route("/metrics")

# Content defined
def content():
    # Environment variables
    file = '/Users/victorcamargo/Desktop/metrics-exporter/templates/textfile.txt' # sera substituida pelo hieradata

    # Variable text is defined by file that will be opened
    text = open(file, 'r+')

    # Variable content is defined by content in file opened
    content = text.read()

    # Close file
    text.close()

    # Function that return the content in content.html
    return render_template('metrics.html', text=content)

# Set options for application
if __name__ == '__main__':
    debug = 'True' # sera substituida pelo hieradata
    port = 9150 # sera substituida pelo hieradata
    app.run(debug = debug, port = port)