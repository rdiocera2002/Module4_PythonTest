import unittest
import re
from ipaddress import ip_network, ip_address

devices = {
    "R1": {
        "location": "TIP_Manila", #Diocera
        "ip_address": "192.168.45.25",
        "subnet_mask": "255.255.255.265"
    },
    "PC": {
        "ip_address": "192.168.1.100", #Diocera
        "mac_address": "00:1A:2B:3C:4D:5E"
    },
    "Device": { 
        "type": "router"
    } #Diocera
}

def is_correct_ip_format(ip): #Diocera
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False

def is_correct_mac_format(mac): #Diocera
    return re.match("[0-9A-Fa-f]{2}([-:])(?:[0-9A-Fa-f]{2}\\1){4}[0-9A-Fa-f]{2}", mac) is not None

def is_valid_device_type(device_type): #Diocera
    return device_type in ["router", "personal computer", "switch", "server"]

def is_subnet_mask_valid(subnet_mask, prefix_length): #Diocera
    try:
        network = ip_network(f"0.0.0.0/{prefix_length}", strict=False)
        return subnet_mask == str(network.netmask)
    except ValueError:
        return False

class NetworkTest(unittest.TestCase): #Diocera

    def test_location_and_ip(self): #Diocera
        r1 = devices["R1"]
        self.assertEqual(r1["location"], "TIP_Manila")
        self.assertEqual(r1["ip_address"], "192.168.45.25")
        self.assertEqual(r1["subnet_mask"], "255.255.255.0")

    def test_ip_and_mac_format(self): #Diocera
        pc = devices["PC"]
        self.assertTrue(is_correct_ip_format(pc["ip_address"]))
        self.assertTrue(is_correct_mac_format(pc["mac_address"]))

    def test_device_type(self): #Diocera
        router = devices["Device"]
        self.assertTrue(is_valid_device_type(router["type"]))

    def test_subnet_mask(self): #Diocera
        r1 = devices["R1"]
        prefix_length = 24
        self.assertTrue(is_subnet_mask_valid(r1["subnet_mask"], prefix_length))

if __name__ == '__main__':
    unittest.main()