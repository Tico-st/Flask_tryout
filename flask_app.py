from flask import Flask
app=Flask(__name__)
if __name__ == '__main__':
    app.run(port=5000,debug=True)

@app.route('/')
def Hello_world():
    return "<p>Welcome to my Flask app!</p>"
