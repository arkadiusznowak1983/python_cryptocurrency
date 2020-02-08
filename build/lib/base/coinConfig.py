# keys
########################################################################################################################
keyLength = 1024

# database
########################################################################################################################
db_file = 'SQLite_coin.db'

createTablePubReg = """ CREATE TABLE IF NOT EXISTS pub_register( coinId integer PRIMARY KEY
                                                                ,pubKey text NOT NULL );"""

createTableMainWallet = """ CREATE TABLE IF NOT EXISTS main_wallet( coinId integer PRIMARY KEY
                                                                   ,privKey text NOT NULL );"""

createTableTransactions = """ CREATE TABLE IF NOT EXISTS transactions( coinId integer PRIMARY KEY
                                                                      ,coinTransactionId number NOT NULL
                                                                      ,pubKey text NOT NULL 
                                                                      ,sign text NOT NULL );"""

initialMainWallet = [ ( 1, 'MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIhthbbayO9cXNOcppsJLYJfbjCgPQmwmAyVRiJzPoiHh5kGpkWuCMigfTJxfgpl9gJiWD09YQ23tJfDB4g/trUAxLnGuhHesuvQM9L5slP1nZ6z/oihxZAh0wjCB3z+CwvQl9WbhG5pphmFjgwDMDM3WNGoK4csDUkRYk27VpFrAgMBAAECgYBi9ic/e7azwmjna0ODRIYJgxXYGfQMulehEQr95GDhAoa+3w7vjo16ksgeNis6ebmZAyOE0Kg9HhvW1jb5g1YRKBc9PBR2+LOz0Eb7PnAfumHWXRJ6zii1txBg+dLln9ZkHU1GoEkKuNXvcRtwFunExWhGB8w3z+1KpBgqX2VzeQJBAMob5b5/Ozy7wbAqZn0hyP/dk/HX6jLEukXeQmdbx+ngLBfRT5hn/GIIiG9RM+dilLzXyUkvBi0TrpeKhLwSh2cCQQCszi6/PLDKgCLOlWfIfeuf0r7k7wpYu7lsBZ56DjVTQjfnVoJoEmWaCXMLHkGKaFVTuHxQ85lfk7AxGOdw8fddAkEAq9QIAWteS4Y9Z67Er8IXhyE09LnizQLgcyJBRmqLjlUeZ6l2iFZwBlDG3g0lmaUAW4UCBoxKLey71O7ZZqRCJQJBAJU8QtbY/P0FCApMsSJOzOxrvnxLjC3xgUKu35wdJSRQLaNV7K0gJiqPOpFBgeycCgSRcJsgpTYLf8AG9+lsrekCQDyUs7KgJ9mdbwosBD9hjA1ywHocVEnKdHZ+YZ90agAM0ovomWBJVgEzaWoV6tWOgw8jBLz2CvI3pTpAnyciqC8=' )
                     ,( 2, 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAJgQTqM4961tVL31xBybJo/qzu8r8rc3Pz6tIpFJm1Njxdam/2c1H9v3gJdjwxw4948G4VlSdBTWGMBMxoyt24qv9qLby4YG4XXK9Nd8GZd3vWe7WPCY2WJOmwaRkuqTD1Io889PotQQKfSzyA6Hyyb/hgjiC2d1+UGxfPtbaUKxAgMBAAECgYBnVL17INz9Vov9QaJwJeYAafkQgXa/laU+e/w/ahtIgUYQ5Q4tHeZ2XStetIYDCZr/8Bb10ZfcCNhs5D8PnZzPByv6rXgGgIUFJvP8ALNKl8Rz1w4nqWhiKVJtNDgL8aDcmtJDtFeisom4ZyEEWC0IXbk+7L6UzuN4JcG+AQL8eQJBAMlPJVwkrLE6cWsgjOSlgXHbeBYX9Me/0uJhEIQnQC/2Ez/GXdsGMLsgmsYYBCMT4rTj5VFSBO0sH+kfAvHopesCQQDBYDAPI8MhjS+CtzLqay4XXP0uHLfxJxsiTGM2Df/7n1rfew4nZDSgz0xhXFLc068O68iu02G+gFyU+hNkDwbTAkAfrzhXH2Ka5nLxhIcIedA85mkpOQ4K3nNHtDVQR4k/w0BWWldtYLUMzt3tbdxA1SFqjTALs5gY6EgBfiMNhiuPAkEAk/BclBiN/isfP+eb4k9hEaqoXxDFgI6kaZb7B62qOvxs7zAbYfN9d9Ff49RX6G1iLg4gl+9Lhgx5x9eR4ijE1QJAc3suEK74bgjM5+f/M65XabC3GkS6H9iAC56z97PmgbLDk5ExgEZifV3tXcAUrcin1H3qFbjfBd6mv+FqWypRRw==' )
                     ,( 3, 'MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAI14kxhQPV5i04o6tW4MiQDMIneRzgbQY4+oXFY/9sryP/1OCfwb6YDjjjBIhwa0kXBEoVqpjhWYQkBnYynAQhkrpLhTmJOdNGYknLlgIuB0nXkmzXkluSNf6BbqPCYw44CXe45mNg1OKDzTszdc61XgrVcDHNFkgdBw/4XiSQyZAgMBAAECgYA4WfP1tliLlUAACpykRlf4OlfsWua/LhjKa1zEelwawN4eTwyJILElRv8nWmx2jkx0dNH05B8VmP2i28vTIKLy/IMrzH6QBUpmOxBVc4r6sRK3MXCNGjVGUR/h6Iq+IPqQYXSkm0jzjMrmsbhblzoH1UtoDahSzT303VV6C49dlQJBANxUKEjoXTV3UpJHlNjlDewNSTLT51rQtqCnEIU667rNaFLghSFUDxy/yqf8Atpgk8N0NNe8wvXm3Ny9aUoaPj8CQQCkYAtNtmo+fPTDwwomXkAXetr/UtVNoqVixDd44FSjP5y5kW9bIN1GYTk81l4Gbxzt7wMciMJE0mqRp/p6JC8nAkA1eW91kn/c1CMEQb9MjPs+CVN0tJ14GyPYBfQqgcxowCXLx5ZIKoCod5wV/UIsAjiavX99xOCEkg2UvZvqUkg9AkBj5W7ZMtRM17oVQvJnMP54hpSTeS7i+MbUSHWCA6vMbrt715Q6aLWxsSKNA6au+FY3j/tvGvodw1c64ECMfHMfAkAVxzRnnZJxjihdNq0Aq04QhWKoG05SvHQIkzIZbuaktD7B+jGPIhy85QkHII8DPxLRhYdFYIvCfTP9PZEjCPYK' ) ]


def __coinConfig__():
    print( "coinConfig: Loading Configuration" )

if __name__ == "coinConfig" or __name__ == "__main__":
    __coinConfig__()