#!/usr/bin/python
from containernet.net import Containernet
from containernet.node import DockerSta, Node
from containernet.cli import CLI
from containernet.term import makeTerm
from containernet.link import Link, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Controller, OVSKernelSwitch

import time
import glob, os

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


def ospftopo():

    net = Containernet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

#Define Routers
    router1 = net.addDocker(name='r1', ip='21.21.21.1/24',dimage="manash22/mc_project01:r1")      #r1-eth0
    router2 = net.addHost( 'r2', cls=LinuxRouter, ip='21.21.21.2/24')       #r2-eth0
    router3 = net.addDocker(name='r3', ip='43.43.43.2/24',dimage="manash22/mc_project01:r3")      #r3-eth0
    router4 = net.addHost('r4', cls=LinuxRouter, ip = '124.124.124.2/24')     #r4-eth0
    router5 = net.addDocker(name='r5', ip='65.65.65.2/24',dimage="manash22/mc_project01:r5")      #r5-eth0
    router6 = net.addHost('r6', cls=LinuxRouter, ip = '96.96.96.2/24')     #r6-eth0
    router7 = net.addHost('r7', cls=LinuxRouter, ip = '72.72.72.2/24')      #r7-eth0
    router8 = net.addHost('r8', cls=LinuxRouter, ip = '87.87.87.2/24')     #r8-eth0
    router9 = net.addHost('r9', cls=LinuxRouter, ip = '98.98.98.2/24')     #r9-eth0
    router10 = net.addHost('r10', cls=LinuxRouter, ip = '108.108.108.2/24')    #r10-eth0
    router11 = net.addHost('r11', cls=LinuxRouter, ip = '117.117.117.2/24')    #r11-eth0
    router12 = net.addHost('r12', cls=LinuxRouter, ip = '112.112.112.2/24')   #r12-eth0
    router13 = net.addHost('r13', cls=LinuxRouter, ip = '123.123.123.2/24')    #r13-eth0
    router14 = net.addDocker(name='r14', ip='148.148.148.2/24',dimage="manash22/mc_project01:r14")    #r14 eth0
    router15 = net.addDocker(name='r15', ip='200.200.200.2/24',dimage="manash22/mc_project01:r15")    #r15-eth0


#Define Router to Router Links
    net.addLink(router1,router2,intfName1='r1-eth0',intfName2='r2-eth0',params1={ 'ip' : '21.21.21.1/24' },params2={ 'ip' : '21.21.21.2/24' })
    net.addLink(router2,router7,intfName1='r2-eth1',intfName2='r7-eth0',params1={ 'ip' : '72.72.72.1/24' },params2={ 'ip' : '72.72.72.2/24' })
    net.addLink(router7,router8,intfName1='r7-eth1',intfName2='r8-eth0',params1={ 'ip' : '87.87.87.1/24' },params2={ 'ip' : '87.87.87.2/24' })
    net.addLink(router8,router14, intfName1='r8-eth1',intfName2='r14-eth0',params1={ 'ip' : '148.148.148.1/24'},params2={ 'ip' : '148.148.148.2/24'})
    net.addLink(router8,router9,intfName1='r8-eth2',intfName2='r9-eth0',params1={ 'ip' : '98.98.98.1/24' },params2={ 'ip' : '98.98.98.2/24' })
    net.addLink(router8,router10,intfName1='r8-eth3',intfName2='r10-eth0',params1={ 'ip' : '108.108.108.1/24' },params2={ 'ip' : '108.108.108.2/24' })
    net.addLink(router7,router10,intfName1='r7-eth2',intfName2='r10-eth1',params1={ 'ip' : '107.107.107.1/24' },params2={ 'ip' : '107.107.107.2/24' })
    net.addLink(router7,router11,intfName1='r7-eth3',intfName2='r11-eth0',params1={ 'ip' : '117.117.117.1/24' },params2={ 'ip' : '117.117.117.2/24' })
    net.addLink(router11,router10,intfName1='r11-eth1',intfName2='r10-eth2',params1={ 'ip' : '110.110.110.1/24' },params2={ 'ip' : '110.110.110.2/24' })
    net.addLink(router11,router12,intfName1='r11-eth2',intfName2='r12-eth0',params1={ 'ip' : '112.112.112.1/24' },params2={ 'ip' : '112.112.112.2/24'})
    net.addLink(router12,router4,intfName1='r12-eth1',intfName2='r4-eth0',params1={ 'ip' : '124.124.124.1/24' },params2={ 'ip' : '124.124.124.2/24'})
    net.addLink(router12,router13,intfName1='r12-eth2',intfName2='r13-eth0',params1={ 'ip' : '123.123.123.1/24' },params2={ 'ip' : '123.123.123.2/24'})
    net.addLink(router11,router13,intfName1='r11-eth3',intfName2='r13-eth1',params1={ 'ip' : '113.113.113.1/24' },params2={ 'ip' : '113.113.113.2/24'})
    net.addLink(router13,router9,intfName1='r13-eth2',intfName2='r9-eth1',params1={ 'ip' : '139.139.139.1/24' },params2={ 'ip' : '139.139.139.2/24' })
    net.addLink(router13,router10,intfName1='r13-eth3',intfName2='r10-eth3',params1={ 'ip' : '130.130.130.1/24' },params2={ 'ip' : '130.130.130.2/24'})
    net.addLink(router9,router10,intfName1='r9-eth2',intfName2='r10-eth4',params1={ 'ip' : '109.109.109.1/24' },params2={ 'ip' : '109.109.109.2/24'})
    net.addLink(router9,router6,intfName1='r9-eth3',intfName2='r6-eth0',params1={ 'ip' : '96.96.96.1/24' },params2={ 'ip' : '96.96.96.2/24'})
    net.addLink(router6,router5,intfName1='r6-eth1',intfName2='r5-eth0',params1={ 'ip' : '65.65.65.1/24' },params2={ 'ip' : '65.65.65.2/24'})
    net.addLink(router4,router3,intfName1='r4-eth1',intfName2='r3-eth0',params1={ 'ip' : '43.43.43.1/24' },params2={ 'ip' : '43.43.43.2/24'})
    net.addLink(router13,router15, intfName1='r13-eth4',intfName2='r15-eth0',params1={ 'ip' : '200.200.200.1/24'},params2={ 'ip' : '200.200.200.2/24'})

