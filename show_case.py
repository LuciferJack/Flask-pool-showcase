#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8
from PyMysqlPool.mysql.connector.flask.mysql import MySQL
from flask import Flask
from flask import json
from flask import render_template
from flask import request
from FlaskPoolShowcase.util.log_util import get_caller_info_total
from FlaskPoolShowcase.util.logger_err import rootLogger

app = Flask(__name__,template_folder='flaskPoolShowcase/flask_templates')

#mysql config
app.config.update(
    DEBUG=False,
    MYSQL_DATABASE_HOST='10.95.130.***',
    MYSQL_DATABASE_PORT=8899,
    MYSQL_DATABASE_USER='root',
    MYSQL_DATABASE_PASSWORD='******',
    MYSQL_DATABASE_DB='flask',
    MYSQL_USE_POOL=
    {
        #use = 0 no pool else use pool
        "use":0,
        # size is >=0,  0 is dynamic pool
        "size":10,
        #pool name
        "name":"local",
    },
)
mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def main():
    #return "Welcome!"
    mysqlTest()
    return render_template('index.html')


@app.route("/mysqlTest")
def mysqlTest():
    cursor = mysql.get_db().cursor()
    _sql = "select * from flask_test"
    _args= ()
    result = ()
    try:
        cursor.execute(_sql, _args)
        result = cursor.fetchall()
    except:
        pass
        rootLogger.error("query exception sql is %s ,_args is %s,stacks is %s", _sql, _args, get_caller_info_total())
        rootLogger.exception("message")
    finally:
        cursor.close()
    return render_template('index.html')

@app.route('/showMountUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/mountUp',methods=['GET'])
def mountUp():
    # read the posted values from the UI
    print "mountUp"

@app.route('/signUp',methods=['POST'])
def signUp():

    # read the posted values from the UI
    _name = request.form['inputTitle']
    _email = request.form['inputContent']
    _password = request.form['inputCategory']
    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()