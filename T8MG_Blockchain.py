# T8MG.io Blockchain: I am using this to songwriters to safely store digital files (leak proof)
# Louis     = dict[Python Programmer, Music Publisher, Freelancer]
# Github    = lc-iv
# email     = louismcoinley@gmail.com
# wechat    = k_louis_iv


import hashlib
import json

# Looking for ways for blocks to self create in an optimizing manner
block_genesis   = {
                   'prev_hash': None,
                   'data_list': [4, 2, 11, 3]
                  }


block_2         = {
                   'prev_hash': None,
                   'data_list': [12, 5, 6, 24, 15, 1]
                  }


block_3         = {
                   'prev_hash': None,
                   'data_list': [7, 6, 2, 14, 8]
                  }


def hash_blocks(blocks):
    prev_hash   = None
    for block in blocks:
        block['prev_hash']  = prev_hash
        block_serialized    = json.dumps(block, sort_keys=True).encode('utf-8')
        block_hash          = hashlib.sha256(block_serialized).hexdigest()
        prev_hash           = block_hash
    return prev_hash


print('Original_Hash')
print(hash_blocks([block_genesis, block_2, block_3]))


print('Updating Blocks')

NewData_List = ['newdata_1', 'newdata_2', 'newdata_3', 'newdata_4']

block_2['data_list'].append(NewData_List)
block_3['data_list'].append(NewData_List[:2])

print('After being tampered')
print(hash_blocks([block_genesis, block_2, block_3]))


