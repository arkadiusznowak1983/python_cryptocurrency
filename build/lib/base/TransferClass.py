import coinConfig
import coinKeys
from KeysClass import Keys
from CoinClass import Coin
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import binascii

# pair = coinKeys.generateNewKeyPair( coinId = 1, password="asd" )

class Transfer:
    coin = None
    newKeys = None
    signature = None

    # setters
    def setCoin( self, coin ):
        self.coin = coin
    def setNewKeys( self, newKeys ):
        self.newKeys = newKeys
    def setSignature( self, signature ):
        self.signature = signature
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
        digest.update( self.getCoin().getKeys().privKeyToByte() )
        signer = PKCS1_v1_5.new( self.getCoin().getKeys().getPrivKey() )
        self.setSignature( signature = binascii.hexlify( signer.sign( digest ) ) )
        return self.getSignature()

    # transfer request to public coins registry
    def coinTransferRequest( self ):
        self.prepareNewKeys()
        self.signNewTransaction()

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





# coin unique id
coinId = 1

#  keys
keysPair = Keys( pubKey = coinKeys.getPubRegisterCoinPubKey( coinId = coinId )
                ,privKey = coinKeys.getWalletCoinPrivKey( coinId = coinId ) )

# coin
coin = Coin( coinId = coinId
            ,keys = keysPair )

# transfer
transfer = Transfer( coin = coin )
transfer.coinTransferRequest();
print( transfer )
