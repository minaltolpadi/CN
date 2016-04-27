from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
from mininet.node import RemoteController
from mininet.cli import CLI

#Run it as sudo python case3_topology.py

class MyTopo( Topo ):

        def __init__( self ):
                "Create custom Topo"

                #Initialize topology
                Topo.__init__( self )

                slowlinkConfig = {'bw': 1, 'delay': '1ms', 'loss': 0}
                linkConfig = {'bw': 100, 'delay': '1ms', 'loss': 0}

                #Add hosts and switches
                h1 = self.addHost( 'h1' )
                h2 = self.addHost( 'h2' )
                h3 = self.addHost( 'h3' )
                h4 = self.addHost( 'h4' )

                s1 = self.addSwitch( 's1' )
                s2 = self.addSwitch( 's2' )
                s3 = self.addSwitch( 's3' )
                s4 = self.addSwitch( 's4' )

                #Adding Links
                self.addLink( h1, s1, port1=1, port2=1, **linkConfig )
                self.addLink( h2, s1, port1=1, port2=2, **linkConfig )
                self.addLink( s1, s3, port1=3, port2=1, **slowlinkConfig )
                self.addLink( s1, s4, port1=4, port2=1, **linkConfig )
                self.addLink( s2, s3, port1=3, port2=2, **slowlinkConfig )
                self.addLink( s2, s4, port1=4, port2=2, **linkConfig )
                self.addLink( h3, s2, port1=1, port2=1, **linkConfig )
                self.addLink( h4, s2, port1=1, port2=2, **linkConfig )

if __name__ == '__main__':
    topo = MyTopo()
    net = Mininet(topo=topo, link=TCLink, controller=RemoteController)
    net.start()
    CLI(net)
    net.stop()