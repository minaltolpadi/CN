from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *

route1 = (match(switch=1, dstip='10.0.0.1') >> fwd(1))\
       + (match(switch=1, dstip='10.0.0.2') >> fwd(2))\
       + (match(switch=1, dstip='10.0.0.3') >> fwd(3))\
       + (match(switch=1, dstip='10.0.0.4') >> fwd(4))

route2 = (match(switch=2, dstip='10.0.0.1') >> fwd(3))\
       + (match(switch=2, dstip='10.0.0.2') >> fwd(4))\
       + (match(switch=2, dstip='10.0.0.3') >> fwd(1))\
       + (match(switch=2, dstip='10.0.0.4') >> fwd(2))

route3 = (match(switch=3, dstip='10.0.0.1') >> fwd(1))\
       + (match(switch=3, dstip='10.0.0.2') >> fwd(1))\
       + (match(switch=3, dstip='10.0.0.3') >> fwd(2))\
       + (match(switch=3, dstip='10.0.0.4') >> fwd(2))

route4 = (match(switch=4, dstip='10.0.0.1') >> fwd(1))\
       + (match(switch=4, dstip='10.0.0.2') >> fwd(1))\
       + (match(switch=4, dstip='10.0.0.3') >> fwd(2))\
       + (match(switch=4, dstip='10.0.0.4') >> fwd(2))

rtpolicy = route1 + route2 + route3 + route4

def main():
	print "Initializing controller"
	return rtpolicy
