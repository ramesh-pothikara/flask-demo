from operator import sub
from flask import Flask, render_template
from concurrent.futures import process
from flask import render_template, redirect, url_for, request
from forms import S_Restart
import subprocess
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/s_restart', methods=['GET', 'POST'])
def service_restart_page():
    global ip_addr
    global process
    #form = S_Restart()
    if request.method == 'GET':
      print("In GET")
      #return render_template('service_restart.html', form=form, first_load=1,disabled = False,ip = "" )
      return render_template('service_restart.html', submit_btn_disable= "NO")
    elif request.method == 'POST':
        message = ""
        # if submit button is clicked
        # call stop_service()
        ip_addr = request.form.get("ip_addr")
        if validate_ip(ip_addr) == 1:
            message = "Invalid IP Address format"
            return render_template('service_restart.html', submit_btn_disable= "NO", message= message)

        print("submit clicked 0")
        stop_service()
        #time.sleep(5)
        status_rtn = check_status()
        return render_template('service_restart.html', data = ip_addr + "\n" + status_rtn[0].decode('utf-8') + "\n" + status_rtn[1].decode('utf-8'), ip_addr= ip_addr,submit_btn_disable= "YES" )
    

@app.route('/sayhi')
def sayhi():
    return render_template('sayhi.html')

def check_status():
    error01 = None
    stdout01 = None

    error01 = proc.stderr.read()
    stdout01 = proc.stdout.read()

    print(error01)
    return  [error01,stdout01]

def stop_service():
    global proc
    proc = subprocess.Popen('c:/users/ramesh/test.bat', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   
    return

def validate_ip(ip):
    part = ip.split(".")
    if not (len(part) == 4):
        return 1
    for i in part:
        if int(i) > 255:
            return 1
        if not isinstance(int(i),int):
            return 1
    return 0    

if __name__ == '__main__':
    app.run(debug=True)    