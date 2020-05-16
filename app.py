from flask import Flask, render_template, redirect

#__name__==__main__
app = Flask(__name__) #creating the instance of flask and passing the module __name__ 

friends = ["John","Tom", "Carry", "Jason"]      
number=15


                    # @ is the decorator in python
@app.route('/')     #routes-> just like different url paths and used for handling the different urls
                    #('/') is the home address
def hello():               #execute this function when home address is accessed
    return render_template("index.html", my_friends = friends, number = number)    #to return a html page which is created inside of template folder

@app.route("/about")    #creating the route for "/about" address
def about():
    return "<h1>About Page</h1>"    #directly returning the html code 

@app.route('/home')         #creating route for redirecting to home page when "/home" is accessed
def home():
    return redirect('/')     #simply pass the address where you want to redirect


if __name__ == '__main__':
    #app.debug = True    #this will not make the server to be restarted everytime you make changes or simple pass in app.run()

    app.run(debug = True)    
