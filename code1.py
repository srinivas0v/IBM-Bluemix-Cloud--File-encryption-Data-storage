import base64
from cloudant.client import Cloudant
from cloudant import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

from flask import Flask, render_template, request, make_response
import swiftclient
import keystoneclient
import os
folder = './files'
ALLOWED_EXTENSIONS = set(['txt','pdf','jpg','jpeg','gif'])

version=int('0')

client = Cloudant("04d5af8d-9cd3-4a30-9faf-eabdac3434c9-bluemix", "1908f8ed148492aaf1d8b89912b684b7093be5b46005084c780f313f98494d43",
                  url="https://04d5af8d-9cd3-4a30-9faf-eabdac3434c9-bluemix:1908f8ed148492aaf1d8b89912b684b7093be5b46005084c780f313f98494d43@04d5af8d-9cd3-4a30-9faf-eabdac3434c9-bluemix.cloudant.com")
client.connect()
session = client.session()
dbName = "mydb"
myDb = client[dbName]
#to create the database
#myDb = client.create_database(dbName)
#if myDb.exists():
 #   print "database created"
print "here12"
#my_database = client[dbName]
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = folder


@app.route('/', methods=['POST','GET'])
def main_page():
    print "here1"
    if request.method == 'POST':
        if request.form['submit'] == 'Upload':
            f = request.files['file_upload']
            print "a"
            pushdoc(f.filename)

        elif request.form['submit'] == 'Download':
            f1 = request.form['file_download']
            print f1
            pulldoc(f1)

        elif request.form['submit'] == 'List':
            list()

        elif request.form['submit'] == 'Delete':
            id = request.form['file_delete']
            print id
            delete(id)

    return render_template('index.html')


def pushdoc(filename):
    fl = open('C:/Users/srinivas venkatesh/Documents/cloud computing/assg1/files' + "/" + filename, "rb", 2048)
    fdata = fl.read()
    version = int('0')
    fdata_encoded = base64.encodestring(fdata)
    print "ab"
    for document in myDb:
            if document['_id'] == filename:
                    version = int(document['version']) + 1
                    return 'File version Updated'
        # Create a document to be pushed cloudant
    data = {
            '_id': filename+'_'+str(version),
            'fileName': filename,
            'version': version,
            'fileContent': fdata_encoded
            }

        # Push the document to cloudant
    print "abc"
    my_document = myDb.create_document(data)
    print "upload"
    fl.close()
    return 'File Uploaded'


def list():
    list = ''
    list1 = ''
    for document in myDb:
        list = list + document['fileName']
        list1 = list1 + str(document['version'])
    print list +'_' + list1

def delete(docID):
    document = myDb[docID]
    document.delete()
    return 'File Delete Successful'

def pulldoc(filename):
    my_document = myDb[filename]
    fdata_decode = base64.decodestring(my_document['fileContent'] )
    dfile = open('C:/Users/srinivas venkatesh/Documents/cloud computing/assg2/downloads/'+filename,'wb')
    dfile.write(fdata_decode)
    dfile.close()
    # Display the document
    print my_document
  # for document in myDb:
    #   if document['fileName'] == filename:
     #      dfile = document.get_attachment(filename,attachment_type='binary')
      #     respose = make_response(dfile)
        #   respose.headers["Content-Disposition"] = "attachment; filename=%s"%fil
if __name__ == '__main__':
    app.run(debug=True,port=8000)