# Define switches
    s1,s2 = [net.addSwitch(s) for s in ('s1','s2')]

#Switch to router links
    net.addLink(s1,router1,intfName2='r1-eth1',params2={ 'ip' : '10.0.1.1/24' })
    net.addLink(s2,router3,intfName2='r3-eth1',params2={ 'ip' : '192.168.10.1/24' })

# Define AccessPoint
    ap1 = net.addAccessPoint("ap1", ssid="ssid_ap1")

#AP to router
    net.addLink(ap1,router5, params1={ "ip" : "192.168.20.10/24" }, params2={ "ip" : "192.168.20.1/24" })

# Define DHCP Servers
    dhcpsrv1=net.addDocker( name='dhcpsrv1', ip='10.0.1.150/24',defaultRoute='via 10.0.1.1',dimage="manash22/mc_project01:dhcpsrv1")
    dhcpsrv2=net.addDocker( name='dhcpsrv2', ip='192.168.10.160/24',defaultRoute='via 192.168.10.1',dimage="manash22/mc_project01:dhcpsrv2")
    dhcpsrv3=net.addDocker( name='dhcpsrv3', ip='192.168.20.170/24',defaultRoute='via 192.168.20.1',dimage="manash22/mc_project01:dhcpsrv3")

# Adding servers
    srv1=net.addDocker( name='srv1', ip='199.199.199.199/25',defaultRoute='via 199.199.199.129',dimage="aniklogu/voipservice:updated")
    srv2=net.addDocker( name='srv2', ip='199.199.199.199/24',defaultRoute='via 199.199.199.1',dimage="aniklogu/voipservice:updated")

#Define Server to Router Links
    net.addLink(srv1,router14,intfName2='r14-eth1',params2={ 'ip' : '199.199.199.129/25'})
    net.addLink(srv2,router15,intfName2='r15-eth1',params2={ 'ip' : '199.199.199.1/24'})

# Adding wifi stations
    sta5 = net.addStation('sta5', ip='192.168.20.50/24', cls=DockerSta, dimage="manash22/mc_project01:phone_wifi")
    sta6 = net.addStation('sta6', ip='192.168.20.51/24', cls=DockerSta, dimage="manash22/mc_project01:phone_wifi")

# Define Hosts
    h1 = net.addDocker( name='h1', ip='10.0.1.50/24',defaultRoute='via 10.0.1.1',dimage="manash22/mc_project01:phone_test_an1")
    h2 = net.addDocker( name='h2', ip='10.0.1.51/24',defaultRoute='via 10.0.1.1',dimage="manash22/mc_project01:phone_test_an1")
    h3 = net.addDocker( name='h3', ip='192.168.10.50/24', defaultRoute='via 192.168.10.1',dimage="manash22/mc_project01:phone_test_an2")
    h4 = net.addDocker( name='h4', ip='192.168.10.51/24', defaultRoute='via 192.168.10.1',dimage="manash22/mc_project01:phone_test_an2")

#DHCP demo hosts
    h101 = net.addHost( name='h101', ip='10.0.1.100/24',defaultRoute='via 10.0.1.1')
    h102 = net.addHost( name='h102', ip='192.168.10.100/24', defaultRoute='via 192.168.10.1')
    sta103 = net.addStation('sta103', ip='192.168.20.100/24' )

#Linking switch to Host
    for h,s in [(h1,s1),(h2,s1),(h101,s1),(h3,s2),(h4,s2),(h102,s2)]:
        net.addLink(h,s)

#Connecting DHCP servers

    net.addLink(dhcpsrv2,s2)
    net.addLink(dhcpsrv3,ap1)
    net.addLink(dhcpsrv1,s1)
