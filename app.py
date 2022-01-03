from flask import Flask, request, render_template,url_for
from flask_cors import cross_origin
import base64

app = Flask(__name__)

@app.route("/")
@cross_origin()
def home():
    global blobPDF
    blobPDF = convertToBinaryPDFData()
    blobIMAGE = convertToBinaryImageData()
    return render_template("index.html",blobPDF=blobPDF,blobIMAGE=blobIMAGE)


def convertToBinaryPDFData():
    '''PDF data'''
    # Convert digital data to binary format
    with open('static/abc.pdf', 'rb') as file:
        binaryData = file.read()
    binaryData = base64.b64encode(binaryData).decode("utf-8")
    return binaryData

def convertToBinaryImageData():
    '''Image data'''
    # Convert digital data to binary format
    with open('static/abc.png', 'rb') as file:
        binaryData = file.read()
    binaryData = base64.b64encode(binaryData).decode("utf-8")
    return binaryData


@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html',blobPDF=blobPDF)



if __name__ == "__main__":
    app.run(debug=True)


