sudo /etc/init.d/mysql restart
mysql -uroot -e "DROP DATABASE bd6";
mysql -uroot -e "CREATE DATABASE bd6 CHARACTER SET=UTF8";
mysql -uroot -e "DROP USER 'ADMIN'@'LOCALHOST'";
mysql -uroot -e "CREATE USER 'ADMIN'@'LOCALHOST'";
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'ADMIN'@'LOCALHOST'";
mysql -uroot -e "FLUSH PRIVILEGES";


