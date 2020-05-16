from flask import Flask, render_template, redirect, request

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

@app.route('/submit', methods = ['POST'])   #creating route for /submit address with POST method. In above cases GET is not passed bcoz it is already passed by defualt
def submit_data():
    if request.method == 'POST':                #handling methods and form functions using request function by importing it
        name = request.form['username']        #taking value from the form
        age = int(request.form['age'])          #taking integer value from the form

        f = request.files['userfile']           #file will be created in another dict 'files' unlike in other form field which is dict 'form'
        print(f)
        f.save(f.filename)                      #file have function to save the file. filename is used to save the file name with the original name of the file uploaded and location will be root folder
    return "<h1> Hello {} and your age is {}".format(name,age)         #printing the value from username and age


if __name__ == '__main__':
    #app.debug = True    #this will not make the server to be restarted everytime you make changes or simple pass in app.run()

    app.run(debug = True)    
