# do all using puppet
exec {'/usr/bin/env sudo apt-get -y install nginx': }
exec {'/usr/bin/env echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html': }
exec {'/usr/bin/env sudo sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env echo "Ceci n\'est pas une page" | sudo tee /usr/share/nginx/html/custom_404.html': }
exec {'/usr/bin/env sudo sed -i "/server_name _;/a error_page 404 /custom_404.html;\nlocation = /custom_404.html {\nroot /usr/share/nginx/html;\ninternal;\n}\n" /etc/nginx/sites-available/default': }
exec {'/usr/bin/env sudo service nginx start': }
