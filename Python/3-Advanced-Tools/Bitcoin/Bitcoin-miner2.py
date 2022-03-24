from hashlib import sha256
import time


def apply_sha256(input_string):
    return sha256(input_string.encode("ascii")).hexdigest()


def mine(block_number, trans, prev_hash, amount_0):
    nonce = 0
    while True:
        text = str(block_number) + trans + prev_hash + str(nonce)
        local_hash = apply_sha256(text)
        if str(local_hash).startswith("0" * amount_0):
            return nonce, local_hash
        nonce += 1


if __name__ == "__main__":
    block_number = 12294029
    trans = ""  # transaction
    amount_0 = 6  # number of zeros
    prev_hash = ""  # previous hash
    start = time.time()
    result = mine(block_number, trans, prev_hash, amount_0)
    print(result)
    print(f'{time.time() - start:.2f}')
