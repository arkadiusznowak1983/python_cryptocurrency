from coin_pkg import *

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import binascii

# pair = coinKeys.generateNewKeyPair( coinId = 1, password="asd" )

class Transfer:
    coin = None
    newKeys = None
    signature = None

    publicRegister = None
    wallet = None

    # setters
    def setCoin( self, coin ):
        self.coin = coin
    def setNewKeys( self, newKeys ):
        self.newKeys = newKeys
    def setSignature( self, signature ):
        self.signature = signature
    def setPublicRegister( self, publicRegister ):
        self.publicRegister = publicRegister
    def setWallet( self, wallet ):
        self.wallet = wallet
    # getters
    def getCoin( self ):
        return self.coin
    def getNewKeys( self ):
        return self.newKeys
    def getSignature( self ):
        return self.signature

    # prepare new pair of asymmetric keys
    def prepareNewKeys( self, newKeys = None ):
        self.setNewKeys( newKeys = coinKeys.generateNewKeyPair( coinId = self.coin.coinId ) ) if newKeys is None else newKeys

    # generate signature
    def signNewTransaction( self ):
        digest = SHA256.new()
        digest.update( self.getCoin().getKeys().pubKey.exportKey() )
        print( "PUB: {0}".format(self.getCoin().getKeys().pubKey.exportKey()) )
        signer = PKCS1_v1_5.new( self.getCoin().getKeys().getPrivKey() )
        self.setSignature( signature = binascii.hexlify( signer.sign( digest ) ) )
        return self.getSignature()

    # transfer request to public coins registry
    def coinTransferRequest( self ):
        self.prepareNewKeys()
        self.signNewTransaction()
        print("Dane zlecenia zmiany wlasciciela monety w rejestrze publicznym")
        print((self.getCoin().getCoinId()
               , self.getNewKeys().getPubKey().exportKey()
               , self.getSignature().decode( 'ascii' )))
        if self.publicRegister.transaction( coinId = self.getCoin().getCoinId()
                                           ,newPublicKey = self.getNewKeys().getPubKey().exportKey().decode( 'ascii' )
                                           ,sign = self.getSignature().decode( 'ascii' ) ):
            print( "Powodzenie zamiany klucza publicznego" )
            self.wallet.addCoinToWallet( coinId = self.getCoin().getCoinId()
                                        ,privateKey = self.getNewKeys().getPrivKey().exportKey().decode( 'ascii' ) )
            print( "Dodano monetę do portfela" )
        else:
            print( "Niepowodzenie zmiany klucza publicznego" )


    def __init__( self, coin, newKeys = None ):
        self.setCoin( coin )
        self.setNewKeys( newKeys )

    def __str__( self ):
        return "[coin]\n" + str( self.coin ) \
               + "\n[newKeys]\n" + str( self.newKeys ) \
               + "\n[signature]: " + str( self.getSignature() )[:80]



def __TransferClass__():
    print( "TransferClass: Initialize Transfer Classes" )

if __name__ == "TransferClass" or __name__ == "__main__":
    __TransferClass__()

