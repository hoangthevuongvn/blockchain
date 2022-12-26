class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce
    
    @staticmethod
    def genesis():
        return Block(
             0,
            "0",
            1508270000000,
            "Welcome to Blockchain Demo 2.0!",
            "000dc75a315c77a1f9c98fb6247d03dd18ac52632d7dc6a9920261d8109b37cf",
            604
        )
