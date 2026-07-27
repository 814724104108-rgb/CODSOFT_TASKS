from scapy.all import sniff
from scapy.layers.inet import IP, TCP

packet_count = {}

def detect(packet):
    if packet.haslayer(IP):
        src = packet[IP].src

        packet_count[src] = packet_count.get(src, 0) + 1

        print(f"Source: {src} | Total Packets: {packet_count[src]}")

        # Simple detection rule
        if packet_count[src] > 20:
            print("=" * 60)
            print("⚠ ALERT: Suspicious Activity Detected!")
            print(f"Source IP: {src}")
            print(f"Packets Sent: {packet_count[src]}")
            print("=" * 60)

print("Starting Network Intrusion Detection System...")
print("Press Ctrl+C to Stop")

sniff(prn=detect, store=False)