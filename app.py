from flask import Flask, render_template
import psutil
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/status")
def status():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return render_template("status.html", cpu=cpu, mem=mem)

@app.route("/dashboard")
def dashboard():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = int(time.time() - psutil.boot_time()) // 3600
    load1, load5, load15 = os.getloadavg()
    net = psutil.net_io_counters()
    sent_mb = net.bytes_sent // (1024*1024)
    recv_mb = net.bytes_recv // (1024*1024)

    return render_template(
        "dashboard.html",
        cpu=cpu,
        mem=mem,
        disk=disk,
        uptime=uptime,
        load1=load1,
        load5=load5,
        load15=load15,
        sent_mb=sent_mb,
        recv_mb=recv_mb
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

 
