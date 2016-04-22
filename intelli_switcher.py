from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
 
import threading

CONGESTION_LIMIT = 500

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
path3= (match(switch=1) >> fwd(3))\
	 + (match(switch=3) >> fwd(2))\
	 + (match(switch=2) >> fwd(2))

# h2 - s1 - s4 - s2 - h4
path4= (match(switch=1) >> fwd(4))\
	 + (match(switch=4) >> fwd(2))\
	 + (match(switch=2) >> fwd(2))

<<<<<<< HEAD
myroute1 = path1 + path2
=======
class myroute(DynamicPolicy):
	
>>>>>>> 40b9e610d38ec211e7fafd772498a917bacdac2b

class myroute(DynamicPolicy):
  def __init__(self):
    super(myroute,self).__init__() 
    self.set_initial_state()
    #self.thread = threading.Timer(10.0, self.handle_function)
    self.byte_count = count_bytes(interval=1, group_by=['switch', 'srcip'])
    self.byte_count.register_callback(self.handle_function)
    #self.thread.start()
 
  def handle_function(self,count):
    print time.time(), " handle_function is called"
    # count >> match(switch=3, srcip=ip1))   and self.byte_count > CONGESTION_LIMIT :
    #    self.forward1 = myroute2
    #    print "change to myroute2"
    # else:
    #    self.forward = myroute1
    #    print "change to myroute1"
    # self.update_policy()
    # self.thread = threading.Timer(10.0, self.handle_function)
    # self.thread.start()
  
  def set_initial_state(self):
    #self.forward = myroute1
    #self.update_policy()
    self.route = myroute1
 
  def set_network(self,network):
    self.set_initial_state()
 
  def update_policy(self):
    self.policy = self.forward

def main():
  return (myroute()  + byte_counts())
