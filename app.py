from flask import Flask

#__name__==__main__
app = Flask(__name__) #creating the instance of flask and passing the module __name__ 
                    # @ is the decorator in python
@app.route('/')     #routes-> just like different url paths and used for handling the different urls
                    #('/') is the home address
def hello():               #execute this function when home address is accessed
    return "Hello World"

if __name__ == '__main__':
    #app.debug = True    #this will not make the server to be restarted everytime you make changes or simple pass in app.run()

    app.run(debug = True)    
