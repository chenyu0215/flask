from flask_restful import Resource,reqparse
from flask import jsonify
import pymysql


parser = reqparse.RequestParser()
parser.add_argument('balance')
parser.add_argument('account_number')


class Accounts(Resource):
    def db_init(self):
        db = pymysql.connect('192.168.56.105','irene','admin123','flask_api')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db,cursor

    def get(self):
        db = pymysql.connect('192.168.56.105','irene','admin123','flask_api')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """Select * From flask_api.accounts where deleted = False"""
        cursor.execute(sql)
        accounts = cursor.fetchall()
        db.close()
        response = {
            'data': accounts
        }
        return jsonify(response)
    def post(self):
        db,cursor = self.db_init()
        arg = parser.parse_args()
        account = {
            'balance':arg['balance'],
            'account_number':arg['account_number'],
        }
        sql = """
            Insert into flask_api.accounts
            (balance,account_number)
            values('{}','{}')
            """.format(account['balance'],account['account_number'])
        result = cursor.execute(sql)
        db.commit()
        db.close()
        response = {
            'result':True
        }
        return jsonify(response)


class Account(Resource):
    def db_init(self):
        db = pymysql.connect('192.168.56.105','irene','admin123','flask_api')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db,cursor
    def get(self,id):
        db,cursor = self.db_init()
        sql = """Select * From flask_api.accounts
                where id = '{}'
        """.format(id)
        cursor.execute(sql)
        account = cursor.fetchone()
        db.close()
        response = {
            'data':account
        }
        return jsonify(response)
    def patch(self,id):
        db,cursor = self.db_init()
        arg = parser.parse_args()
        account = {
            'balance':arg['balance'],
            'account_number':arg['account_number'],
        }  
        query = []
        for key,value in account.items():
            if value !=None:
                query.append(key + '=' + " '{}' ".format(value))  
        query = ','.join(query)
        sql = """ Update flask_api.accounts Set {} where id = "{}"
        """.format(query,id)
        result = cursor.execute(sql)
        db.commit()
        db.close()
        response = {
            'result':True
        }
        return jsonify(response)
    def delete(self,id):
        db,cursor = self.db_init()
        sql = """Update flask_api.accounts Set deleted = True where id = "{}"
        """.format(id)
        cursor.execute(sql)
        db.commit()
        db.close()
        response = {
            'result':True
        }
        return jsonify(response)