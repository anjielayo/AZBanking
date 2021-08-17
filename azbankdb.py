"""
Created on Tue Aug 06 13:16 2021

@author: Anjolaoluwa
Creating the AZBank database
"""

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS azbankdb")
cursor.execute("USE azbankdb")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS azbank_empusers(id INT(10) NOT NULL AUTO_INCREMENT, customer_id INT(10) NOT NULL, firstname VARCHAR(200), lastname VARCHAR(200), accountname VARCHAR(300), accountno BIGINT UNSIGNED, bvn BIGINT UNSIGNED, age INT(20), gender VARCHAR(50), marital_status VARCHAR(100), next_of_kin VARCHAR(300), address VARCHAR(500), amount DECIMAL(65,2), narration LONGTEXT, PRIMARY KEY(id,customer_id))")
cursor.execute("CREATE TABLE IF NOT EXISTS azbank_staff(id INT(10) NOT NULL AUTO_INCREMENT, staff_id VARCHAR (50) NOT NULL, name VARCHAR (200), password VARCHAR (100),PRIMARY KEY(id,staff_id))")
cursor.execute("CREATE TABLE IF NOT EXISTS azbank_regusers(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, userid VARCHAR (300), password VARCHAR (100), pin VARCHAR(4))")
cursor.execute("CREATE TABLE IF NOT EXISTS bill_vendors(id INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, vendor VARCHAR(100),accountno BIGINT UNSIGNED)")
conn.commit()
conn.close()
