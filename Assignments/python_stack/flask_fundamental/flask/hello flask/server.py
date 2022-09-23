from flask import Flask  
app = Flask(__name__)   

@app.route('/')          
def hello():
    return "hello world"

@app.route('/dojo')          
def dojo():
    return "Dojo"
  
  

@app.route('/say/<name>')          
def hello(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<name>')          
def pattern(name):
    return ((name+" ")*35)

@app.route('/repeat/<name>') 
def second(name):
    return ((name+" ")*80)

@app.route('/repeat/<name>') 
def third(name):
    return ((name+" ")*99)
    


if __name__=="__main__":   
    app.run(debug=True)  
