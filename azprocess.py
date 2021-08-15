# -*- coding: utf-8 -*-
"""
Created on Tue Aug 06 13:10 2021

@author: Anjolaoluwa
Server script to handle user authentication requests
"""
import shelve
import threading
from tkinter import messagebox

import mysql.connector
import socket
import json  # used to move data in complex forms such as lists and dictionaries
import random


class processServer(threading.Thread):
    def __init__(self, client, addr):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.conn = mysql.connector.connect(host="localhost", database="azbankdb", user="root", password="")
        self.cursor = self.conn.cursor(buffered=True)

    def run(self):
        myclient = threading.local()
        myclient.client = self.client
        myclient.addr = self.addr
        print("Accepted connection from ", myclient.addr)
        # myclient.client.send(str.encode("Welcome to my server!"))

        while True:
            data = client.recv(1024)
            message = json.loads(bytes.decode(data))

            if "stafflogin" in message:
                message.remove("stafflogin")
                self.cursor.execute(
                    "SELECT * FROM azbank_staff WHERE staff_id='{}' AND password='{}'".format(*message))
                resp = self.cursor.fetchall()
                print("Sending employee login response...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()

            elif "empreg" in message:
                message.remove("empreg")
                # print("The message")
                print(message)
                self.cursor.execute(
                    "INSERT INTO azbank_empusers(customer_id,firstname,lastname,accountname,accountno,bvn,age,gender,marital_status,next_of_kin,address,password,amount) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        *message))
                self.cursor.execute("SELECT * from azbank_empusers ORDER BY id DESC LIMIT 1")
                resp = self.cursor.fetchall()
                print("Sending registration response...")
                print("The response")
                print(type(resp))
                print(resp)
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()

            # elif "custlogin" in message:
            #     message.remove("custlogin")
            #     self.cursor.execute(
            #         "SELECT * FROM azbank_empusers WHERE accountno='{}' AND password='{}'".format(*message))
            #     resp = self.cursor.fetchall()
            #     print("Sending customer login response...")
            #     print(resp)
            #     self.client.send(str.encode(json.dumps(resp)))
            #     self.conn.commit()

            elif "empload" in message:
                message.remove("empload")
                print("Message received from azabnk is")
                print(message)
                self.cursor.execute(
                    "UPDATE azbank_empusers SET amount =amount+'{}',narration=CONCAT(narration,' {}') WHERE accountno='{}'".format(
                        *message))
                self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno='{}'".format(message[2]))
                resp = self.cursor.fetchall()
                print("Loading the customer account...")
                print(resp)
                print(type(resp))
                self.client.send(str.encode(json.dumps(resp)))
                # print(self.cursor.rowcount, "Rows affected")
                self.conn.commit()

            # elif "empinfo" in message:
            #     message.remove("empinfo")
            #     print("Message received from azabnk is")
            #     print(message)
            #     self.cursor.execute(
            #         "SELECT id,customer_id,firstname,lastname,accountname,accountno,bvn,amount,narration FROM azbank_empusers where accountno='{}'".format(
            #             *message))
            #     resp = self.cursor.fetchall()
            #     print("Account information...")
            #     print(resp)
            #     self.client.send(str.encode(json.dumps(resp)))
            #     self.conn.commit()

            elif "check_account" in message:
                message.remove("check_account")
                # print(message)
                self.cursor.execute("SELECT accountno FROM azbank_empusers")
                resp = self.cursor.fetchall()
                # print(resp)
                altern = []
                for i in resp:
                    item = list(i)
                    altern += item
                # print(type(altern[0]))
                # print(resp[0])
                # print("Types")
                # print(type(resp[0]))
                # print(type(message[0]))

                if message[0] in altern:
                    print("Account number exists in employee database")
                    self.cursor.execute("SELECT userid FROM azbank_regusers")
                    collect = self.cursor.fetchall()
                    # print("collect is")
                    # print(collect)
                    colist = []
                    cointlist = []
                    for i in collect:
                        thing = list(i)
                        colist += thing
                    # print("colist is")
                    # print(colist)
                    # print(type(colist[0]))
                    for j in colist:
                        possess = int(j)
                        cointlist.append(possess)
                    # print("cointlist is")
                    # print(cointlist)
                    # print(type(cointlist[0]))
                    if message[0] in cointlist:
                        print("Account already exists")
                        msg = "exist"
                    else:
                        # self.cursor.execute(
                        #     "INSERT INTO azbank_regusers(userid) SELECT accountno FROM azbank_empusers WHERE accountno='{}'".format(
                        #         *message))
                        self.cursor.execute("SELECT accountno FROM azbank_empusers where accountno={}".format(*message))
                        result = self.cursor.fetchall()
                        print(f"result is {result}")
                        if result:
                            msg = "success"
                        else:
                            msg = "failed"
                            print("Account does not exist")
                else:
                    msg = "failed"

                self.client.send(str.encode(msg))
                print(msg)

                # tbs=str.encode(json.dumps(result))
                # print(tbs)
                self.conn.commit()

            elif "userlogin" in message:
                message.remove("userlogin")
                print("Message received from azbank is")
                print(message)
                self.cursor.execute(
                    "SELECT * from azbank_regusers WHERE userid='{}' and password='{}'".format(*message))
                resp = self.cursor.fetchall()
                print("Sending login response...")
                self.client.send(str.encode(json.dumps(resp)))
                self.conn.commit()

            elif "airtime" in message:
                message.remove("airtime")
                print(f"type of message {type(message)}")
                print(f"type of message0 {type(message[0])}")
                self.cursor.execute("SELECT pin FROM azbank_regusers WHERE userid='{}'".format(message[0]))
                resp=self.cursor.fetchone()
                str_resp = str(resp)
                str_resp = str_resp.strip("\',()")
                if message[4]==str_resp:
                    self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[0]))
                    result = self.cursor.fetchone()
                    result = str(result)
                    result = result.strip("\',()")
                    result = float(result)
                    newamount = result - message[2]
                    self.cursor.execute("UPDATE azbank_empusers SET amount='{}' WHERE accountno='{}'".format(
                                        newamount,message[0]))

                    self.client.send(str.encode("airsuccess"))
                else:
                    self.client.send(str.encode("airfail"))
                self.conn.commit()

            elif "quickairtime" in message:
                message.remove("quickairtime")
                print(f"type of message {type(message)}")
                print(f"type of message0 {type(message[0])}")
                self.cursor.execute("SELECT pin FROM azbank_regusers WHERE userid='{}'".format(message[0]))
                resp=self.cursor.fetchone()
                str_resp = str(resp)
                str_resp = str_resp.strip("\',()")
                if message[4]==str_resp:
                    self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[0]))
                    result = self.cursor.fetchone()
                    result = str(result)
                    result = result.strip("\',()")
                    result = float(result)
                    newamount = result - message[2]
                    self.cursor.execute("UPDATE azbank_empusers SET amount='{}' WHERE accountno='{}'".format(
                                        newamount,message[0]))

                    self.client.send(str.encode("quickairsuccess"))
                else:
                    self.client.send(str.encode("quickairfail"))
                self.conn.commit()

            elif "quickbills" in message:
                message.remove("quickbills")
                self.cursor.execute("SELECT pin FROM azbank_regusers WHERE userid='{}'".format(message[0]))
                resp = self.cursor.fetchone()
                str_resp = str(resp)
                str_resp = str_resp.strip("\',()")
                if message[3] == str_resp:
                    self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[0]))
                    result = self.cursor.fetchone()
                    result = str(result)
                    result = result.strip("\',()")
                    result = float(result)
                    newamount = result - message[2]
                    self.cursor.execute("UPDATE azbank_empusers SET amount={} WHERE accountno='{}'".format(newamount,message[0]))
                    self.client.send(str.encode("quickbillssuccess"))
                else:
                    self.client.send(str.encode("quickbillsfail"))
                self.conn.commit()

            elif "bills" in message:
                message.remove("bills")
                self.cursor.execute("SELECT pin FROM azbank_regusers WHERE userid='{}'".format(message[0]))
                resp = self.cursor.fetchone()
                str_resp = str(resp)
                str_resp = str_resp.strip("\',()")
                if message[3] == str_resp:
                    self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[0]))
                    result = self.cursor.fetchone()
                    result = str(result)
                    result = result.strip("\',()")
                    result = float(result)
                    newamount = result - message[2]
                    self.cursor.execute("UPDATE azbank_empusers SET amount={} WHERE accountno='{}'".format(newamount,message[0]))
                    self.client.send(str.encode("billssuccess"))
                else:
                    self.client.send(str.encode("billsfail"))
                self.conn.commit()

            elif "quicktransfer" in message:
                message.remove("quicktransfer")
                self.cursor.execute("SELECT pin FROM azbank_regusers WHERE userid='{}'".format(message[0]))
                resp = self.cursor.fetchall()
                str_resp = str(resp[0])
                str_resp = str_resp.strip("\',()")
                if message[3] == str_resp:
                    result = self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[0]))
                    result = self.cursor.fetchall()
                    result = str(result[0])
                    result = result.strip("\',()")
                    result = float(result)
                    newamount = result - message[2]

                    self.cursor.execute("UPDATE azbank_empusers SET amount={} WHERE accountno='{}'".format(newamount, message[0]))

                    self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[1]))
                    amt_post = self.cursor.fetchall()
                    amt_post = str(amt_post[0])
                    amt_post = amt_post.strip("\',()")
                    amt_post = float(amt_post)
                    cred_amount = amt_post + message[2]
                    self.cursor.execute(
                        "UPDATE azbank_empusers SET amount={} WHERE accountno='{}'".format(
                            cred_amount,message[1]))
                    self.client.send(str.encode("quicktransfersuccess"))
                else:
                    self.client.send(str.encode("quicktransferfail"))
                self.conn.commit()

            elif "transfer" in message:
                message.remove("transfer")
                self.cursor.execute("SELECT pin FROM azbank_regusers WHERE userid='{}'".format(message[0]))
                resp = self.cursor.fetchall()
                str_resp = str(resp[0])
                str_resp = str_resp.strip("\',()")
                if message[3] == str_resp:
                    result = self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[0]))
                    result = self.cursor.fetchall()
                    result = str(result[0])
                    result = result.strip("\',()")
                    result = float(result)
                    newamount = result - message[2]

                    self.cursor.execute("UPDATE azbank_empusers SET amount={} WHERE accountno='{}'".format(newamount, message[0]))

                    self.cursor.execute("SELECT amount from azbank_empusers WHERE accountno={}".format(message[1]))
                    amt_post = self.cursor.fetchall()
                    amt_post = str(amt_post[0])
                    amt_post = amt_post.strip("\',()")
                    amt_post = float(amt_post)
                    cred_amount = amt_post + message[2]
                    self.cursor.execute(
                        "UPDATE azbank_empusers SET amount={} WHERE accountno='{}'".format(
                            cred_amount,message[1]))
                    self.client.send(str.encode("transfersuccess"))
                else:
                    self.client.send(str.encode("transferfail"))
                self.conn.commit()

            # elif "delete" in message:
            #     message.remove("delete")
            #     print("The message")
            #     print(message)
            #     try:
            #         self.cursor.execute(
            #             "DELETE FROM azbank_empusers WHERE customer_id='{}'AND accountno='{}'".format(*message))
            #         self.cursor.execute(
            #                 "DELETE FROM azbank_regusers WHERE userid='{}'".format(message[1]))
            #         self.cursor.execute("SELECT * FROM azbank_empusers WHERE customer_id='{}' AND accountno='{}'".format(*message))
            #         resp = self.cursor.fetchone()
            #         self.client.send(str.encode(json.dumps(resp)))
            #     except:
            #         self.client.send(str.encode("alreadydel"))
            #     print("Sending delete account response...")
            #     print(resp)
            #
            #     self.conn.commit()


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
