# import requirements needed
from flask import Flask, render_template, url_for, redirect, request
from utils import get_base_url

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 81
base_url = get_base_url(port)
# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
	app = Flask(__name__)
else:
	app = Flask(__name__, static_url_path=base_url + 'static')


@app.route('/')
def index():

 #if something:
    # FILL
    #return redirect(url_for('uploaded_file',filename=filename))
  
	return render_template('index.html')

#@app.route() #change later
#def predict():

  ### FILL

#  return render_template('results.html', results = results)


if __name__ == '__main__':
	# IMPORTANT: change url to the site where you are editing this file.
	website_url = 'url'

	print(f'Try to open\n\n    https://{website_url}' + base_url + '\n\n')
	app.run(host='0.0.0.0', port=port, debug=True)
