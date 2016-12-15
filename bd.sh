sudo /etc/init.d/mysql restart
mysql -uroot -e "DROP DATABASE tt";
mysql -uroot -e "CREATE DATABASE tt CHARACTER SET=UTF8";
mysql -uroot -e "DROP USER 'ADMIN'@'LOCALHOST'";
mysql -uroot -e "CREATE USER 'ADMIN'@'LOCALHOST'";
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'ADMIN'@'LOCALHOST'";
mysql -uroot -e "FLUSH PRIVILEGES";


