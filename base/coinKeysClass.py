from coin_pkg import *


import Crypto
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import binascii

class coinKeys:
    def generateNewKeyPair( coinId = None, password = None ):
        from base.KeysClass import Keys
        keyPair = RSA.generate( coinConfig.keyLength )
        # passphrase = str( coinId ) if password is None else password
        # passphrase = str( coinId ) if password is None else password
        return Keys( pubKey = keyPair.publickey().exportKey( passphrase = "12345" )
                    ,privKey = keyPair.exportKey( passphrase = "12345" )
                    ,pubKeyRSA=None, privKeyRSA=None )

    def getPubRegisterCoinPubKey( coinId ):
        sqliteConnection = sqlite3.connect( coinConfig.db_file )
        try:
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
        sqliteConnection = sqlite3.connect(coinConfig.db_file)
        try:
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
        digest.update( self.toBytePubKey( self.getPubRegisterCoinPubKey( coinId ) ) )
        return digest

    def getSignature( coinId, asAscii = False ):
        signer = PKCS1_v1_5.new( self.getRSAPrivKey( self.getWalletCoinPrivKey( coinId ) ) )
        signature = binascii.hexlify( signer.sign( self.getSignatureDigest( coinId ) ) )
        return signature.decode( 'ascii' ) if asAscii else signature

    def isSignatureVerified( coinId ):
        verifier = PKCS1_v1_5.new( self.getRSAPubKey( self.getPubRegisterCoinPubKey( coinId ) ) )
        return True if verifier.verify( self.getSignatureDigest( coinId ), binascii.unhexlify( self.getSignature( coinId ) ) ) else False

    def __init__( self ):
        pass

