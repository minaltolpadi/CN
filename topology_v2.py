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
		self.addLink(leftHost,upperSwitch)
		self.addLink(leftHost,lowerSwitch)
		self.addLink(rightHost,upperSwitch)
		self.addLink(rightHost,lowerSwitch)

def simpleTest():
   "Create and test a simple network"
   topo = LinearTopo()
   net = Mininet(topo)
   net.start()
   print "Dumping host connections"
   dumpNodeConnections(net.hosts)
   print "Testing network connectivity"
   net.pingAll()
   net.stop()

if __name__ == '__main__':
   # Tell mininet to print useful information
   setLogLevel('info')
   simpleTest()
