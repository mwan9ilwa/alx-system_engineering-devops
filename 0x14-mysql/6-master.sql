-- lets change the slave to be synchronized with the server
CHANGE MASTER TO
MASTER_HOST='107.23.94.198',
MASTER_USER='replica_user',
MASTER_PASSWORD='hbtn89',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=727;

START SLAVE;