# Define Controller


# Define Node name
    r1=net.getNodeByName('r1')
    r2=net.getNodeByName('r2')
    r3=net.getNodeByName('r3')
    r4=net.getNodeByName('r4')
    r5=net.getNodeByName('r5')
    r6=net.getNodeByName('r6')
    r7=net.getNodeByName('r7')
    r8=net.getNodeByName('r8')
    r9=net.getNodeByName('r9')
    r10=net.getNodeByName('r10')
    r11=net.getNodeByName('r11')
    r12=net.getNodeByName('r12')
    r13=net.getNodeByName('r13')
    r14=net.getNodeByName('r14')
    r15=net.getNodeByName('r15')


#Configuring WIFI nodes
    info('*** Configuring WiFi nodes\n')
    net.configureWifiNodes()

    net.build()
    os.system("service ospfd start")
    # c0.start()
    s1.start([])
    s2.start([])
    ap1.start([])

    info('starting zebra and ospfd  service:\n')

    info(net['r1'].cmd("ifconfig r1-eth0 hw ether 00:00:00:00:01:01"))
    info(net['r3'].cmd("ifconfig r3-eth0 hw ether 00:00:00:00:01:02"))
    info(net['r5'].cmd("ifconfig r5-eth0 hw ether 00:00:00:00:01:03"))

    info(net['s1'].cmd("ovs-ofctl add-flow s1 priority=1,arp,actions=flood"))
    info(net['s1'].cmd("ovs-ofctl add-flow s1 priority=65535,ip,dl_dst=00:00:00:00:01:01,actions=output:1"))
    info(net['s1'].cmd("ovs-ofctl add-flow s1 priority=10,ip,nw_dst=10.0.1.50,actions=output:2"))
    info(net['s1'].cmd("ovs-ofctl add-flow s1 priority=10,ip,nw_dst=10.0.0.51,actions=output:3"))
    info(net['s1'].cmd("ovs-ofctl add-flow s1 priority=20,udp,tp_dst=67,actions=output:5"))
    info(net['s1'].cmd("ovs-ofctl add-flow s1 priority=30,ip,actions=normal"))

    info(net['s2'].cmd("ovs-ofctl add-flow s2 priority=1,arp,actions=flood"))
    info(net['s2'].cmd("ovs-ofctl add-flow s2 priority=65535,ip,dl_dst=00:00:00:00:01:02,actions=output:1"))
    info(net['s2'].cmd("ovs-ofctl add-flow s2 priority=10,ip,nw_dst=192.168.10.50,actions=output:2"))
    info(net['s2'].cmd("ovs-ofctl add-flow s2 priority=10,ip,nw_dst=192.168.10.51,actions=output:3"))
    info(net['s2'].cmd("ovs-ofctl add-flow s2 priority=20,udp,tp_dst=67,actions=output:5"))
    info(net['s2'].cmd("ovs-ofctl add-flow s2 priority=30,ip,actions=normal"))

#Linking AP to stations
    sta5.cmd('iw dev sta5-wlan0 connect ssid_ap1')
    sta6.cmd('iw dev sta6-wlan0 connect ssid_ap1')
    sta103.cmd('iw dev sta103-wlan0 connect ssid_ap1')

    ap1.cmd("ovs-vsctl add-port ap1 ap1-wlan1 && ovs-vsctl add-port ap1 ap1-eth1")
    ap1.cmd("ovs-ofctl add-flow ap1 actions=normal")


#Adding default route to wifi stations
    sta5.cmd("ip route del default")
    sta5.cmd("ip route add default via 192.168.20.1 dev sta5-wlan0")
    sta6.cmd("ip route del default")
    sta6.cmd("ip route add default via 192.168.20.1 dev sta6-wlan0")
    sta103.cmd("ip route add default via 192.168.20.1 dev sta103-wlan0")

# Adding Dfault Route on EDge Routers
    r1.cmd("ip route del default")
    r1.cmd('ip route add default via 21.21.21.2 dev r1-eth0')
    r3.cmd("ip route del default")
    r3.cmd('ip route add default via 43.43.43.1 dev r3-eth0')
    r5.cmd("ip route del default")
    r5.cmd('ip route add default via 65.65.65.1 dev r5-eth0')
    r14.cmd("ip route del default")
    r14.cmd('ip route add default via 148.148.148.1 dev r14-eth0')
    r15.cmd("ip route del default")
    r15.cmd('ip route add default via 200.200.200.1 dev r15-eth0')

# Disabling rp_filter
    for x in range(1,15):
        info(net["r%s"%x].cmd("sysctl net.ipv4.conf.all.rp_filter=2"))
    time.sleep(1)

    srv1.cmd("sysctl net.ipv4.conf.all.rp_filter=2")
    srv2.cmd("sysctl net.ipv4.conf.all.rp_filter=2")

