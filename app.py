import logging
import os
import sys
from dotenv import load_dotenv

from flask import (
    Flask,
    jsonify,
    render_template,
    request
)
from logger import log
from db import DB

load_dotenv('/home/azureuser/Ansible/.env')
mydb = DB()



logging.basicConfig(filename="LOG_ansible.log",
                    filemode="a",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')




app = Flask(__name__)


    # "GET /" pour renvoyer le template de bienvenue

    # "GET /inc" qui incrément l'id dans la bdd

    # "GET /id" qui renvoie l'id en cours




@app.route("/")
@log
def index():
    # DB.set_table()
    return render_template('index.html')

#------------- init flask .py------------
@log
@app.route('/id', methods=['GET', 'POST'])
@app.route('/id/<name>', methods=['GET', 'POST'])
def id(name='undefine'):
    r = request.form
    user = r['user']
    if not user:
        with DB() as mydb:
            max_users = mydb.get_max()
            mydb.insert_user(name)
        return render_template('id.html', name=name) 
    else:
        return render_template('id.html', name=user) 

@log
@app.route('/json', methods=['GET'])
def results():
    with DB() as mydb:
        resp = jsonify(mydb.get_users())
    return resp

# @app.route("/inc", methods=['GET'])
# @log
# def inc():
#     mydb.insert_user(name)



@log
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

@log
@app.errorhandler(500)
def special_exception_handler(error):
    return 'Database connection failed', 500

@log
@app.route('/hello/<name>')
def hello(name):
    return 'Hello {} !'.format(name.capitalize())


if __name__ == '__main__':
    with DB() as mydb:
        mydb.del_table()
        mydb.set_table()
        mydb.test_insert()
        app.run(host='0.0.0.0', port=int(os.environ['FLASK_RUN_PORT']), debug=True)