"""
Created on Tue Jun  8 10:07:27 2021

@author: Anjolaoluwa
Creating my first MySQL database
"""

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS commercedb")
cursor.execute("USE commercedb")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS commerce_users(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT(10) NOT NULL, username VARCHAR(100),  email VARCHAR(100),password VARCHAR(100), reg_status CHAR(5))")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS price(id int(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, product VARCHAR(50), price decimal(10,2))")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS transaction (id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, emp_id INT(10) NOT NULL, employee VARCHAR(200),item VARCHAR(200),amount FLOAT,date_purchase DATE)")
conn.commit()
conn.close()
