sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/gunicorn.conf.py /etc/gunicorn.d/test.py

