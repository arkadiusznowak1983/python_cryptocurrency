import initDb
import coinKeys

def test_initTables():
    initDb.initTables()

def test_coinKeysSignature():
    coinKeys.test([ 1, 2 ])

def test_coinKeys_newPairWithoutCoinId():
    pair = coinKeys.generateNewKeyPair()
    print( pair.pubKey )
    print( pair.privKey )

def test_coinKeys_newPairWithCoinId():
    pair = coinKeys.generateNewKeyPair( coinId = 1 )
    print( pair.pubKey )
    print( pair.privKey )

def test_coinKeys_newPairWithPassword():
    pair = coinKeys.generateNewKeyPair( coinId = 1, password="asd" )
    print( pair.pubKey )
    print( pair.privKey )


#test_initTables()
#test_coinKeysSignature()
#test_coinKeys_newPairWithoutCoinId()
test_coinKeys_newPairWithCoinId()
#test_coinKeys_newPairWithPassword()
