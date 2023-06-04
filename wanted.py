import sha3
import os 
from ethereum import utils
import time

start = time.time()

a = 1
while (a <= 1000):

    elapsed_time = time.time() - start

    private_key = utils.sha3(os.urandom(256))
    raw_address = utils.privtoaddr(private_key)
    account_address = (utils.checksum_encode(raw_address)).lower()
    z=utils.encode_hex(private_key)
    #for testt
    #account_address = " <PUT THE ADDRESS HERE>"
    wanted = {"0xDA9dfA130Df4dE4673b89022EE50ff26f6EA73Cf"
              "0xbf60c77e1eb1a94ecec0b6926d8a8936f6e31ec3"
              "0xeb7df1cc45d9fe719fd1606ee0a2f4d57e71c681"
              "0x3879ea64dcfa8baac07dcd99d52ad9da2cab3970"
              "0xc17d043df0399347f206a397b13500fc22035a40"
              "0x29cdb04431926b47669a1a91732ee223eb140f6d"
              "0xe31d6af006fd02899162014417bb1d81850661fe"
              "0x34f091a2e41690b1f6435d21541d691779677e8a"
              "0x843d51149a65ba4d8c9ddc3e43f2a685648994da"
              "0x7117819eac6f3f1022145db8b771835e9ce2c53f"
              "0xb3a9defc561cac78ba098c575b5ed0420b445062"
              "0xf7571d58c0c0267cd966627879ccbbac76349ac4"
              "0xab24705d5977a484a8abc529bff3933b531267b0"
              "0xbe606fe66b0337c1dbdb9115a054cd7c46f60d4c"
              "0x1d044d5f1f3804cf36b9c169930270f7248cdb6c"
              "0x42f7bc2a19ee9dea55240b265d030ea21e641181"
              "0xf5f425655679950355f8b94da55c6a210f705b73"
              "0x6f6ccef7dcbce4d7bc7cf45becd1c90feecafbd6"
              "0xabdb624c38a812fd323c9c68ff95073d93ce24b1"
              "0xe754a3551361730c9efb2fa5803360f25e30d6c4"
              "0x7acdf5798647acc0d289ea751d0b19b477c8cde1"
              "0xde101e1ee99cf62b1489361d9179eaaa9c06ba2b"
              "0x4cb810486ab9cfaba76f797ebfdb8f25b9510688"
              "0x4bda629a6987fbe56120e8e9d3b49dfa6d5711ad"} #set your Target address

    if wanted == account_address:
        print("***finnally*****finally****finally*****finally****finally***")
        print("private_key       : " + z)
        print("Address           : " + account_address)

        dosya2 = open("eslesme.txt", "a")
        dosya2.write(z + " " + account_address + "\n")
        dosya2.close()

        time.sleep(5)
    else:
        print ('Private Key:', z + ' ' + 'Address: ' + account_address + '   '+ str(a))
    a = a + 1
print ("Total Time %s sn" %elapsed_time)