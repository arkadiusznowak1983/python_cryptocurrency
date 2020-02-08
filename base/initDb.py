import coin_pkg
from coin_pkg import *

import sqlite3
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def createTables():
    try:
        sqliteConnection = sqlite3.connect( coinConfig.db_file )
        cursor = sqliteConnection.cursor()

        cursor.execute( coinConfig.createTablePubReg )
        cursor.execute( coinConfig.createTableMainWallet )
        cursor.execute( coinConfig.createTableTransactions )

        cursor.close()
        print( "Tables created" )
    except sqlite3.Error as error:
        print( "Error while connecting to sqlite", error )
    finally:
        if ( sqliteConnection ):
            sqliteConnection.close()
            print( "The SQLite connection is closed" )

def createFirstCoins():
    try:
        sqliteConnection = sqlite3.connect( coinConfig.db_file )
        cursor = sqliteConnection.cursor()

        initialPubRegister = []
        initialMainWallet = []
        for coinId in range( 1, 5 + 1 ):
            keys = RSA.generate( 1024 )
            initialPubRegister.append( (coinId, keys.publickey().exportKey().decode( 'ascii' ) ) )
            initialMainWallet.append( (coinId, keys.exportKey().decode( 'ascii' ) ) )

        cursor.executemany( 'INSERT INTO pub_register VALUES(?,?);', initialPubRegister );
        print( 'Inserted ', cursor.rowcount, 'records to the table pub_register.' )
        cursor.executemany( 'INSERT INTO main_wallet VALUES(?,?);', initialMainWallet );
        print( 'Inserted ', cursor.rowcount, 'records to the table main_wallet.' )

        sqliteConnection.commit()
        cursor.close()
        print( "Tables created" )
    except sqlite3.Error as error:
        print( "Error while connecting to sqlite", error )
    finally:
        if ( sqliteConnection ):
            sqliteConnection.close()
            print( "The SQLite connection is closed" )

def initTables():
    createTables()
    createFirstCoins()

def __initDb__():
    print( "initDb: SqlLite Database Initialization" )

if __name__ == "initDb" or __name__ == "__main__":
    __initDb__()