# Configuring OSPF/Quagga Configuration

    path = "/home/manash/containernet/examples/quagga1"
    r2.cmd('zebra -f %s/r2zebra.conf -d -i %s/r2zebra > %s/r2zebra.log' % (path,path,path))
    r4.cmd('zebra -f %s/r4zebra.conf -d -i %s/r4zebra > %s/r4zebra.log' % (path,path,path))
    r6.cmd('zebra -f %s/r6zebra.conf -d -i %s/r6zebra > %s/r6zebra.log' % (path,path,path))
    r7.cmd('zebra -f %s/r7zebra.conf -d -i %s/r7zebra > %s/r7zebra.log' % (path,path,path))
    r8.cmd('zebra -f %s/r8zebra.conf -d -i %s/r8zebra > %s/r8zebra.log' % (path,path,path))
    r9.cmd('zebra -f %s/r9zebra.conf -d -i %s/r9zebra > %s/r9zebra.log' % (path,path,path))
    r10.cmd('zebra -f %s/r10zebra.conf -d -i %s/r10zebra > %s/r10zebra.log' % (path,path,path))
    r11.cmd('zebra -f %s/r11zebra.conf -d -i %s/r11zebra > %s/r11zebra.log' % (path,path,path))
    r12.cmd('zebra -f %s/r12zebra.conf -d -i %s/r12zebra > %s/r12zebra.log' % (path,path,path))
    r13.cmd('zebra -f %s/r13zebra.conf -d -i %s/r13zebra > %s/r13zebra.log' % (path,path,path))
    time.sleep(1)       #time for zebra to create api socket

# Zebra API creation
    time.sleep(1)#time for zebra to create api socket
    r2.cmd('zebra -f %s/r2zebra.conf -d -z %s/r2zebra.api -i %s/r2zebra.interface' % (path,path,path))
    r4.cmd('zebra -f %s/r4zebra.conf -d -z %s/r4zebra.api -i %s/r4zebra.interface' % (path,path,path))
    r6.cmd('zebra -f %s/r6zebra.conf -d -z %s/r6zebra.api -i %s/r6zebra.interface' % (path,path,path))
    r7.cmd('zebra -f %s/r7zebra.conf -d -z %s/r7zebra.api -i %s/r7zebra.interface' % (path,path,path))
    r8.cmd('zebra -f %s/r8zebra.conf -d -z %s/r8zebra.api -i %s/r8zebra.interface' % (path,path,path))
    r9.cmd('zebra -f %s/r9zebra.conf -d -z %s/r9zebra.api -i %s/r9zebra.interface' % (path,path,path))
    r10.cmd('zebra -f %s/r10zebra.conf -d -z %s/r10zebra.api -i %s/r10zebra.interface' % (path,path,path))
    r11.cmd('zebra -f %s/r11zebra.conf -d -z %s/r11zebra.api -i %s/r11zebra.interface' % (path,path,path))
    r12.cmd('zebra -f %s/r12zebra.conf -d -z %s/r12zebra.api -i %s/r12zebra.interface' % (path,path,path))
    r13.cmd('zebra -f %s/r13zebra.conf -d -z %s/r13zebra.api -i %s/r13zebra.interface' % (path,path,path))

# OSPFD Service
    r2.cmd('ospfd -f %s/r2ospfd.conf -d -z %s/r2zebra.api -i %s/r2ospfd.interface' % (path,path,path))
    r4.cmd('ospfd -f %s/r4ospfd.conf -d -z %s/r4zebra.api -i %s/r4ospfd.interface' % (path,path,path))
    r6.cmd('ospfd -f %s/r6ospfd.conf -d -z %s/r6zebra.api -i %s/r6ospfd.interface' % (path,path,path))
    r7.cmd('ospfd -f %s/r7ospfd.conf -d -z %s/r7zebra.api -i %s/r7ospfd.interface' % (path,path,path))
    r8.cmd('ospfd -f %s/r8ospfd.conf -d -z %s/r8zebra.api -i %s/r8ospfd.interface' % (path,path,path))
    r9.cmd('ospfd -f %s/r9ospfd.conf -d -z %s/r9zebra.api -i %s/r9ospfd.interface' % (path,path,path))
    r10.cmd('ospfd -f %s/r10ospfd.conf -d -z %s/r10zebra.api -i %s/r10ospfd.interface' % (path,path,path))
    r11.cmd('ospfd -f %s/r11ospfd.conf -d -z %s/r11zebra.api -i %s/r11ospfd.interface' % (path,path,path))
    r12.cmd('ospfd -f %s/r12ospfd.conf -d -z %s/r12zebra.api -i %s/r12ospfd.interface' % (path,path,path))
    r13.cmd('ospfd -f %s/r13ospfd.conf -d -z %s/r13zebra.api -i %s/r13ospfd.interface' % (path,path,path))

