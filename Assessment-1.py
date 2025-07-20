import hashlib
import datetime


class Block:
    def __init__(self, index, previous_hash, timestamp, data, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.proof = proof
        self.hash = self.calculate_hash()


    def calculate_hash(self):
        new_block_chain = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.proof}"
        return hashlib.sha256(new_block_chain.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4


    def create_genesis_block(self):
        return Block(index=0, previous_hash="0", timestamp=str(datetime.time()), data="Genesis Block", proof=1)

    def get_latest_block(self):
        return self.chain[-1]


    def add_block(self, new_block):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.time(), previous_block.hash)
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
        proof = self.proof_of_work


    def is_chain_valid(self, block):
        previous_block = self.chain[-1]
        block_index = 1


if __name__ == "__main__":
   blockchain = Blockchain()

   while True:
        question = input("1. Add a new transaction\n2. Display Blockchain\n3. Validate Blockchain\n4. Exit")
        if question == "1":
            print("Mining block 1...")
            blockchain.add_data(data)
        elif question == "2":
            print("Mining block 2...")
            blockchain.add_data("Transaction data for Block 2")
        elif question == "3":
            print("\nBlockchain validity:", blockchain.is_chain_valid())
        elif question == "4":
            print("Exiting...")
            break