from flask import Flask,render_template #using render we can import html files

app=Flask(__name__) # creating empty webapp

@app.route('/') #add to url to webapp(starting page url)
def index():
    return "Welcome to the Website!"

@app.route('/page1')
def page1():
    return "This is page 1"

@app.route('/page2')
def page2():
    return render_template('test-template.html') # this files should saved in template folder

app.run(debug=True) #can be edit in testing