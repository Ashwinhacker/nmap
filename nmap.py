print("""                                                           
888b      88                                               
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

import subprocess


def run_nmap_scan():
    target = input("Enter the target IP address or hostname: ")
    command = ["nmap", "-sn", target]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        print(f"An error occurred: {error.decode('utf-8')}")
    else:
        print(f"Nmap scan results:\n{output.decode('utf-8')}")

# Call the function to run the Nmap scan
run_nmap_scan()
