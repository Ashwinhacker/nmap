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