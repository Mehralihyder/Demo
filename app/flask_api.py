from flask import Flask,render_template,request
application=Flask(__name__)
@application.route("/")
def index():
    return  render_template('index.html')

@application.route("/my_name/" ,methods=['POST'])
def my_name():
    aa=request.form['a']
    bb=request.form['b']
    cc=request.form['c']
    out=int(aa)+int(bb)
    out1=int(out)/int(cc)


    return render_template('index.html',results=out1)

if __name__=="__main__":
    application.run(host="localhost",port=3439)
