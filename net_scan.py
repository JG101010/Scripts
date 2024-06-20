import subprocess
import csv

def ping(ip):
    try:
        # Ping the IP address
        output = subprocess.run(["ping", "-c", "1", "-W", "1000", ip], capture_output=True, text=True)
        # Check if the ping was successful
        if "1 packets transmitted, 1 packets received" in output.stdout:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def network_sweep(ip_list):
    for ip in ip_list:
        if ping(ip):
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")

def read_ips_from_csv(file_path):
    ip_addresses = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row:
                    ip_addresses.append(row[0])
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
    return ip_addresses

# Path to the CSV file containing IP addresses
csv_file_path = 'ip_addresses.csv'

# Read IP addresses from the CSV file
ip_addresses = read_ips_from_csv(csv_file_path)

# Perform the network sweep
network_sweep(ip_addresses)
