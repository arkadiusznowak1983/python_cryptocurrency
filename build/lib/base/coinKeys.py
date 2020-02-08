import coinConfig
from KeysClass import Keys

import sqlite3
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import binascii

def generateNewKeyPair( coinId = None, password = None ):
    keyPair = RSA.generate( coinConfig.keyLength )
    # passphrase = str( coinId ) if password is None else password
    # passphrase = str( coinId ) if password is None else password
    return Keys( keyPair.publickey().exportKey( passphrase = "12345" )
                ,keyPair.exportKey( passphrase = "12345" ) )

def getPubRegisterCoinPubKey( coinId ):
    try:
        sqliteConnection = sqlite3.connect( coinConfig.db_file )
        cursor = sqliteConnection.cursor()
        cursor.execute( "SELECT * FROM pub_register WHERE coinId=?", (coinId,) )
        pubKey = cursor.fetchone()[1]
        cursor.close()
    except sqlite3.Error as error:
        print( "Error while connecting to sqlite", error )
    finally:
        if ( sqliteConnection ):
            sqliteConnection.close()
        return pubKey

def getWalletCoinPrivKey( coinId ):
    try:
        sqliteConnection = sqlite3.connect( coinConfig.db_file )
        cursor = sqliteConnection.cursor()
        cursor.execute( "SELECT * FROM main_wallet WHERE coinId=?", (coinId,) )
        privKey = cursor.fetchone()[1]
        cursor.close()
    except sqlite3.Error as error:
        print( "Error while connecting to sqlite", error )
    finally:
        if ( sqliteConnection ):
            sqliteConnection.close()
        return privKey

def getRSAPubKey( pubKey ):
    return RSA.import_key( extern_key = pubKey
                          ,passphrase = "12345" )
def getRSAPrivKey( privKey ):
    return RSA.import_key( extern_key = privKey
                          ,passphrase = "12345" )
def toBytePubKey( pubKeyAscii ):
    return pubKeyAscii.encode( 'ascii' )
def toBytePrivKey( privKeyAscii ):
    return privKeyAscii.encode( 'ascii' )
def toAsciiPubKey( pubKeyByte ):
    return pubKeyByte.decode( 'ascii' )
def toAsciiPrivKey( privKeyByte ):
    return privKeyByte.decode( 'ascii' )
def getSignatureDigest( coinId ):
    digest = SHA256.new()
    digest.update( toBytePubKey( getPubRegisterCoinPubKey( coinId ) ) )
    return digest

def getSignature( coinId, asAscii = False ):
    signer = PKCS1_v1_5.new( getRSAPrivKey( getWalletCoinPrivKey( coinId ) ) )
    signature = binascii.hexlify( signer.sign( getSignatureDigest( coinId ) ) )
    return signature.decode( 'ascii' ) if asAscii else signature

def isSignatureVerified( coinId ):
    verifier = PKCS1_v1_5.new( getRSAPubKey( getPubRegisterCoinPubKey( coinId ) ) )
    return True if verifier.verify( getSignatureDigest( coinId ), binascii.unhexlify( getSignature( coinId ) ) ) else False

def test( coinsIds = [ 1 ] ):
    print( "============= Test coins =============" )
    for coinId in coinsIds:
        print( "coin: ", coinId, ( "Verified" if isSignatureVerified( 1 ) else "Incorrect" ) )

def __coinKeys__():
    print( "coin: Initialize Coin Keys" )

if __name__ == "coinKeys" or __name__ == "__main__":
    __coinKeys__()
