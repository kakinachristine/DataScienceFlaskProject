from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/about')
def about():
    return 'About Page'

@app.route('/hello')
def hello():

    return render_template("index.html", name ="Student")

@app.route('/submit',methods=['POST'])
def submit():
    userText = request.form.get('text', 'No text submitted')
    return f"You submitted {userText}"

@app.route('/home')
def home():
    return "Hello Flask!"


if __name__ == '__main__':
    app.run(debug=True)
