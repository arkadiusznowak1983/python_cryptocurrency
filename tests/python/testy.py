# from coin_pkg import *
from coin_pkg import *


# coin unique id
coinId = 1

print( coinConfig.db_file )

#  keys
aaa = Keys()
sss = coinKeys.getPubRegisterCoinPubKey(coinId = coinId)
keysPair = Keys(pubKey = coinKeys.getPubRegisterCoinPubKey(coinId = coinId)
                , privKey = coinKeys.getWalletCoinPrivKey(coinId = coinId))

# coin
coin = Coin( coinId = coinId
            ,keys = keysPair )

# transfer
transfer = Transfer( coin = coin )
transfer.coinTransferRequest();
print( transfer )