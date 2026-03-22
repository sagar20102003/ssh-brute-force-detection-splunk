# Detailed Setup Guide

## Prerequisites
- VirtualBox/VMware installed
- 8GB RAM minimum
- 40GB free disk space

## Step 1: Target Server Setup (Ubuntu 22.04)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install SSH
sudo apt install openssh-server -y

# Create test users
sudo useradd -m admin
sudo useradd -m rootbackup
sudo useradd -m testuser

# Set passwords
echo "admin:Password123" | sudo chpasswd
echo "rootbackup:Welcome1" | sudo chpasswd

# Enable verbose logging
sudo sed -i 's/#LogLevel INFO/LogLevel VERBOSE/' /etc/ssh/sshd_config
sudo systemctl restart ssh

## Step 2: Splunk Installation

# Download Splunk
wget -O splunk.deb 'https://download.splunk.com/products/splunk/releases/9.0.4/linux/splunk-9.0.4-de405f4a7979-linux-2.6-amd64.deb'

# Install
sudo dpkg -i splunk.deb

# Start Splunk
sudo /opt/splunk/bin/splunk start --accept-license
# Create admin password when prompted

# Add SSH log monitoring
sudo /opt/splunk/bin/splunk add monitor /var/log/auth.log -index main -sourcetype linux_secure

## Step 3: Attacker Setup (Kali Linux)

# Install tools
sudo apt install hydra metasploit-framework -y

# Create wordlist
cat > passwords.txt << EOF
123456
password
admin
Password123
EOF

## Step 4: Launch Attack

# Replace with your Ubuntu IP
hydra -l admin -P passwords.txt ssh://192.168.1.50