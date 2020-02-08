@echo Test transakcji na coinId: 1

curl -i http://127.0.0.1:5002/transaction/coin/1 --header "Content-Type: application/json" --request POST --data "{\"publicKey\":\"-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDR/mYG8i7hvR2dW9az8+qhLFGF
rnbEzFyWNrpoJttZCUn5J8Ld8QwymCgbbC3LdjB6lyr6pwxmyrhdIwTWbi9cr4Yd
mBLKjX5qwQfrmOnjAqSHzepsSPsbpjObaoEZdjmXo3mM7L213XFWe2GcLg2lD4Ij
ya5dc8Mq9OV3XKNt8wIDAQAB
-----END PUBLIC KEY-----\", \"sign\":\"78d04e67527806b2af67a675a3a14dc7a4fc2db9999bdd26921e2f4ad70ba7aa52b91bda3bc90e5119308e697365343be9b2a46446660c44ec27f8cc417419b5584ef3d748a8f7b885b0d54d08fc4205ada07e4f858893d7591758215db218fb74e5b0a4080686978085b6e78688d04f4e7f59b0195fe3cf893e1b5f4dcda59e\"}"
