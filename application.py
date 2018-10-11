from flask import Flask, redirect, render_template, url_for, request
import os

app = Flask(__name__)

app_root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
	#return app_root
	return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    target = os.path.join(app_root, 'files')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    
    print(request.files.getlist("file"))
    
    for upload in request.files.getlist("file"):
        
        print(upload)
        
        print("{} is the file name".format(upload.filename))
        
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        
        if (ext == ".csv"):
            print("File supported moving on...")
        else:
            render_template("Error.html", message="Files uploaded are not supported...")
        
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("upload_successful.html", filename=filename)

@app.route("/send", methods=["POST"])
def send():
	
	return ("sending mails")