#Access Network 1 to Access Network 2 Geneve Tunnel
    r1.cmd('ip link add dev gnv0 type geneve remote 43.43.43.2 vni 500')
    r1.cmd('ip link set gnv0 up')
    r1.cmd('ip addr add 50.50.50.1/24 dev gnv0')
    r1.cmd('ip route add 192.168.10.0/24 via 50.50.50.2 encap ip  dev gnv0')

    r3.cmd('ip link add dev gnv0 type geneve remote 21.21.21.1 vni 500')
    r3.cmd('ip link set gnv0 up')
    r3.cmd('ip addr add 50.50.50.2/24 dev gnv0')
    r3.cmd('ip route add 10.0.1.0/24 via 50.50.50.1 encap ip  dev gnv0')

#Access Network 1 to Access Network 3 Geneve Tunnel
    r1.cmd('ip link add dev gnv1 type geneve remote 65.65.65.2 vni 700')
    r1.cmd('ip link set gnv1 up')
    r1.cmd('ip addr add 70.70.70.1/24 dev gnv1')
    r1.cmd('ip route add 192.168.20.0/24 via 70.70.70.2 encap ip  dev gnv1')

    r5.cmd('ip link add dev gnv1 type geneve remote 21.21.21.1 vni 700')
    r5.cmd('ip link set gnv1 up')
    r5.cmd('ip addr add 70.70.70.2/24 dev gnv1')
    r5.cmd('ip route add 10.0.1.0/24 via 70.70.70.1 encap ip  dev gnv1')

#Access Network 2 to Access Network 3 Geneve Tunnel
    r3.cmd('ip link add dev gnv2 type geneve remote 65.65.65.2 vni 900')
    r3.cmd('ip link set gnv2 up')
    r3.cmd('ip addr add 90.90.90.1/24 dev gnv2')
    r3.cmd('ip route add 192.168.20.0/24 via 90.90.90.2 encap ip  dev gnv2')

    r5.cmd('ip link add dev gnv2 type geneve remote 43.43.43.2 vni 900')
    r5.cmd('ip link set gnv2 up')
    r5.cmd('ip addr add 90.90.90.2/24 dev gnv2')
    r5.cmd('ip route add 192.168.10.0/24 via 90.90.90.1 encap ip  dev gnv2')

#Access Network 1 to VOIP server 1 Geneve Tunnel
    r1.cmd('ip link add dev gnv3 type geneve remote 148.148.148.2 vni 484')
    r1.cmd('ip link set gnv3 up')
    r1.cmd('ip addr add 2.2.2.1/24 dev gnv3')
    r1.cmd('ip route add 199.199.199.128/25 via 2.2.2.2 encap ip  dev gnv3')

    r14.cmd('ip link add dev gnv3 type geneve remote 21.21.21.1 vni 484')
    r14.cmd('ip link set gnv3 up')
    r14.cmd('ip addr add 2.2.2.2/24 dev gnv3')
    r14.cmd('ip route add 10.0.1.0/24 via 2.2.2.1 encap ip  dev gnv3')

#Access Network 2 to VOIP server 1 Geneve Tunnel
    r3.cmd('ip link add dev gnv4 type geneve remote 148.148.148.2 vni 584')
    r3.cmd('ip link set gnv4 up')
    r3.cmd('ip addr add 4.4.4.1/24 dev gnv4')
    r3.cmd('ip route add 199.199.199.128/25 via 4.4.4.2 encap ip  dev gnv4')

    r14.cmd('ip link add dev gnv4 type geneve remote 43.43.43.2 vni 584')
    r14.cmd('ip link set gnv4 up')
    r14.cmd('ip addr add 4.4.4.2/24 dev gnv4')
    r14.cmd('ip route add 192.168.10.0/24 via 4.4.4.1 encap ip  dev gnv4')

#Access Network 3 to VOIP server 1 Geneve Tunnel
    r5.cmd('ip link add dev gnv5 type geneve remote 148.148.148.2 vni 684')
    r5.cmd('ip link set gnv5 up')
    r5.cmd('ip addr add 6.6.6.1/24 dev gnv5')
    r5.cmd('ip route add 199.199.199.128/25 via 6.6.6.2 encap ip  dev gnv5')

    r14.cmd('ip link add dev gnv5 type geneve remote 65.65.65.2 vni 684')
    r14.cmd('ip link set gnv5 up')
    r14.cmd('ip addr add 6.6.6.2/24 dev gnv5')
    r14.cmd('ip route add 192.168.20.0/24 via 6.6.6.1 encap ip  dev gnv5')


#Access Network 1 to VOIP server 2 Geneve Tunnel
    r1.cmd('ip link add dev gnv103 type geneve remote 200.200.200.2 vni 103')
    r1.cmd('ip link set gnv103 up')
    r1.cmd('ip addr add 3.3.3.1/24 dev gnv103')
    r1.cmd('ip route add 199.199.199.0/24 via 3.3.3.2 encap ip  dev gnv103 metric 200')

    r15.cmd('ip link add dev gnv103 type geneve remote 21.21.21.1 vni 103')
    r15.cmd('ip link set gnv103 up')
    r15.cmd('ip addr add 3.3.3.2/24 dev gnv103')
    r15.cmd('ip route add 10.0.1.0/24 via 3.3.3.1 encap ip  dev gnv103')

