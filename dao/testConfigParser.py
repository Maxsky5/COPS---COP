# -*-coding: utf-8-*-
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("../config.ini")

host = config.get('database', 'host')
db_name = config.get('database', 'dbname')
username = config.get('database', 'username')
password = config.get('database', 'password')
port = config.get('database', 'port')

print host