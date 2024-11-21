import psutil
import time

def convert_bytes(bytes):

    sizes = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while bytes >= 1024 and i < len(sizes)-1:
        bytes /= 1024
        i += 1
    return f"{bytes:.2f} {sizes[i]}"

def get_wifi_data_usage(wifi_name):
  
    data_usage = 0

    interfaces = psutil.net_io_counters(pernic=True)

    wifi_interface = None
    for interface in interfaces:
        if wifi_name in interface:
            wifi_interface = interface
            break

    if wifi_interface is None:
        print(f"WiFi network '{wifi_name}' not found.")
        return

    try:
        while True:
           
            network_io = psutil.net_io_counters(pernic=True)[wifi_interface]
            data_usage = network_io.bytes_recv + network_io.bytes_sent

            print(f"Data Usage: {convert_bytes(data_usage)}", end='\r')

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting data usage monitor.")

if __name__ == "__main__":
    wifi_name = "WiFi"
    get_wifi_data_usage(wifi_name)
