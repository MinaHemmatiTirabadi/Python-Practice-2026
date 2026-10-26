#Perform the proof-of-work process with 7 zeros.
#Determine the mining duration and the nonce value.

import hashlib
import json
class block:
    id=None
    history=None
    parent_id=None
    parent_hash=None
block_A=block()
block_A.id=1
block_A.history="Data for A"
block_B=block()
block_B.id=2
block_B.history="Data for B"
block_B.parent_id=block_A.id
block_B.parent_hash=hashlib.sha256(json.dumps(block_A.__dict__).encode("utf-8")).hexdigest()
block_C=block()
block_C.id=3
block_C.history="Data for C"
block_C.parent_id=block_B.id
block_C.parent_hash=hashlib.sha256(json.dumps(block_B.__dict__).encode("utf-8")).hexdigest()
block_D=block()
block_D.id=4
block_D.history="Data for D"
block_D.parent_id=block_C.id
block_serialized=json.dumps(block_D.__dict__).encode("utf-8")
payload=b'{"history":"Data for D","parent_id":3,"id":4}'
for i in range(1000000):
    nonce=str(i).encode("utf-8")
    result=hashlib.sha256(payload+nonce).hexdigest()
    if result[0:7]=="0000000":
        print(i)
        print(result)
        break
