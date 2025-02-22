import requests
from settings import CLIENT_SECRET
from flask import Flask, request, session, jsonify, redirect


API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '1342691151693615225'
REDIRECT_URI = 'http://localhost:5173/api/authorize'

def exchange_code(code):
  data = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post(f'{API_ENDPOINT}/oauth2/token', data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  print(r.json())
  return r.json()


app = Flask(__name__)
app.secret_key = 'afjhiuashdf'


@app.route('/api/authorize')
def authorize():
  code = request.args.get('code')
  exchanged_code = exchange_code(code)
  session['access'] = exchanged_code
  return redirect('/') # return the user upon successful authorization

@app.route('/api/get/session')
def get_session():
  session_data = session.get('access', None)
  return jsonify({'success':True if session_data else False,'session_data':session_data})


app.run(debug=True)