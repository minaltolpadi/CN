from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
from collections import defaultdict

from datetime import datetime
import time
import threading


#thr[srcip][dstip]
byte=defaultdict(lambda:None)
clock=defaultdict(lambda:None)
global thr
thr=defaultdict(lambda:None)

route1 = (match(switch=1, dstip='10.0.0.1') >> fwd(1))\
       + (match(switch=1, dstip='10.0.0.2') >> fwd(2))\
       + (match(switch=1, dstip='10.0.0.3') >> fwd(3))\
       + (match(switch=1, dstip='10.0.0.4') >> fwd(4))

route2 = (match(switch=2, dstip='10.0.0.1') >> fwd(3))\
       + (match(switch=2, dstip='10.0.0.2') >> fwd(4))\
       + (match(switch=2, dstip='10.0.0.3') >> fwd(1))\
       + (match(switch=2, dstip='10.0.0.4') >> fwd(2))

alter1 = (match(switch=1, dstip='10.0.0.1') >> fwd(1))\
       + (match(switch=1, dstip='10.0.0.2') >> fwd(2))\
       + (match(switch=1, dstip='10.0.0.3') >> fwd(4))\
       + (match(switch=1, dstip='10.0.0.4') >> fwd(4))

alter2 = (match(switch=2, dstip='10.0.0.1') >> fwd(4))\
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

retpolicy = route1 + route2 + route3 + route4
altpolicy = alter1 + alter2 + route3 + route4

class pathswitch(DynamicPolicy):
  def __init__(self):
    super(pathswitch,self).__init__()
    self.set_initial_state()
    self.thread = threading.Timer(1.0, self.byte_counts)
    self.thread.start()

  def pathchanger(self, n):
    if len(n)!=0:
      #print time.time()
      for i, j in n.items():
        if byte[str(i).split(" ")[2][0]]>0:
          thr[str(i).split(" ")[2][0]] = (j - byte[str(i).split(" ")[2][0]]) * 8.0 / (time.time()-clock[str(i).split(" ")[2][0]])
          print "switch ", str(i).split(" ")[2][0], " =", thr[str(i).split(" ")[2][0]], "bps"
        byte[str(i).split(" ")[2][0]]=j
        clock[str(i).split(" ")[2][0]]=time.time()
        print " ----------------------------------------------------"
    print thr[3]
    #print time.time(), " pathchanger called"
    if thr[3] >= 10:
       self.forward = altpolicy
       print "Changing to Alternate Policy"
    else:
       if self.forward == retpolicy:
           self.forward = retpolicy
           print "Continuing to use Default Policy"
       if self.forward == altpolicy:
           self.forward = altpolicy
           print "Continuing to use Alternate Policy"
    self.update_policy()
    self.thread = threading.Timer(1.0, self.byte_counts)
    self.thread.start()

  def set_initial_state(self):
    self.forward = retpolicy
    self.update_policy()

  def set_network(self,network):
    self.set_initial_state()

  def update_policy(self):
    self.policy = self.forward

  def byte_counts(self):
    q = count_bytes(1,['switch'])
    q.register_callback(self.pathchanger)
    return q

def main():
  return pathswitch()
