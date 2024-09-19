from flask import Flask, session, redirect, request, url_for, render_template
from main_db_controll import db
import os

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def index():
   data = db.get_data()
   return render_template('main.html', data=data)
   
def add():
   file = request.files['file']
   if file and allowed_file(file.filename):
      # Сохранение файла в указанной папке
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
   form_data = tuple(request.form.values()) + (file.filename,)
   db.add_data(form_data)
   return redirect(url_for('index'))

app = Flask(__name__)
app.add_url_rule('/', 'index', index, methods=["GET"])
app.add_url_rule('/add', 'add', add, methods=["POST"])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if __name__ == '__main__':
   if not os.path.exists(UPLOAD_FOLDER):
      os.makedirs(UPLOAD_FOLDER)
   app.run(debug=True)