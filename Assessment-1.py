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
        new_block_chain = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.proof)
        return hashlib.sha256(new_block_chain).hexdigest()


class blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block("Genesis Block", "0")


    def get_latest_block(self):
        return self.chain[-1]


    def add_block(self, new_block):
        self.chain.append(new_block)


    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:self.difficulty] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof


    def add_data(self, data):
        new_block = blockchain.add_block(self, data)
        proof = self.proof_of_work(new_block)

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
