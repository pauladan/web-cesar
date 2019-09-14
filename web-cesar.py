from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

# page_header = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>FlickList</title>
#     </head>
#     <body>
#         <h1>FlickList</h1>
# """

# page_footer = """
#     </body>
# </html>
# """

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method='POST'>
            <label>Rotate by:
                <input name="rot" type="text" value=0 />
            </label>
            <label>
                <textarea name="text" type="text"></textarea>
            </label>
            <input type="submit" /> 
        
    </body>
</html>
"""

@app.route ("/", methods = ['POST'])
def encrypt():
    rotation = int(request.form['rot'])
    original_text = str(request.form['text'])

    encrypted_txt = rotate_string(original_text, rotation)
    return '<h1>' + encrypted_txt + '</h1'



@app.route("/")
def index():
    return form

app.run()