#Access Network 2 to VOIP server 2 Geneve Tunnel
    r3.cmd('ip link add dev gnv104 type geneve remote 200.200.200.2 vni 104')
    r3.cmd('ip link set gnv104 up')
    r3.cmd('ip addr add 5.5.5.1/24 dev gnv104')
    r3.cmd('ip route add 199.199.199.0/24 via 5.5.5.2 encap ip  dev gnv104 metric 200')

    r15.cmd('ip link add dev gnv104 type geneve remote 43.43.43.2 vni 104')
    r15.cmd('ip link set gnv104 up')
    r15.cmd('ip addr add 5.5.5.2/24 dev gnv104')
    r15.cmd('ip route add 192.168.10.0/24 via 5.5.5.1 encap ip  dev gnv104')

#Access Network 3 to VOIP server 2 Geneve Tunnel
    r5.cmd('ip link add dev gnv105 type geneve remote 200.200.200.2 vni 105')
    r5.cmd('ip link set gnv105 up')
    r5.cmd('ip addr add 7.7.7.1/24 dev gnv105')
    r5.cmd('ip route add 199.199.199.0/24 via 7.7.7.2 encap ip  dev gnv105 metric 200')

    r15.cmd('ip link add dev gnv105 type geneve remote 200.200.200.2 vni 105')
    r15.cmd('ip link set gnv105 up')
    r15.cmd('ip addr add 7.7.7.2/24 dev gnv105')
    r15.cmd('ip route add 192.168.20.0/24 via 7.7.7.1 encap ip  dev gnv105')

# H1 to H3 Geneve Tunnel with IP rule
    r1.cmd('ip link add dev gnv13 type geneve remote 43.43.43.2 vni 13')
    r1.cmd('ip link set gnv13 up')
    r1.cmd('ip addr add 13.13.13.13/24 dev gnv13')
    r1.cmd('ip rule add from 10.0.1.50 to 192.168.10.50 table 13')
    r1.cmd('ip route add 192.168.10.50 via 13.13.13.31 encap ip  dev gnv13 table 13')

    r3.cmd('ip link add dev gnv13 type geneve remote 21.21.21.1 vni 13')
    r3.cmd('ip link set gnv13 up')
    r3.cmd('ip addr add 13.13.13.31/24 dev gnv13')
    r3.cmd('ip rule add from 192.168.10.50 to 10.0.1.50 table 13')
    r3.cmd('ip route add 10.0.1.50 via 13.13.13.13 encap ip  dev gnv13 table 13')

# H2 to H4 Geneve Tunnel with IP rule
    r1.cmd('ip link add dev gnv24 type geneve remote 43.43.43.2 vni 24')
    r1.cmd('ip link set gnv24 up')
    r1.cmd('ip addr add 24.24.24.24/24 dev gnv24')
    r1.cmd('ip rule add from 10.0.1.51 to 192.168.10.51 table 24')
    r1.cmd('ip route add 192.168.10.51 via 24.24.24.42 encap ip  dev gnv24 table 24')

    r3.cmd('ip link add dev gnv24 type geneve remote 21.21.21.1 vni 24')
    r3.cmd('ip link set gnv24 up')
    r3.cmd('ip addr add 24.24.24.42/24 dev gnv24')
    r3.cmd('ip rule add from 192.168.10.51 to 10.0.1.51 table 24')
    r3.cmd('ip route add 10.0.1.51 via 24.24.24.24 encap ip  dev gnv24 table 24')

# H1 to H5 Geneve Tunnel with IP rule
    r1.cmd('ip link add dev gnv15 type geneve remote 65.65.65.2 vni 15')
    r1.cmd('ip link set gnv15 up')
    r1.cmd('ip addr add 15.15.15.15/24 dev gnv15')
    r1.cmd('ip rule add from 10.0.1.50 to 192.168.20.50 table 15')
    r1.cmd('ip route add 192.168.20.50 via 15.15.15.51 encap ip  dev gnv15 table 15')

    r5.cmd('ip link add dev gnv15 type geneve remote 21.21.21.1 vni 15')
    r5.cmd('ip link set gnv15 up')
    r5.cmd('ip addr add 15.15.15.51/24 dev gnv15')
    r5.cmd('ip rule add from 192.168.20.50 to 10.0.1.50 table 15')
    r5.cmd('ip route add 10.0.1.50 via 15.15.15.15 encap ip  dev gnv15 table 15')

# H2 to H6 Geneve Tunnel with IP rule
    r1.cmd('ip link add dev gnv26 type geneve remote 65.65.65.2 vni 26')
    r1.cmd('ip link set gnv26 up')
    r1.cmd('ip addr add 26.26.26.26/24 dev gnv26')
    r1.cmd('ip rule add from 10.0.1.51 to 192.168.20.51 table 26')
    r1.cmd('ip route add 192.168.20.51 via 26.26.26.62 encap ip  dev gnv26 table 26')

    r5.cmd('ip link add dev gnv26 type geneve remote 21.21.21.1 vni 26')
    r5.cmd('ip link set gnv26 up')
    r5.cmd('ip addr add 26.26.26.62/24 dev gnv26')
    r5.cmd('ip rule add from 192.168.20.51 to 10.0.1.51 table 26')
    r5.cmd('ip route add 10.0.1.51 via 26.26.26.26 encap ip  dev gnv26 table 26')

