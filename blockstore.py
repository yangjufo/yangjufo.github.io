import rpyc
import sys
import logging

"""
The BlockStore service is an in-memory data store that stores blocks of data,
indexed by the hash value.  Thus it is a key-value store. It supports basic
get() and put() operations. It does not need to support deleting blocks of
data–we just let unused blocks remain in the store. The BlockStore service only knows about blocks–it doesn’t know anything about how blocks relate to files.
"""
class BlockStore(rpyc.Service):


    """
    Initialize any datastructures you may need.
    """
    def __init__(self):
        self.hash_blocks = {}        
        self.logger = logging.getLogger('blockstore')
        hdlr = logging.FileHandler('blockstore.log')
        formatter = logging.Formatter('%(asctime)s %levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.WARNING)


    """
    store_block(h, b) : Stores block b in the key-value store, indexed by
    hash value h
    
    As per rpyc syntax, adding the prefix 'exposed_' will expose this
    method as an RPC call
    """
    def exposed_store_block(self, h, block):        
        self.logger.info("store block: " + str(h))
        self.hash_blocks[h] = block
        return True
        


    """
    b = get_block(h) : Retrieves a block indexed by hash value h
    
    As per rpyc syntax, adding the prefix 'exposed_' will expose this
    method as an RPC call
    """
    def exposed_get_block(self, h):
        self.logger.info("get block: " + str(h))
        return self.hash_blocks[h]

    """
    rue/False = has_block(h) : Signals whether block indexed by h exists
    in the BlockStore service

    As per rpyc syntax, adding the prefix 'exposed_' will expose this
    method as an RPC call
    """
    def exposed_has_block(self, h):
        self.logger.info("has block: " + str(h))
        return h in self.hash_blocks
		
if __name__ == '__main__':
    from rpyc.utils.server import ThreadPoolServer
    port = int(sys.argv[1])
    server = ThreadPoolServer(BlockStore(), port=port)
    server.start()
