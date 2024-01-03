print("""
                                                          
8888b     88                                               
88 `8b    88                                               
88  `8b   88  88,dPYba,,adPYba,   ,adPPYYba,  8b,dPPYba,   
88   `8b  88  88P'   "88"    "8a  ""     `Y8  88P'    "8a  
88    `8b 88  88      88      88  ,adPPPPP88  88       d8  
88     `8888  88      88      88  88,    ,88  88b,   ,a8"  
88      `888  88      88      88  `"8bbdP"Y8  88`YbbdP"'   
                                              88           
                                              88                                            
   """)

import nmap
def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p 1-1024')  # Scan ports 1 through 1024, adjust as needed

    for host in nm.all_hosts():
        print(f"Host: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"Port: {port}, State: {nm[host][proto][port]['state']}")

if __name__ == "__main__":
    target = input("Enter the target domain or IP address: ")
    scan_ports(target)
