from mininet.topo import Topo


class MyTopo( Topo ):

        def __init__( self ):
                "Create custom Topo"

                #Initialize topology
                Topo.__init__( self )

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
                self.addLink( h1, s1, port1=1, port2=1 )
                self.addLink( h2, s1, port1=1, port2=2 )
                self.addLink( s1, s3, port1=3, port2=1 )
                self.addLink( s1, s4, port1=4, port2=1 )
                self.addLink( s2, s3, port1=3, port2=2 )
                self.addLink( s2, s4, port1=4, port2=2 )
                self.addLink( h3, s2, port1=1, port2=1 )
                self.addLink( h4, s2, port1=1, port2=2 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
