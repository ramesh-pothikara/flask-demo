from operator import sub
from flask import Flask, render_template
from concurrent.futures import process
from flask import render_template, redirect, url_for, request
from forms import S_Restart
import subprocess

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
    form = S_Restart()
    if request.method == 'GET':
      return render_template('service_restart.html', form=form, first_load=1,disabled = False,ip = "" )
    elif request.method == 'POST':
        # if submit button is clicked
        # call stop_service()
        if form.submit.data:
            print("submit clicked")
            ip_addr = form.ip_addr.data
            stop_service()
            return render_template('service_restart.html', form=form, first_load=2,disabled = True,ip = ip_addr,  data="running")
        # if check_status button is clicked
        # call check_status()
        if form.check_status.data:
            print("check_status clicked")
            status_rtn = check_status()
            return render_template('service_restart.html', form=form, first_load=2,disabled = True,ip = ip_addr, data = status_rtn[0].decode('utf-8') + "\n" + status_rtn[1].decode('utf-8') )
    

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

if __name__ == '__main__':
    app.run(debug=True)    