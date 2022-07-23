import requests
from flask import Flask, render_template

app = Flask(__name__)

r = requests.get('https://script.google.com/macros/s/AKfycbyNRCy33Mwq-03Gx6cDgz27cgyJOXmCgRhl-SINcbKY14A9L6IKbdHpRO49ylWCpD7PmA/exec')
j = r.json()
# print(j)

# name = input('Name: ')
# o = requests.get(f'https://script.google.com/macros/s/AKfycbyNRCy33Mwq-03Gx6cDgz27cgyJOXmCgRhl-SINcbKY14A9L6IKbdHpRO49ylWCpD7PmA/exec?college={name}')
# p = o.json()
# print(o.json())
# print(p['data'][])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/all')
def all():
	lst = j['data']
	return render_template('all.html', lst=lst)

@app.route('/college/<name>')
def college(name):
	o = requests.get(f'https://script.google.com/macros/s/AKfycbyNRCy33Mwq-03Gx6cDgz27cgyJOXmCgRhl-SINcbKY14A9L6IKbdHpRO49ylWCpD7PmA/exec?college={name}')
	oa = o.json()
	lst = oa['data']
	return render_template('college.html', college=oa, lst=lst)

if __name__ == '__main__':
	app.run(debug=True)




