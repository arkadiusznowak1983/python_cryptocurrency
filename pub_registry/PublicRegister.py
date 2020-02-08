from coin_pkg import *

class PublicRegister:
    sqliteConnection = None

    def getPubKey( self, coinId ):
        import sqlite3
        if self.sqliteConnection is None:
            flagCloseConnection = True
            self.sqliteConnection = sqlite3.connect( coinConfig.db_file )
        else:
            flagCloseConnection = False
        cursor = self.sqliteConnection.cursor()
        cursor.execute( "SELECT * FROM pub_register WHERE coinId=?", (coinId,) )
        pubKey = cursor.fetchone()[1]
        cursor.close()
        if flagCloseConnection:
            self.sqliteConnection.close()
            self.sqliteConnection = None
        return pubKey

    def verify( self, coinId, sign ):
        from Crypto.Hash import SHA256
        from Crypto.Signature import PKCS1_v1_5
        import binascii
        publicKey = self.getPubKey( coinId = coinId )
        print(publicKey)
        digest = SHA256.new()
        digest.update( publicKey.encode( 'ascii' ) )
        verifier = PKCS1_v1_5.new( coinKeys.getRSAPubKey( pubKey = publicKey ) )
        return True if verifier.verify( digest, binascii.unhexlify( sign ) ) else False

    def replacePublicKey( self, coinId, newPublicKey ):
        import sqlite3
        if self.sqliteConnection is None:
            flagCloseConnection = True
            self.sqliteConnection = sqlite3.connect(coinConfig.db_file)
        else:
            flagCloseConnection = False
        cursor = self.sqliteConnection.cursor()
        cursor.execute( "UPDATE pub_register SET pubKey=? WHERE coinId=?", (newPublicKey, coinId,))
        self.sqliteConnection.commit()

    def transaction(self, coinId, newPublicKey, sign):
        print("SIGN: {0}".format(sign))

        if self.verify( coinId = coinId, sign = sign ):
            self.replacePublicKey( coinId = coinId, newPublicKey = newPublicKey )
            # print( "Pub Key replaced" )
            return True
        else:
            # print( "Invalid signature" )
            return False
