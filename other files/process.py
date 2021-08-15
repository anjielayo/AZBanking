# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:38:09 2021

@author: Anjolaoluwa
Server script to handle user authentication requests
"""
import shelve
import threading

import mysql.connector
import socket
import json  # used to move data in complex forms such as lists and dictionaries
import random
from datetime import date, datetime


class processServer(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.conn = mysql.connector.connect(host="localhost", database="commercedb", user="root", password="")
        self.cursor = self.conn.cursor()

    def run(self):
        myclient = threading.local()
        myclient.client = self.client
        myclient.addr = self.addr
        print("Accepted connection from ", myclient.addr)
        myclient.client.send(str.encode("Welcome to my server!"))

        while True:
            data = client.recv(1024)
            message = json.loads(bytes.decode(data))

            if "register" in message:
                message.remove("register")
                self.cursor.execute(
                    "INSERT INTO commerce_users (user_id,username,email,password,reg_status) VALUES('{}','{}','{}','{}','{}')".format(
                        *message))
                # * is for list, ** is for dictionary, acts like a spread operator
                self.cursor.execute("SELECT * from commerce_users ORDER BY id DESC LIMIT 1")
                # ORDER BY means sort by. DESC means sort serially in descending order and LIMIT the search to just
                # one row
                resp = self.cursor.fetchall()  # resp stands for response

                print("Sending registration response...")
                self.client.send(str.encode(json.dumps(resp)))
                # encodes the complex data type (list,dict,tuple) first in
                # form of json then in form of string
                #  json.loads() is for decoding json, json.dumps() is for encoding json
                #  bytes.decode() is for decoding string, str.encode() is for encoding string
                self.conn.commit()
                # client.close()

            elif "login" in message:
                message.remove("login")
                self.cursor.execute(
                    "SELECT * FROM commerce_users WHERE username='{}' AND password='{}'".format(*message))
                resp = self.cursor.fetchall()
                print("Sending login response...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()
                # client.close()
            # conn.close()

            elif "calculate" in message:
                dicts = {
                    'bag': 0,
                    'heels': 0,
                    'blouse': 0,
                    'shirt': 0,
                    'trousers': 0,
                    'jeans': 0,
                    'sneakers': 0,
                    'skirt': 0,
                    'socks': 0
                }
                self.cursor.execute("SELECT * FROM price")
                rows = self.cursor.fetchall()
                print(rows)
                for row in rows:
                    dicts[row[1]] = float(row[2])  # the price is in row[2] while meal is in row[1]
                    # eg dict['jeans']=2000.00

                self.client.send(str.encode(json.dumps(dicts)))
                self.conn.commit()
                # client.close()


            elif "transaction" in message:
                del message['transaction']
                trans = shelve.open("trans_info", flag="n")
                username = message['username']
                self.cursor.execute("SELECT user_id FROM commerce_users WHERE username='{}'".format(username))
                user_id = self.cursor.fetchone()
                # we use fetchone() because we only need one row since user_id is unique to each user
                message['user_id'] = user_id[0]

                for item in message:
                    trans[item] = message[item]
                trans.close()
                print("Sending transaction response...")
                self.client.send(str.encode(json.dumps(message)))
                self.conn.commit()


            elif "post" in message:
                newdicts = {}
                trans = shelve.open("trans_info")
                for item in trans:
                    newdicts[item] = trans[item]
                trans.close()
                user_id = newdicts['user_id']
                username = newdicts['username']
                transaction_date = datetime.now()
                trans_date = transaction_date.strftime("%Y-%m-%d %H:%M:%S")
                del newdicts['user_id']
                del newdicts['username']

                print(newdicts)

                for row in newdicts:
                    self.cursor.execute(
                        "INSERT INTO transaction (emp_id, employee, item, amount, date_purchase) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                            user_id, username, row, newdicts[row], trans_date))
                self.cursor.execute("SELECT * FROM transaction WHERE date_purchase = '{}'".format(trans_date))
                result = self.cursor.fetchall()
                print(f"The result is {result}")
                if not result:
                    msg = "success"
                else:
                    msg = "failed"
                self.client.send(str.encode(msg))
                self.conn.commit()





            elif "logout" in message:
                break


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8000
server.bind((host, port))
server.listen(5)

while True:
    print("Listening for a client...")
    client, addr = server.accept()
    client1 = processServer(client, addr)
    client1.start()
