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
	
	target = os.path.join(app_root, 'files')
	filename = request.form.get("file")

	return filename
	'''
	# sending mails code
	file = pandas.read_csv("/".join([target, filename]))

	file = file.values


	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("man11invisible", "12345@@@@@")

	#server = smtplib.SMTP_SSL('smtp.ipage.com', 465)
	#server.login("sharmahrishabh@cevgroup.org", "CEVgroup123")

	for i in file:
	    
	    server.sendmail(
	      "sharmahrishabh@cevgroup.org", 
	      i, 
	      "Hello! keep up with you good work.")
	    print(str(i),"\n")  
	    time.sleep(60)

server.quit()

	return ("sending mails")
	'''