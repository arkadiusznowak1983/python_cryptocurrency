import coinConfig
import coinKeys
from KeysClass import Keys

# pair = coinKeys.generateNewKeyPair( coinId = 1, password="asd" )

class Coin:
    coinId = None
    keys = None

    def setPubKey( self, pubKey ):
        self.keys.pubKey = pubKey

    # setters
    def setCoinId( self, coinId ):
        self.coinId = coinId
    def setKeys( self, keys ):
        self.keys = keys
    # getters
    def getCoinId( self ):
        return self.coinId
    def getKeys( self ):
        return self.keys

    def __init__( self, coinId ):
        self.setCoinId(coinId)

    def __init__( self, coinId, pubKey ):
        self.setCoinId( coinId )
        self.setPubKey( pubKey )

    def __init__(self, coinId, keys=None):
        self.setCoinId(coinId)
        self.setKeys(keys)

    def __str__( self ):
        return "[coinId]: " + str( self.coinId )\
               + "\n[keys]\n" + str( self.keys )






def __TransferClass__():
    print( "TransferClass: Initialize Transfer Classes" )

if __name__ == "TransferClass" or __name__ == "__main__":
    __TransferClass__()



