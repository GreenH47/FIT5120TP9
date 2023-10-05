#!/bin/bash
apt-get update
apt-get install -y docker.io nginx apache2-utils

usermod -aG docker ubuntu

# Start Nginx service
service nginx start

# Configure Nginx for reverse proxy with basic authentication
cat > /etc/nginx/sites-available/default <<- EOF
server {
    listen 80;
    listen [::]:80 default_server;

    server_name wasteisland.me;

    location / {
        # auth_basic "Restricted Area";
        # auth_basic_user_file /etc/nginx/.htpasswd;
        proxy_pass http://localhost:8080;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}

server {
    listen 80;
    listen [::]:80;

    server_name iteration2.wasteisland.me;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}

EOF

# Enable the Nginx configuration
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Restart Nginx to apply the new configuration
service nginx restart

apt-get update
apt-get install apache2-utils

# Pull and run the Docker image
# for default server (you can replace it with your own image)
docker run --name naughty_burnell -d -p 8080:5000 greenh47/wasteisland:it3

# backup server for iteration2 (for iteration2 instance only)
# (you can replace it with your own image)
docker run --name it2 -d -p 5000:80 greenh47/wasteisland:it2
