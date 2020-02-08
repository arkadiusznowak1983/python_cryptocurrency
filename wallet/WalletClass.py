from coin_pkg import *

class Wallet:
    # all private coins dictionary
    coins = {  }

    sqliteConnection = None

    def setCoins( self, coins = {} ):
        self.coins = coins
    def addCoin( self, coin ):
        coinId = coin.getCoinId()
        if coin is None or coinId is None:
            return
        if coin is not None:
            self.coins[ 0 if coinId is None else coinId ] = coin
    def getCoins( self ):
        return self.coins

    def getPubRegisterCoinPubKey( self, coinId ):
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

    def addCoinToWallet( self, coinId, privateKey ):
        import sqlite3
        if self.sqliteConnection is None:
            flagCloseConnection = True
            self.sqliteConnection = sqlite3.connect(coinConfig.db_file)
        else:
            flagCloseConnection = False
        cursor = self.sqliteConnection.cursor()
        cursor.execute("DELETE FROM main_wallet WHERE coinId=?", (coinId,) )
        cursor.execute( "INSERT INTO main_wallet VALUES(?, ?)", (coinId, privateKey) )
        self.sqliteConnection.commit()

    def loadCoins( self ):
        import sqlite3
        self.coins = {}
        if self.sqliteConnection is None:
            flagCloseConnection = True
            self.sqliteConnection = sqlite3.connect(coinConfig.db_file)
        else:
            flagCloseConnection = False
        cursor = self.sqliteConnection.cursor()
        cursor.execute( "SELECT * FROM main_wallet" )
        for row in cursor.fetchall():
            rowCoinId = row[ 0 ]
            keys = Keys( pubKey = self.getPubRegisterCoinPubKey( coinId = rowCoinId )
                        ,privKey = row[ 1 ] )
            self.addCoin( coin = Coin( coinId = rowCoinId
                                      ,keys = keys ) )
        cursor.close()
        if ( self.sqliteConnection ):
            self.sqliteConnection.close()
            self.sqliteConnection = None

    def __init__( self, coins = None ):
        self.setCoins( coins = {} if coins is None else coins )