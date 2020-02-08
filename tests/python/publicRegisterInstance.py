from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from json import dumps
from flask import jsonify

from coin_pkg import *

app = Flask(__name__)
api = Api(app)

class ListAllCoins(Resource):
    def get(self):
        dbConnection = sqlite3.connect(coinConfig.db_file_pub_register)
        cursor = dbConnection.cursor()
        cursor.execute("select coinId, pubKey from pub_register")
        result = [{'coinId' : rowCoinId, 'pubKey' : pubKey} for rowCoinId, pubKey in cursor.fetchall()]
        cursor.close()
        dbConnection.close()
        return result

class GetCoin(Resource):
    def get(self,coinId):
        dbConnection = sqlite3.connect(coinConfig.db_file_pub_register)
        cursor = dbConnection.cursor()
        cursor.execute("select pubKey from pub_register where coinId=?",(coinId,))
        pubKey = cursor.fetchone()
        if pubKey is None:
            result = {'error': 'brak monety o id {0}'.format(coinId)}
        else:
            result = {'coinId': coinId, 'pubKey': pubKey}
        cursor.close()
        dbConnection.close()
        return result

class AddTransaction(Resource):
    def post(self,coinId):
        errorMessage = None
        json_data = request.get_json(force=True)
        publicKey = json_data['publicKey']
        sign = json_data['sign']
        publicRegister = PublicRegister()

        if publicKey is None or sign is None:
            errorMessage = 'nie podano wymaganych parametrów sign: {0} oraz publicKey: {1}'.format(sign,publicKey)
        elif not publicRegister.transaction(coinId=coinId
                                           ,newPublicKey=publicKey.encode( 'ascii' )
                                           ,sign=sign):
            errorMessage = 'podpis się nie zgadza'

        return {'success' : 'dokonano modyfikacji klucza dla monety {0}'.format(coinId)} \
            if errorMessage is None \
            else {'error' : 'nie dokonano modyfikacji klucza dla monety {0}, powód to {1}'.format(coinId,errorMessage)}

api.add_resource(ListAllCoins,'/all') # wszystkie monety
api.add_resource(GetCoin,'/coin/<coinId>')  # wybrana moneta
api.add_resource(AddTransaction,'/transaction/coin/<coinId>')  # wybrana moneta
# /coin/<coinId>/publicKey/<pubKey>/sign/<sign>

if __name__ == '__main__':
    app.run(port='5002', debug=True)



'''
class Employees_Name(Resource):
    def get(self, employee_id):
        # conn = db_connect.connect()
        query = dbConnection.execute("select * from employees where EmployeeId =%d " % int(employee_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
'''
