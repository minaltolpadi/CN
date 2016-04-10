from mininet.topo import Topo

class MyTopo(Topo):
	"Project topology."

	def __init__(self):
		"Create topology for the project."

		#Initialize topology
		Topo.__init__(self)

		#Add hosts and switches
		leftHost = self.addHost('h1')
		rightHost = self.addHost('h2')
		upperSwitch = self.addSwitch('s3')
		lowerSwitch = self.addSwitch('s4')

		#Add links
		self.addLink(leftHost,upperSwitch,bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
		self.addLink(leftHost,lowerSwitch,bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
		self.addLink(rightHost,upperSwitch,bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
		self.addLink(rightHost,lowerSwitch,bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)

def simpleTest():
   "Create and test a simple network"
   topo = LinearTopo()
   net = Mininet(topo)
   net.start()
   print "Dumping host connections"
   dumpNodeConnections(net.hosts)
   print "Testing network connectivity"
   net.pingAll()
   print "Testing bandwidth between h1 and h2"
   h1, h4 = net.get('h1', 'h2')
   net.iperf((h1, h2))
   net.stop()

if __name__ == '__main__':
   # Tell mininet to print useful information
   setLogLevel('info')
   simpleTest()
