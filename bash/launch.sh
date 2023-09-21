#!/bin/bash
apt-get update
apt-get install -y docker.io nginx
usermod -aG docker ubuntu

# Start Nginx service
service nginx start

# Configure Nginx for reverse proxy
cat > /etc/nginx/sites-available/default <<- EOF
server {
    listen 80;
    listen [::]:80 default_server;

    # root /var/www/html;
    # index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

# Enable the Nginx configuration
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Restart Nginx to apply the new configuration
service nginx restart

# Pull and run the Docker image
docker run --name naughty_burnell -d -p 8080:80 greenh47/wasteisland:it2
