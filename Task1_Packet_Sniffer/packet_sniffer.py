from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        protocol = "Other"

        if packet.haslayer(TCP):
            protocol = "TCP"

        elif packet.haslayer(UDP):
            protocol = "UDP"

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        print("=" * 70)
        print(f"Source IP      : {src}")
        print(f"Destination IP : {dst}")
        print(f"Protocol       : {protocol}")
        print(f"Packet Summary : {packet.summary()}")

        if packet.haslayer(TCP):
            payload = bytes(packet[TCP].payload)
            if payload:
                print("Payload:")
                print(payload)

print("Starting Packet Sniffer...")
print("Press Ctrl+C to Stop")

sniff(prn=process_packet, store=False)