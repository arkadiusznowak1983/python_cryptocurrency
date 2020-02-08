from coin_pkg import *

def testTransakcjiLokalnie( coinId = 1 ):
    myWallet = Wallet()
    myWallet.loadCoins()
    transaction = Transfer( coin = myWallet.getCoins()[ coinId ] )
    transaction.setPublicRegister( publicRegister = PublicRegister() )
    transaction.setWallet( wallet = myWallet )
    transaction.coinTransferRequest()

testTransakcjiLokalnie(2)