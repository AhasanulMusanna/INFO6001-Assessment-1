import hashlib
import datetime
import json


class block:
    def __init__(self, index, previous_hash, timestamp, data, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()


class blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        genesis_block: block = block()


    def get_latest_block(self):
        latest_block = self.chain[-1]


    def add_block(self, new_block):
        self.chain.append(block)


    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256()
            str_operation = str(new_proof).encode().hexdigest()


    def add_data(self, data):
        new_block = blockchain.add_block(self, data)

    def is_chain_valid(self, block):
        previous_block = self.chain[-1]
        block_index = 1



if __name__ == "__main__":
            Blockchain = blockchain()

            print("Mining block 1...")
            blockchain.add_data("Transaction data for Block 1")

            print("Mining block 2...")
            blockchain.add_data("Transaction data for Block 2")

            print("\nBlockchain validity:", blockchain.is_chain_valid())

            for block in blockchain.chain:
                print(f"Block {block.index} | Hash: {block.hash} | Previous Hash: {block.previous_hash}")
