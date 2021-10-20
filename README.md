# 5G-network-slicing
5G Network Slicing in an Emulated Network environment : VoIP communication through GENEVE using Docker within Mininet environment
Containnernet :

Our script use containernet with mininet-wifi support. It needs to be installed on the base machine before running the script.
Containernet installation:
Follow the below mentioned steps for the installation.
~$ sudo apt-get install ansible git aptitude
~$ git clone https://github.com/ramonfontes/containernet.git
~$ cd containernet/ansible
~/containernet/ansible$ sudo ansible-playbook -i "localhost," -c local install.yml
~$ cd ..
~/containernet$ sudo python setup.py install
	Source ( https://mininet-wifi.github.io/containernet/)

Quagga
Our implementation of the routing uses quagga. 

Quagga installation: 
	Step 1: sudo apt-get install quagga

Step 2: Extract router config files from the “quagga.tar.gz” and place them on your desired location.
	
	Step 3: Change the user and group ownership for the config files to “quagga”
		sudo chown quagga:quagga <path>/*.conf
	
	Step 4: Change permision to 640 for the configuration files
		sudo chmod 777 <path>/*.conf
	
	Step 5: Copy the path to the new location of the router config files.

Step 6: Open the “Geneve_VOIP.py” file and change the “path” variable value with the new file location ( it’s under section “Configuring OSPF/Quagga Configuration”).

Docker images :
The docker images can be downloaded from the docker hub  ( https://hub.docker.com/r/manash22/mc_project01 ).
Images needed: 
You can run the script the directly and the Containernet will download the images by itself. But it is suggested to download them before running the program.
    1. r1
    2. r3
    3. r5
    4. r14
    5. r15
    6. phone_test_an1
    7. phone_test_an2
    8. phone_wifi
    9. voip
    10. dhcpsrv1
    11. dhcpsrv2
    12. dhcpsrv3
Testing VOIP:
    1. VOIP registration can be done from two users from each access network as they are running on docker images which already have linphone installed.
        a. H1 and H2 in Access network 1
        b. H3 and H4 in Access network 2
        c. Sta5 and Sta6 in Access network 3
    2. Once you get the prompt of “containernet>” use command “xterm <host> to access the individual host machines.
    3. Individual tunnels are set between host machines.
        a. H1 and H3
        b. H1 and Sta5
        c. H2 and H4
        d. H2 and Sta6
        e. H3 and Sta5
        f. H4 and Sta6
    4. Once accessed you can run “linphonec” and once getting the prompt “linphone>” you can register a user “register sip:username@199.199.199.199 199.199.199.199 password”.
    5. To setup a call use “call <username>”
    6. User “h101, h102 and sta103” are for demonstration of DHCP service.
Note : 
    1. As there are multiple docker images, the program will take some time to run.
    2. If the registration fails then access the VOIP server and restart the kamailio (/etc/init.d/kamailio start”
