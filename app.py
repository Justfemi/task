import flask
from flask import render_template, abort
from flask import jsonify
from flask import request
app = flask.Flask(__name__)

products = [
    {'id':'1', 'name': 'Bags of Rice', 'price': 20000, 'in-stock': 'yes'},
    {'id':'2', 'name': 'Pairs of shoes', 'price': 5000, 'in-stock': 'yes'},
    {'id':'3', 'name': 'Shirt', 'price': 2500, 'in-stock': 'yes'}
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/products/product', methods=['GET'])
def getAllprod():
    return jsonify({'products':products})

@app.route('/products/product/<productID>', methods=['GET'])
def getprod(productID):
    user = [ prod for prod in products if (prod['id'] == productID) ]
    return jsonify({'prod': user})

@app.route('/products/product/<productID>', methods=['PUT'])
def updateprod(productID):
    fm = [ prod for prod in products if (prod['id'] == productID) ]
    if 'name' in request.json:
        em[0]['name'] = request.json['name']
    if 'in-stock' in request.json:
         fm[0]['in-stock'] = request.json['in-stock']
    return jsonify({'prod': fm[0]})    

@app.route('/products/product', methods=['POST'])
def createprod():
    data = {
        'id':reguest.json['id'],
        'name':reguest.json['name'],
        'price':reguest.json['price'],
        'in-stock':reguest.json['in-stock']
    }
    product.append(data)
    return jsonify(data)

@app.route('/products/product/<productID>', methods=['DELETE'])
def deleteprod(productID):
    pl = [ prod for prod in products if (prod['id'] == productID)]
    if len(pl) == 0:
        abort(404)
    products.remove(fm[0])
    return jsonify({ 'response':'success'})
if __name__ == '__main__':
    app.run()