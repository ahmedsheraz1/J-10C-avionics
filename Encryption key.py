Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from hashlib import blake2b
FANOUT = 2
DEPTH = 2
LEAF_SIZE = 4096
INNER_SIZE = 64
buf = bytearray(6000)
# Left leaf
h00 = blake2b(buf[0:LEAF_SIZE], fanout=FANOUT, depth=DEPTH,
              leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
              node_offset=0, node_depth=0, last_node=False)
# Right leaf
h01 = blake2b(buf[LEAF_SIZE:], fanout=FANOUT, depth=DEPTH,
              leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
              node_offset=1, node_depth=0, last_node=True)
# Root node
h10 = blake2b(digest_size=32, fanout=FANOUT, depth=DEPTH,
              leaf_size=LEAF_SIZE, inner_size=INNER_SIZE,
              node_offset=0, node_depth=1, last_node=True)
h10.update(h00.digest())
h10.update(h01.digest())
h10.hexdigest()
'3ad2a9b37c6070e374c7a8c508fe20ca86b6ed54e286e93a0318e95e881db5aa'
