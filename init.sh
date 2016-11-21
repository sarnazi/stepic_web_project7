sudo ln -sf /home/box/web/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/gunicorn.conf /etc/init.d/test
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart -c hello.py hello:application 

