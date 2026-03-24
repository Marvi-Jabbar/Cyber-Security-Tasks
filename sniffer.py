from scapy.all import sniff, IP

# This function runs every time a packet is captured
def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"Captured: {src_ip} -> {dst_ip} | Protocol: {proto}")

print("Sniffer is running... Press Ctrl+C to stop.")

# Start sniffing (requires sudo/root)
sniff(filter="ip", prn=process_packet, store=False)