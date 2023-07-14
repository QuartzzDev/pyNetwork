# QuartzzDev

import psutil
from prettytable import PrettyTable
import time

def get_network_usage():
    connections = psutil.net_io_counters(pernic=True)

    network_usage = []
    
    for interface, connection in connections.items():
        interface_usage = [
            interface,
            connection.bytes_sent / 1024 / 1024,
            connection.bytes_recv / 1024 / 1024,
            connection.packets_sent,
            connection.packets_recv
        ]
        network_usage.append(interface_usage)

    return network_usage

def display_network_usage(network_usage):
    table = PrettyTable(["Arayüz", "Gönderilen (MB)", "Alınan (MB)", "Gönderilen Paketler", "Alınan Paketler"])
    for usage in network_usage:
        table.add_row(usage)
    print(table)

def main():
    network_usage = get_network_usage()
    display_network_usage(network_usage)

    while True:
        time.sleep(1)
        updated_network_usage = get_network_usage()
        for i in range(len(network_usage)):
            network_usage[i][1] = updated_network_usage[i][1]
            network_usage[i][2] = updated_network_usage[i][2]
            network_usage[i][3] = updated_network_usage[i][3]
            network_usage[i][4] = updated_network_usage[i][4]
        
        display_network_usage(network_usage)

if __name__ == "__main__":
    main()
