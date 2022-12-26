import block
from block import Block
from Crypto.Hash import SHA256
from datetime import datetime
import json

class Blockchain:

    def __init__(self):
        self.blockchain = [block.genesis(),]
        self.difficulty = 3;

    def get(self):
        return self.blockchain

    def latestBlock(self):
        return self.blockchain[len(self.blockchain) - 1]

    def isValidHashDifficulty(self, hash):
        for i in range(len(hash)):
            if hash[i] != "0":
                break
            return i >= self.difficulty

    def calculateHashForBlock(self, block):
        return self.calculateHash(block.index, block.previousHash, block.timestamp, block.data, block.nonce)

    def calculateHash(self, index, previousHash, timestamp, data, nonce):
        hash = SHA256.new()
        hash.update(index + previousHash + timestamp + data + nonce)
        return hash.hexdigest()
    
    def mine(self, data):
        newBlock = self.generateNextBlock(data)
        try:
            self.addBlock(newBlock)
        except:
            print("Something went wrong")

    def generateNextBlock(self, data):
        nextIndex = self.latestBlock.index + 1
        previousHash = self.latestBlock.hash
        timestamp = datetime.timestamp(datetime.now())
        nonce = 0
        nextHash = self.calculateHash(nextIndex, previousHash, timestamp, data, nonce)

        while not self.isValidHashDifficulty(nextHash):
            nonce += 1;
            timestamp = datetime.timestamp(datetime.now())
            nextHash = self.calculateHash(nextIndex, previousHash, timestamp, data, nonce)

        nextBlock = Block(nextIndex, previousHash, timestamp, data, nonce)

    def addBlock(self,newBlock):
        if self.isValidNextBlock(newBlock, self.latestBlock):
            self.blockchain.append(newBlock)
        else:
            raise Exception("Error: Invalid block") 

    def isValidNextBlock(self, nextBlock, previousBlock):
        nextBlockHash = self.calculateHashForBlock(nextBlock)

        if previousBlock.index + 1 != nextBlock.index:
            return False
        elif previousBlock.hash != nextBlock.previousHash:
            return False
        elif nextBlockHash != nextBlock.hash:
            return False
        elif not self.isValidHashDifficulty(nextBlockHash):
            return False
        else:
            return True

    def isValidChain(self, chain):
        if json.dumps(chain[0] != json.dumps(Block.genesis)):
            return False

        tempChain = [chain[0],]
        for i in range(len(chain)):
            if self.isValidNextBlock(chain[i], tempChain[i - 1]):
                tempChain.append(chain[i])
            else:
                return False
        return True

    def isChainLonger(self, chain):
        return len(chain) > len(self.blockchain)

    def replaceChain(self, newChain):
        if self.isValidChain(newChain) and self.isChainLonger(newChain):
            self.blockchain = json.loads(json.dumps(newChain))
        else:
            raise Exception("Error: invalid chain")