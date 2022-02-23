from flask import Flask, jsonify
from models.ngo import NGO, NGOEncoder
from extensions import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = NGOEncoder #Define qual o decodificador a app deve utilizar

@app.route('/')
def index():
    return '<h1>Encontre uma ONG</h1><p>Este site é um protótipo de API para encontrar ONGs pelo Brasil.</p>'

@app.route('/instituicoes', methods=['GET'])
def list_all():
    return jsonify({'ngos': db})
app.run()