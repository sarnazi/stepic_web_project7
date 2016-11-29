sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE TEST3 CHARACTER SET=UTF8";
mysql -uroot -e "CREATE USER ADMIN@LOCALHOST IDENTIFIED BY '1'";
mysql -uroot -e "GRANT ALL PRIVILEGES ON TEST.* TO 'ADMIN@LOCALHOST'";
mysql -uroot -e "FLUSH PRIVILEGES";


