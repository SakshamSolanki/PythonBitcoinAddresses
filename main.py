from PrivateKey import PrivateKey
import random 


if __name__ == '__main__':
    random_seed = input("Enter a random number (at least 10 digits):")
    num_addresses = input("Enter number of address to be generated:")
    random.seed(int(random_seed))
    for i in range(int(num_addresses)):
        private_key = random.randint(0 , 2**256)
        priv = PrivateKey(private_key)
        print("Address: {}\nPrivate Key: {}".format(priv.point.address(compressed = True , testnet = True) , private_key))
