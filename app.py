from flask import Flask, jsonify

app = Flask(__name__)

# Lista de frutas
fruits = ["Maca", "Banana", "Laranja", "Pera", "Manga"]

# Rota que retorna a lista de frutas
@app.route('/fruits', methods=['GET'])
def get_fruits():
    return jsonify(fruits), 200

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)