from flask import Flask, request, send_file, render_template
import pyqrcode
import png
from pyqrcode import QRCode


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def qrcode():
   if request.method== 'POST' :
      data = request.form['data']
   
      print(request.form['data'])
      url = pyqrcode.create(data)
      url.png('static/QRCode.png', scale = 8)
   return render_template('index.html')
   
   

if __name__ == "__main__":
    app.run(debug=False)