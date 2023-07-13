from tronpy import Tron
from tronpy.keys import PrivateKey
import random

# Initialize Tron client
client = Tron(network='shasta')

# Source address and private key
source_private_key = PrivateKey(bytes.fromhex("c3471fdd3cf6e1a361f00d49a497706f1b2d12114c249dfa83319eb45c9722ad"))
source_address = source_private_key.public_key.to_hex_address()

# Generate new intermediate addresses and private keys
num_intermediate_addresses = 5
intermediate_keys = [PrivateKey.random() for _ in range(num_intermediate_addresses)]

# Destination addresses
destination_addresses = ["TUKLHxMbXZnk4GUBLczRuWxjrzQRfaQHj3", "TUKLHxMbXZnk4GUBLczRuWxjrzQRfaQHj3"]

# Distribute TRX from source address to intermediate addresses
source_balance = client.get_account_balance(source_address)
amount_per_address = (source_balance / num_intermediate_addresses) * 1_000_000

for key in intermediate_keys:
    txn = (
        client.trx.transfer(source_address, key.public_key.to_hex_address(), int(amount_per_address) - 1_000_000)
        .memo("s")
        .build()
        .inspect()
        .sign(source_private_key)
        .broadcast()
    )

# Send TRX from intermediate addresses to destination addresses
amount_per_destination = ((source_balance / len(destination_addresses)) - 1) * 1_000_000
for dest_address in destination_addresses:
    # Choose a random intermediate address
    random_key = random.choice(intermediate_keys)
    intermediate_address = random_key.public_key.to_hex_address()

    txn = (
        client.trx.transfer(intermediate_address, dest_address, int(amount_per_destination) - 1_000_000)
        .memo("s")
        .build()
        .inspect()
        .sign(random_key)
        .broadcast()
    )
