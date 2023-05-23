#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp to say hello
"""
from flask import Flask  # From 'flask' module import 'Flask' class
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler (or view function)
def main():
    """Say hello"""
    return 'Hello, world!'

if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run()  # Launch built-in web server and run this Flask webapp




# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp to say hello
"""
from flask import Flask  # From 'flask' module import 'Flask' class
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler (or view function)
def main():
    """Say hello"""
    return 'Hello, world!'

if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run()  # Launch built-in web server and run this Flask webapp




@app.route('/')
@app.route('/hello')
@app.route('/hi')
def main():
    """Return an HTML-formatted string and an optional response status code"""
    return """
      <!DOCTYPE html>
      <html>
      <head><title>Hello</title></head>
      <body><h1>Hello, from HTML</h1></body>
      </html>
      """, 200





<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Say hello</title>
</head>
<body>
  <h1>Hello, from templates</h1>
</body>
</html>






