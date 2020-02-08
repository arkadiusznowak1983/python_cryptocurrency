from coin_pkg import *

# class to store and manage asymmetric keys
class Keys:
    from coin_pkg.base.coinKeysClass import coinKeys
    pubKey = None
    privKey = None

    # setters
    def setPubKey( self, pubKey = None, pubKeyRSA = None ):
        self.pubKey = pubKeyRSA if pubKey is None else coinKeys.getRSAPubKey( pubKey = pubKey )
    def setPrivKey( self, privKey = None, privKeyRSA = None ):
        self.privKey = privKeyRSA if privKey is None else coinKeys.getRSAPrivKey( privKey = privKey )

    # getters
    def getPubKey( self ):
        return self.pubKey;
    def getPrivKey( self ):
        return self.privKey;

    # cast, format & map
    def pubKeyToByte( self ):
        return self.pubKey.exportKey().encode( 'ascii' )
    def pubKeyToAscii( self ):
        return self.pubKey.exportKey().decode( 'ascii' )
    def privKeyToByte( self ):
        return self.privKey.exportKey()
    def privKeyToAscii( self ):
        return self.privKey.exportKey()

    # constructors
    def __init__( self, pubKey = None, privKey = None, pubKeyRSA = None, privKeyRSA = None ):
        self.setPubKey( pubKeyRSA = pubKeyRSA ) if pubKey is None else self.setPubKey( pubKey = pubKey )
        self.setPrivKey( privKeyRSA = privKeyRSA ) if privKey is None else self.setPrivKey( privKey = privKey )

    # string representation
    def __str__(self):
        return "=== pubKey ===\n" + self.pubKey.exportKey().decode( 'ascii' )[:80] \
               + "\n=== privKey ===\n" + self.privKey.exportKey().decode( 'ascii' )[:80]


if __name__ == "KeysClass" or __name__ == "__main__":
    print( "KeysClass: Keys classes" )