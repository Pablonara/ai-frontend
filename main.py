# import requirements needed
from flask import Flask, render_template, url_for, redirect, request, flash, Response, send_from_directory
from utils import get_base_url
import os
from werkzeug.utils import secure_filename
import requests
import json

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 80
base_url = get_base_url(port)
# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
	app = Flask(__name__)
else:
	app = Flask(__name__, static_url_path=base_url + 'static')


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# checks for file post req?
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
  
    return render_template('index.html')


@app.route(f'{base_url}/uploads/<path:filename>')
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

#@app.route() #change later
#def predict():

  ### FILL

#  return render_template('results.html', results = results)


if __name__ == '__main__':
	# IMPORTANT: change url to the site where you are editing this file.
	website_url = 'url'

	print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
	app.run(host='0.0.0.0', port=port, debug=True)


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename: str) -> bool:
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def api_upload():
    if request.json['url']:
        header, data = request.json['url'].split('base64,', 1)

        r = requests.post(PREDICT_URL, json={ "data": [data] })
        print(r.text)
        
        return Response(json.dumps(r.json()['data'][0]), headers={
            "Content-Type": "application/json"
        })
    else:
        return 'not ok!'