#!/bin/bash

# Write the Nginx configuration to /etc/nginx/sites-available/default using heredoc
sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
# Default server configuration
server {
    listen 8080;  # Listen on port 8080 for incoming HTTP traffic
    listen [::]:8080;  # Listen on IPv6 for port 8080

    # Root directory for the server
    root /var/www/html;

    # Add index file to be served
    index index.html index.htm index.nginx-debian.html;

    server_name jtwp.app www.jtwp.app;

    # Reverse proxy to forward traffic to port 5000
    location / {
        proxy_pass http://localhost:5000;  # Forward requests to port 5000 on the same machine
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        try_files \$uri \$uri/ =404;
    }
}

# Redirect HTTP (non-SSL) to HTTPS
server {
    listen 80;
    listen [::]:80;

    server_name www.jtwp.app jtwp.app;

    if (\$host = www.jtwp.app) {
        return 301 https://\$host\$request_uri;
    }

    if (\$host = jtwp.app) {
        return 301 https://\$host\$request_uri;
    }

    return 404;  # Return 404 if the host is invalid
}
EOF

# Test the Nginx configuration
sudo nginx -t

# Check if the test was successful
if [ $? -eq 0 ]; then
    # Reload Nginx if configuration is valid
    sudo systemctl reload nginx
    echo "Nginx has been reloaded successfully with the new configuration."
else
    echo "Nginx configuration test failed. Please check the configuration for errors."
fi

