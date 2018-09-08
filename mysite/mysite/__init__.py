import pymysql
# py3不支持mysqldb
# 告诉Django用pymysql代替默认的MySQLDB 连接MySQL数据库
pymysql.install_as_MySQLdb()