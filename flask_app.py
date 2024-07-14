from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return <p>Hello world!</p>

'''
De reactie van de terminal op get commando 'git checkout -b main is':
"Switched to a new branch 'main'

Gevolg van ingeven van commando: 'git checkout -b main'

git maakt een nieuwe 'tak' aan van de hoofd repository en schakeld om naar deze tak
hiermee kunnen we werken aan deze tak terwijl we altijk nog kunnen terugschakelen naar
de orginele tak, of deze later met elkaar samenvoegen.
'''

if __name__ == '__main__':
    app.run(port=5000,debug=True)

