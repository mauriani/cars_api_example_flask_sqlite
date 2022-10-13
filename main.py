from flask import Flask, make_response, jsonify, request
import sqlite3

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('cars.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/carros', methods=['GET'])
def get_carros():
    conn = db_connection()

    cars = conn.execute("SELECT * FROM cars").fetchall()

    return make_response(
        jsonify(
            message='Lista de carros',
            data=cars
        )
    )


@app.route('/carros', methods=['DELETE'])
def delete_carros():
    carId = request.args.get('id')

    conn = db_connection()
    conn.execute("DELETE from cars WHERE id = ?", (carId))
    conn.commit()

    return make_response(
        jsonify(
            message='Carro deletado com sucesso',
        )
    )


@app.route('/carros', methods=['POST'])
def create_carros():
    try:
        conn = db_connection()

        data = request.json

        conn.execute(""" INSERT INTO cars(marca, modelo, ano) VALUES (?, ?, ?)""", (
            data['marca'],  data['modelo'], data['ano']
        ))

        conn.commit()

        return make_response(
            jsonify(
                message='Carro cadastrado com sucesso',
            )
        )

    except:
        conn().rollback()

    finally:
        conn.close()


app.run()
