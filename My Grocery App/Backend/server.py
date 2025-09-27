

from flask import Flask,request,jsonify
from sql_connection import get_sql_connection
from Backend import product_dao

app = Flask(__name__)
connect=get_sql_connection()
@app.route('/getProducts',methods=['GET'])
def get_products():
    products=product_dao.get_all_products()
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Store Management System")
    app.run(port=5000)