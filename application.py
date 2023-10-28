from flask import Flask, send_from_directory
from flask import request
from flask_cors import CORS, cross_origin
from services.getprice import save_xls
from data.vendors import vendordata


application = Flask(__name__)


@application.route('/', methods=['GET'])
def hello():
    return 'Welcome'


@application.route("/api/prices/<path:filename>", methods=['GET'])
def test(filename):
    return send_from_directory('prices', filename, as_attachment=True)


@application.route("/api/allprices", methods=['GET'])
def allprices():
    for tienda in vendordata.keys():
        print(f'Descargando precios de {tienda}')
        save_xls(tienda)


@application.route("/api/vendors/<string:name>", methods=['GET'])
def vendor(name):
    return


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
