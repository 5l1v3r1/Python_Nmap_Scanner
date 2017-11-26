#!/usr/bin/python
import nmap
import time

def banner():

        print O+'###########################################################################################'
        print '#                               <<<Python Nmap Scanner>>>                                   #'
        print '#                               Made by <<RISHABH SHARMA>>                                  #'
        print '#                                 Twitter : @blacknet22                                     #'
        print '############################################################################################'+END


# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

def Nmap_Scanner(domaintoscan,porttoscan):
        nm = nmap.PortScanner()
        print BOLD+R+'Time: '+END+Y+str(time.ctime(time.time()))
        print BOLD+R+"Scanning URL: "+END+Y+domaintoscan+END
        logs = nm.scan(domaintoscan,arguments='-sS --open -sV -p '+porttoscan)
        print BOLD+R+'Nmap Command: '+END+Y+nm.command_line()+END
        for host in nm.all_hosts():
        	print BOLD+G+'-------------------------------------------------------------------------------------------------------'+END
                #print('Host : %s (%s)'% (host, nm[host].hostname()))
                print BOLD+R+'Host: '+END+Y+str(host)+' ('+str(nm[host].hostname())+')'+END
                #print('State : %s' %nm[host].state())
                print BOLD+R+'State: '+END+Y+str(nm[host].state())+END
                for proto in nm[host].all_protocols():
                	print('----------')
                        print(BOLD+R+'Protocol: '+END+Y+str(proto))
                        lport = nm[host][proto].keys()
                        lport.sort()
                        #print 'lport: ',lport
                        for port in lport:
                        	#print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                                data = (nm[host][proto][port])
                                service = data['name']
                                product = data['product']
				version = data['version']
                                print  BOLD+O+'Port : '+END+Y+str(port)+END+BOLD+O+'\tState : '+END+Y+str(nm[host][proto][port]['state'])+END+BOLD+O+'\tService : '+END+Y+service+END+BOLD+O+'\tProduct : '+END+Y+product+END+BOLD+O+'\tVersion : '+END+Y+product+END
                print BOLD+G+'---------------------------------------------------------------------------------------------------------'+END

def main():
	banner()
        domaintoscan = raw_input(BOLD+O+"Enter Domain Name to Scan (ex: microsoft.com): "+END)
	porttoscan = raw_input(BOLD+O+"Enter Port Range or Port Number (ex: 80-443 or 80): "+END)
        print '\n'
	Nmap_Scanner(domaintoscan,porttoscan)
if __name__ =='__main__':
        main()
