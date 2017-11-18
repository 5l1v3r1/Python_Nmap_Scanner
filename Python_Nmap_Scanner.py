#!/usr/bin/python

from nmap import PortScanner
import nmap
nm = nmap.PortScanner()
def Nmap_Scanner():
	with open('domain.txt','r') as domain_file:
		domains = domain_file.readlines()
		for domain in domains:
			domain = domain.rstrip()
			print "URL: "+domain
			logs = nm.scan(domain,'80-443')
			#print logs
			print 'Command: '+nm.command_line()
			for host in nm.all_hosts():
     				print('----------------------------------------------------')
     				print('Host : %s (%s)' % (host, nm[host].hostname()))
     				print('State : %s' % nm[host].state())
				for proto in nm[host].all_protocols():
         				print('----------')
         				print('Protocol : %s' % proto)

         				lport = nm[host][proto].keys()
         				lport.sort()
         				for port in lport:
             					print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
			print '------------------------------------------------------'

def main():
	Nmap_Scanner()

if __name__ =='__main__':
        main()