# H3 to H5 Geneve Tunnel with IP rule
    r3.cmd('ip link add dev gnv35 type geneve remote 65.65.65.2 vni 35')
    r3.cmd('ip link set gnv35 up')
    r3.cmd('ip addr add 35.35.35.35/24 dev gnv35')
    r3.cmd('ip rule add from 192.168.10.50 to 192.168.20.50 table 35')
    r3.cmd('ip route add 192.168.20.50 via 35.35.35.53 encap ip  dev gnv35 table 35')

    r5.cmd('ip link add dev gnv35 type geneve remote 43.43.43.2 vni 35')
    r5.cmd('ip link set gnv35 up')
    r5.cmd('ip addr add 35.35.35.53/24 dev gnv35')
    r5.cmd('ip rule add from 192.168.20.50 to 192.168.10.50 table 35')
    r5.cmd('ip route add 192.168.10.50 via 35.35.35.35 encap ip  dev gnv35 table 35')

# H4 to H6 Geneve Tunnel with IP rule
    r3.cmd('ip link add dev gnv46 type geneve remote 65.65.65.2 vni 46')
    r3.cmd('ip link set gnv46 up')
    r3.cmd('ip addr add 46.46.46.46/24 dev gnv46')
    r3.cmd('ip rule add from 192.168.10.51 to 192.168.20.51 table 46')
    r3.cmd('ip route add 192.168.20.51 via 46.46.46.64 encap ip  dev gnv46 table 46')

    r5.cmd('ip link add dev gnv46 type geneve remote 43.43.43.2 vni 46')
    r5.cmd('ip link set gnv46 up')
    r5.cmd('ip addr add 46.46.46.64/24 dev gnv46')
    r5.cmd('ip rule add from 192.168.20.51 to 192.168.10.51 table 46')
    r5.cmd('ip route add 192.168.10.51 via 46.46.46.46 encap ip  dev gnv46 table 46')


# Iptable rules binding Linphone hosts allowing other hosts to comminicate with each other

# h1 to sta5
    r1.cmd('iptables -t raw -I PREROUTING -s 10.0.1.50 -d 192.168.20.50 -j ACCEPT')
    r1.cmd('iptables -t raw -A PREROUTING -s 10.0.1.50 -d 192.168.20.0/24 -j DROP')
# h2 to sta6
    r1.cmd('iptables -t raw -I PREROUTING -s 10.0.1.51 -d 192.168.20.51 -j ACCEPT')
    r1.cmd('iptables -t raw -A PREROUTING -s 10.0.1.51 -d 192.168.20.0/24 -j DROP')

# h1 to h3
    r1.cmd('iptables -t raw -I PREROUTING -s 10.0.1.50 -d 192.168.10.50 -j ACCEPT')
    r1.cmd('iptables -t raw -A PREROUTING -s 10.0.1.50 -d 192.168.10.0/24 -j DROP')
# h2 to h4
    r1.cmd('iptables -t raw -I PREROUTING -s 10.0.1.51 -d 192.168.10.51 -j ACCEPT')
    r1.cmd('iptables -t raw -A PREROUTING -s 10.0.1.51 -d 192.168.10.0/24 -j DROP')

# h3 to h1
    r3.cmd('iptables -t raw -I PREROUTING -s 192.168.10.50 -d 10.0.1.50 -j ACCEPT')
    r3.cmd('iptables -t raw -A PREROUTING -s 192.168.10.50 -d 10.0.1.0/24 -j DROP')
# h4 to h2
    r3.cmd('iptables -t raw -I PREROUTING -s 192.168.10.51 -d 10.0.1.51 -j ACCEPT')
    r3.cmd('iptables -t raw -A PREROUTING -s 192.168.10.51 -d 10.0.1.0/24 -j DROP')

# h3 to h5
    r3.cmd('iptables -t raw -I PREROUTING -s 192.168.10.50 -d 192.168.20.50 -j ACCEPT')
    r3.cmd('iptables -t raw -A PREROUTING -s 192.168.10.50 -d 192.168.20.0/24 -j DROP')
# h4 to h6
    r3.cmd('iptables -t raw -I PREROUTING -s 192.168.10.51 -d 192.168.20.51 -j ACCEPT')
    r3.cmd('iptables -t raw -A PREROUTING -s 192.168.10.51 -d 192.168.20.0/24 -j DROP')

# sta5 to h1
    r5.cmd('iptables -t raw -I PREROUTING -s 192.168.20.50 -d 10.0.1.50 -j ACCEPT')
    r5.cmd('iptables -t raw -A PREROUTING -s 192.168.20.50 -d 10.0.1.0/24 -j DROP')
