from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "<p>Dit is het huiswerk van Patrick Kox voor de NHA opleiding: 'programmeren voor Beginners'</p>"

if __name__ == '__main__':
    app.run(port=5000,debug=True)

