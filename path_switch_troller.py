from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *

def staticpolicy():

	route1 = ((match(switch=1, dstip='10.0.0.1') >> fwd(1)\
			+ (match(switch=1, dstip='10.0.0.2') >> fwd(2)\
			+ (match(switch=1, dstip='10.0.0.4') >> fwd(4))

	route2 = ((match(switch=2, dstip='10.0.0.2') >> fwd(4)\
			+ (match(switch=2, dstip='10.0.0.3') >> fwd(1)\
			+ (match(switch=2, dstip='10.0.0.4') >> fwd(2))

	route3 = ((match(switch=3, dstip='10.0.0.1') >> fwd(1)\
			+ (match(switch=3, dstip='10.0.0.2') >> fwd(1)\
			+ (match(switch=3, dstip='10.0.0.3') >> fwd(2)\
			+ (match(switch=3, dstip='10.0.0.4') >> fwd(2))

	route4 = ((match(switch=4, dstip='10.0.0.1') >> fwd(1)\
			+ (match(switch=4, dstip='10.0.0.2') >> fwd(1)\
			+ (match(switch=4, dstip='10.0.0.3') >> fwd(2)\
			+ (match(switch=4, dstip='10.0.0.4') >> fwd(2))

	static_policy = route1 + route2 + route3 + route4
	return static_policy

def switcheroo(byte_count):
	if byte_count > 50000:
		print "Routing along Switch 4"
		swapp1 = (match(switch=1, dstip='10.0.0.3') >> fwd(4)\
				+ match(switch=2, dstip='10.0.0.1') >> fwd(4))		
		return swapp1
	else:
		print "Routing along Switch 3"
		swapp2 = (match(switch=1, dstip='10.0.0.3') >> fwd(3)\
				+ match(switch=2, dstip='10.0.0.1') >> fwd(3))		
		return swapp2
	
	
def switchpolicy():
	Q = count_bytes(interval=1, group_by=['srcip'])
	Q.register_callback(switcheroo)
	
def switchchecker():
    return (match(switch=3, srcip='10.0.0.1') | match(switch=3, srcip='10.0.0.3')) >> switchpolicy()
	
def main():
	print "Initializing controller"
	
    return staticpolicy() + switchchecker()