# sta6 to h2
    r5.cmd('iptables -t raw -I PREROUTING -s 192.168.20.51 -d 10.0.1.51 -j ACCEPT')
    r5.cmd('iptables -t raw -A PREROUTING -s 192.168.20.51 -d 10.0.1.0/24 -j DROP')

# sta5 to h3
    r5.cmd('iptables -t raw -I PREROUTING -s 192.168.20.50 -d 192.168.10.50 -j ACCEPT')
    r5.cmd('iptables -t raw -A PREROUTING -s 192.168.20.50 -d 192.168.10.0/24 -j DROP')
# sta6 to h4
    r5.cmd('iptables -t raw -I PREROUTING -s 192.168.20.51 -d 192.168.10.51 -j ACCEPT')
    r5.cmd('iptables -t raw -A PREROUTING -s 192.168.20.51 -d 192.168.10.0/24 -j DROP')

# Define tc classed
    r2.cmd('tc qdisc add dev r2-eth1 root handle 1: htb default 30')
    r2.cmd('tc class add dev r2-eth1 parent 1: classid 1:1 htb rate 1.5mbit')
    r2.cmd('tc class add dev r2-eth1 parent 1:1 classid 1:10 htb rate 1mbit ceil 1.5mbit')
    r2.cmd('tc class add dev r2-eth1 parent 1:1 classid 1:20 htb rate 400kbit ceil 800kbit')
    r2.cmd('tc class add dev r2-eth1 parent 1:1 classid 1:30 htb rate 50kbit ceil 200kbit')
    r2.cmd('tc qdisc add dev r2-eth1 parent 1:10 handle 10:sfq perturb 10')
    r2.cmd('tc qdisc add dev r2-eth1 parent 1:20 handle 20:sfq perturb 10')
    r2.cmd('tc qdisc add dev r2-eth1 parent 1:30 handle 30:sfq perturb 10')

# Adding Filters

    r2.cmd('tc filter add dev r2-eth1 protocol ip parent 1:prio 1 u32 match ip src 10.0.1.50/32 flowid 1:20')
    r2.cmd('tc filter add dev r2-eth1 protocol ip parent 1:prio 2 u32 match ip src 10.0.1.51/32 flowid 1:30')

# Adding voip-server to /etc/Hosts
    dhcpsrv1.cmd("echo '199.199.199.199 group10.com' >> /etc/hosts")
    dhcpsrv2.cmd("echo '199.199.199.199 group10.com' >> /etc/hosts")
    dhcpsrv3.cmd("echo '199.199.199.199 group10.com' >> /etc/hosts")
    time.sleep(2)

# Starting dnsmasq service
    dhcpsrv1.cmd('/etc/init.d/dnsmasq start')
    dhcpsrv2.cmd('/etc/init.d/dnsmasq start')
    dhcpsrv3.cmd('/etc/init.d/dnsmasq start')

# Adding DNS nameserver to hosts
    h1.cmd("echo 'nameserver 10.0.1.150' > /etc/resolv.conf")
    h2.cmd("echo 'nameserver 10.0.1.150' > /etc/resolv.conf")
    h3.cmd("echo 'nameserver 192.168.10.160' > /etc/resolv.conf")
    h4.cmd("echo 'nameserver 192.168.10.160' > /etc/resolv.conf")
    sta5.cmd("echo 'nameserver 192.168.20.170' > /etc/resolv.conf")
    sta6.cmd("echo 'nameserver 192.168.20.170' > /etc/resolv.conf")

# Starting Mysql and Kamailio Service
    srv1.cmd('/etc/init.d/mysql start')
    time.sleep(10)
    srv1.cmd('/etc/init.d/kamailio start')

# DHCP demo hosts requesting IP to DHCP Server
    h101.cmd('dhclient -r h101-eth0')
    h101.cmd('dhclient h101-eth0')
    time.sleep(1)

    h102.cmd('dhclient -r h102-eth0')
    h102.cmd('dhclient h102-eth0')
    time.sleep(1)

    sta103.cmd('dhclient -r sta103-wlan0')
    sta103.cmd('dhclient sta103-wlan0')
    time.sleep(1)

# DYnamic geneve tunnel tracking scripts
    r1.cmd("sh ./r1_srv1.sh &")
    r1.cmd("sh ./r1_srv2.sh &")
    r3.cmd("sh ./r3_srv1.sh &")
    r3.cmd("sh ./r3_srv2.sh &")
    r5.cmd("sh ./r5_srv1.sh &")
    r5.cmd("sh ./r5_srv2.sh &")
    r14.cmd("sh ./r14_srv1.sh &")
    r15.cmd("sh ./r15_srv2.sh &")

    CLI( net )
    net.stop()
    os.system("killall -9 ospfd zebra")
    os.system("rm -f %s/*api*" % (path))
    os.system("rm -f %s/*interface*" % (path))
    os.system("rm -f %s/r*zebra" % (path))
    os.system("rm -f %s/*log" % (path))

if __name__=='__main__':
    setLogLevel( 'info' )
    ospftopo()
