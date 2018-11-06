from flask import Flask, render_template, request, send_from_directory
import py_time , report, lazydb, download

app = Flask(__name__) #define app using flask

@app.route('/') #首頁
def test():
    draft = report.get_draft("https://udn.com/news/index")

    data= {"date": py_time.get_date(),
    	   "time": py_time.get_time(),
    	   "report": ""}

    return render_template("index.html", data=data)

@app.route('/test2') #首頁
def test2():
    draft = report.get_draft("https://udn.com/news/index")

    db=lazydb.init("busy_hw4")
    lazydb.insert(db, "busy_hw4", report.speech(draft)) #寫入leveldb

    data= {"date": py_time.get_date(),
    	   "time": py_time.get_time(),
    	   "report": lazydb.search(db, "busy_hw4")}

    download.check_and_create("gossip")
    download.sound(data["report"])

    return render_template("index.html", data=data)

@app.route('/test3/<path:filename>', methods=['GET','POST'])
def test3(filename):
    return send_from_directory(directory="gossip", filename=filename)


if __name__ == '__main__':
    app.run(debug=True, port=1487)