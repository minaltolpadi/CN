from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
 
import threading

ip1 = IPAddr('10.0.0.1')
ip2 = IPAddr('10.0.0.2')
ip3 = IPAddr('10.0.0.3')
ip4 = IPAddr('10.0.0.4')

# h1 - s1 - s3 - s2 - h3
path1= (match(switch=1) >> fwd(3))\
	 + (match(switch=3) >> fwd(2))\
	 + (match(switch=2) >> fwd(1))

# h1 - s1 - s4 - s2 - h3
path2= (match(switch=1) >> fwd(4))\
	 + (match(switch=4) >> fwd(2))\
	 + (match(switch=2) >> fwd(1))

# h2 - s1 - s3 - s2 - h4
path2= (match(switch=1) >> fwd(3))\
	 + (match(switch=3) >> fwd(2))\
	 + (match(switch=2) >> fwd(2))

# h2 - s1 - s4 - s2 - h4
path2= (match(switch=1) >> fwd(4))\
	 + (match(switch=4) >> fwd(2))\
	 + (match(switch=2) >> fwd(2))

class myroute(DynamicPolicy):
	

def byte_counts():

def main():
  return (myroute()  + byte_counts())

 def set_initial_state(self):
    self.query = packets(1,['srcip', 'dstip'])
    self.query.register_callback(self.myroute)
    self.forward = self.flood
    self.update_policy()
 
  def set_network(self,network):
    self.set_initial_state()
 
  def update_policy(self):
    self.policy = self.forward + self.query
 
