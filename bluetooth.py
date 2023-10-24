import bluetooth

def scan_for_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=8, device_id=-1, device_name=None, duration_id=-1, length_id=-1, address=None, len_inq=8, lookup_class=False, device_class=None, unknown8=None)
    
    if nearby_devices:
        print("Found nearby Bluetooth devices:")
        for addr, name in nearby_devices:
            print(f"Device Name: {name}, Address: {addr}")
    else:
        print("No nearby Bluetooth devices found.")

if __name__ == "__main__":
    scan_for_devices()
