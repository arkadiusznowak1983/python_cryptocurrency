

class Wallet:
    # all private coins dictionary
    coins = {}

    def setCoins( self, coins = {} ):
        self.coins = coins
    def addCoin(self, coin ):
        if coincoin.getCoinId() is None:
            return
        self.coins[ coin.getCoinId() ] = coin

    def __init__( self, coins = None ):
        self.setCoin( coin )