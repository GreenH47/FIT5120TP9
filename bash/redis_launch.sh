#!/bin/bash

# Update packages and install Redis server
apt update
apt install -y redis-server awscli

# Set Redis password
sed -i 's/# requirepass foobared/requirepass 8479f1eb312d/' /etc/redis/redis.conf

# Enable Redis to listen on all interfaces
sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf

# Restart Redis service
systemctl restart redis-server

