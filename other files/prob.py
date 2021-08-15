#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 05, 2021 03:22:38 PM WAT  platform: Windows NT
import re
import shelve
import socket
import sys
import threading
import time
from datetime import datetime
from tkinter import messagebox

import mysql.connector
import socket
import json  # used to move data in complex forms such as lists and dictionaries
import random

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

from PIL import Image, ImageTk

import Bank_App_updated_support
import os.path


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Az_Bank(root)
    Bank_App_updated_support.init(root, top)
    root.mainloop()


w = None


def create_Az_Bank(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Az_Bank(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Az_Bank(w)
    Bank_App_updated_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Az_Bank():
    global w
    w.destroy()
    w = None


class Emp_Frame:
    pass


class Az_Bank(tk.Tk):
    def __init__(self, *args, **kwargs):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.container.place(relx=0.348, rely=0.588, height=24, width=77)
        self.current_frame = None
        self.show_frame(Emp_Frame)

    def show_frame(self, new_frame_class):
        self.refresh()
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = new_frame_class(self.container, controller=self)
        self.current_frame.place(relx=0.183, rely=0.042, relheight=0.885
                                 , relwidth=0.575)
        self.current_frame.configure(relief='groove')
        self.current_frame.configure(borderwidth="2")
        self.current_frame.configure(relief="groove")
        self.current_frame.configure(background="#d9d9d9")



    # ----------------------STAFF LOGIN METHOD-------------------------------#
    def staff_login(self):
        time.sleep(0.2)
        username = self.Emp_Username.get()
        password = self.Emp_Password.get()
        data = self.s.recv(1024)
        # print(bytes.decode(data))
        message = [username, password, "stafflogin"]
        self.s.send(str.encode(json.dumps(message)))
        resp = self.s.recv(1024)
        result = json.loads(bytes.decode(resp))
        # print(result)

        if not result:
            messagebox.showerror("Error", "Invalid username or password!")
            Az_Bank(root)

        else:
            messagebox.showinfo("", "Login Successful!")
            text = self.Emp_Username.get()
            self.cursor.execute("SELECT name FROM azbank_staff WHERE staff_id={}".format(text))
            resp = self.cursor.fetchall()
            # print("My response")
            # print(resp)
            user = str(resp[0])
            user = user.strip("',()")
            print(user)
            self.emplabel.configure(text=user)
            self.show_frame(self.Emp_dash)

    # ----------------------STAFF CREATE ACCOUNT METHOD-------------------------------#
    def staff_reg(self):
        time.sleep(0.2)

        submitOk = True
        # custid = self.Customer_ID.get()
        fname = self.First_name.get()
        lname = self.Last_name.get()
        # accno = self.Acc_Aname.get()
        # bvn = self.Acc_BVN.get()
        # amt = self.Amount.get()

        fname_pattern = "\\w+\\S"
        fname_result = re.match(fname_pattern, fname)

        if not fname_result:
            submitOk = False
            messagebox.showerror("Error", "Invalid first name!")

        lname_pattern = "\\w+\\S"
        lname_result = re.match(lname_pattern, lname)

        if not lname_result:
            submitOk = False
            messagebox.showerror("Error", "Invalid last name!")

        # bvn_pattern = "\\d{11}"
        # bvn_result = re.match(bvn_pattern, bvn)
        #
        # if not bvn_result:
        #     submitOk = False
        #     messagebox.showerror("Error", "Invalid BVN details")

        if submitOk is False:
            # messagebox.showerror("Error", "")
            return False

        else:
            custid = random.randint(0, 1111111111)
            accno = random.randint(1000000000, 9999999999)
            bvn = random.randint(11111111111, 90000000000)
            messagebox.showinfo("Success", "Customer Registered Successfully!")
            self.cursor.execute("SELECT accountno,bvn from azbank_empusers")
            respid = self.cursor.fetchall()
            print("The respid is")
            print(respid)

            global newaccno
            global newbvn
            if accno or bvn in respid:
                newaccno = accno + 1
                newbvn = bvn + 1
            else:
                pass

            message = [custid, fname, lname, fname + lname, newaccno, newbvn, '0000', 50000, "empreg"]
            print("The message")
            print(message)
            self.s.send(str.encode(json.dumps(message)))
            # data = self.s.recv(1024)
            # message_json = bytes.decode(data)
            # getter = json.loads(message_json)
            # print("The response")
            # print(getter)

    # ----------------------VALIDATION FOR CUSTOMER LOGIN METHOD-------------------------------#
    def custvalidate(self):
        time.sleep(0.2)
        user = self.hp_login_entry.get()
        password = self.hp_password_entry.get()
        data = self.s.recv(1024)
        # print(bytes.decode(data))
        message = [user, password, "custlogin"]
        self.s.send(str.encode(json.dumps(message)))
        resp = self.s.recv(1024)
        result = json.loads(bytes.decode(resp))
        print(result)
        if not result:
            messagebox.showerror("Error", "Invalid username or password!")
            Az_Bank(root)
        else:
            messagebox.showinfo("", "User Login Successful!")
            self.show_frame(self.Welcome_Page)

    # ----------------------DELETE ACCOUNT METHOD-------------------------------#
    def delete_account(self):
        time.sleep(0.2)
        custid = self.del_Cust_id.get()
        accno = self.del_Acc_num.get()
        self.cursor.execute(
            "SELECT * FROM azbank_empusers WHERE customer_id='{}' AND accountno='{}'".format(custid, accno))
        record = self.cursor.fetchone()
        print("The record is")
        print(record)
        self.cursor.execute("DELETE FROM azbank_empusers WHERE customer_id = '{}'".format(custid))
        self.conn.commit()
        # result = self.cursor.fetchall()
        # print(result)
        # message = [custid, accno, "delete"]
        # self.s.send(str.encode(json.dumps(message)))
        # resp = self.s.recv(1024)
        # print(resp)
        # result = json.loads(bytes.decode(resp))
        # print(result)
        if record:
            messagebox.showinfo("", "Account Successfully Deleted!")
        else:
            messagebox.showerror("", "User Does Not Exist!")

    # ----------------------LOAD ACCOUNT METHOD-------------------------------#
    def load_account(self):
        time.sleep(0.2)
        submitOk = True

        account_no = self.Acc_Number.get()
        newacc = float(account_no)

        amount = self.load_amount.get()
        add1 = float(amount)
        narration = "\nCredit of {} to {} on".format(amount, account_no)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        newnarration = narration + " " + dt_string + "."

        # self.cursor.execute("SELECT amount FROM azbank_empusers WHERE accountno='{}'".format(account_no))
        # select_amt = self.cursor.fetchone()
        # print("Selected amount from database is")
        # print(select_amt)
        # add2 = str(select_amt[0])
        # add2=add2.strip("',()'")
        # add2=float(add2)
        #
        # newamount = add1 + add2
        # print("The amount to send to process")
        # print(newamount)

        accno_pattern = "\\d+"
        accno_result = re.match(accno_pattern, account_no)
        if not accno_result:
            submitOk = False
            messagebox.showerror("Error", "Invalid Account Number supplied")

        amount_pattern = "\\d+"
        amount_result = re.match(amount_pattern, amount)
        if not amount_result:
            submitOk = False
            messagebox.showerror("Error", "Enter a valid amount")

        if submitOk is False:
            return False
        else:
            message = [add1, newnarration, newacc, "empload"]
            print("The message to be sent is")
            print(message)
            self.s.send(str.encode(json.dumps(message)))
            resp = self.s.recv(1024)
            result = json.loads(bytes.decode(resp))
            print("Result from process")
            print(result)
            messagebox.showinfo("", "Account {} loaded successfully with ₦{}!".format(account_no, amount))

    # ----------------------EMPLOYEE CHECKING CUSTOMER ACCOUNT INFO METHOD-------------------------------------------------#
    def acc_details(self):
        contain = []
        accno = self.info_Acc_Num.get()
        print(accno)
        message = [accno, "empinfo"]
        self.s.send(str.encode(json.dumps(message)))
        resp = self.s.recv(1024)
        result = json.loads(bytes.decode(resp))

        print("Result from process")
        print(result)
        if len(result) == 0:
            messagebox.showerror("Error", "Account number does not exist!")
        else:
            messagebox.showinfo("", "Account details successfully retrieved!")
            for k in result[0]:
                # self.info_list.insert(tk.END, f"id:{k[0]}\ncustomer id:{k[1]}\nfirstname:{k[2]}\nlastname:{k[3]}\naccountname:{k[4]}\naccountno:{k[5]}\nbvn:{k[6]}\npassword:{k[7]}\namount:{k[8]}\nstatement:{k[9]}\n")
                print(k)
                contain.append(k)
            names = ["id", "customer id", "first name", "last name", "account name", "account no", "bvn",
                     "password",
                     "amount", "statement"]
            j = 0
            for i in names:
                self.info_list.insert(tk.END, f"{i}:{contain[j]}")
                j += 1

    # --------------------------USER LOGOUT METHOD-------------------------
    def user_logout(self):
        time.sleep(0.3)
        if messagebox.askquestion("Sign Out", "Do you want to Log out?") == "yes":
            Az_Bank(root)

    # def show_startframe(self):
    #     self.show_frame(self.Welcome_Page)

    # def showstartframe_thread(self, event):
    #     ssf_thread = threading.Thread(target=self.show_startframe)
    #     ssf_thread.daemon = True
    #     ssf_thread.start()

    def refresh(self):
        self.Emp_Username.delete(0, tk.END)
        self.Emp_Password.delete(0, tk.END)

    # def reload(self):
    #     self.destroy
    #     self.__init__()

    def showempframe_thread(self, event):
        sef_thread = threading.Thread(target=self.show_empframe)
        sef_thread.daemon = True
        sef_thread.start()

    # ----------------------STAFF LOGIN THREAD-------------------------------#
    def stafflogin_thread(self, event):
        staff_thread = threading.Thread(target=self.staff_login)
        staff_thread.daemon = True
        staff_thread.start()

    # ----------------------STAFF ACCOUNT CREATION THREAD-------------------------------#
    def staffreg_thread(self, event):
        sac_thread = threading.Thread(target=self.staff_reg)
        sac_thread.daemon = True
        sac_thread.start()

    # ----------------------VALIDATION FOR CUSTOMER LOGIN THREAD-------------------------------#
    def custvalidate_thread(self, event):
        cv_thread = threading.Thread(target=self.custvalidate)
        cv_thread.daemon = True
        cv_thread.start()

    # ----------------------DELETE ACCOUNT THREAD-------------------------------------------------#
    def deleteaccount_thread(self, event):
        deletion_thread = threading.Thread(target=self.delete_account)
        deletion_thread.daemon = True
        deletion_thread.start()

    # ----------------------LOAD ACCOUNT THREAD-------------------------------------------------#
    def loadaccount_thread(self, event):
        load_thread = threading.Thread(target=self.load_account)
        load_thread.daemon = True
        load_thread.start()

    # ----------------------EMPLOYEE CHECKING CUSTOMER ACCOUNT INFO THREAD-------------------------------------------------#
    def accdetails_thread(self, event):
        ad_thread = threading.Thread(target=self.acc_details)
        ad_thread.daemon = True
        ad_thread.start()

    def userlogout_thread(self, event):
        logout_thread = threading.Thread(target=self.user_logout)
        logout_thread.daemon = True
        logout_thread.start()



class Welcome_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Welcome_Page.place(relx=0.183, rely=0.042, relheight=0.885
                                , relwidth=0.575)
        Welcome_Page.configure(relief='groove')
        Welcome_Page.configure(borderwidth="2")
        Welcome_Page.configure(relief="groove")
        Welcome_Page.configure(background="#ffffff")
        Welcome_Page.configure(highlightbackground="#d9d9d9")
        Welcome_Page.configure(highlightcolor="black")

        logo = tk.Label(self)
        logo.place(relx=0.345, rely=0.186, height=41, width=104)
        logo.configure(activebackground="#f9f9f9")
        logo.configure(activeforeground="black")
        logo.configure(background="#d9d9d9")
        logo.configure(disabledforeground="#a3a3a3")
        logo.configure(foreground="#000000")
        logo.configure(highlightbackground="#d9d9d9")
        logo.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "Azlogo3.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        logo.configure(image=_img0)
        logo.configure(text='''Label''')

        Enter = tk.Button(self)
        Enter.place(relx=0.287, rely=0.727, height=24, width=147)
        Enter.configure(activebackground="#ececec")
        Enter.configure(activeforeground="#000000")
        Enter.configure(background="#ff8000")
        Enter.configure(borderwidth="3")
        Enter.configure(disabledforeground="#a3a3a3")
        Enter.configure(font="-family {Verdana} -size 10 -weight bold")
        Enter.configure(foreground="#ffffff")
        Enter.configure(highlightbackground="#d9d9d9")
        Enter.configure(highlightcolor="black")
        Enter.configure(pady="0")
        Enter.configure(text='''Enter Here''')

        staff = tk.Button(self)
        staff.place(relx=0.548, rely=0.927, height=24, width=147)
        staff.configure(activebackground="#ececec")
        staff.configure(activeforeground="#000000")
        staff.configure(background="#0080c0")
        staff.configure(disabledforeground="#a3a3a3")
        staff.configure(font="-family {Segoe UI} -size 10")
        staff.configure(foreground="#ffffff")
        staff.configure(highlightbackground="#d9d9d9")
        staff.configure(highlightcolor="black")
        staff.configure(pady="0")
        staff.configure(text='''Staff? Sign In here.''')

        headingLabel_welcome = tk.Label(self)
        headingLabel_welcome.place(relx=0.174, rely=0.351, height=41
                                        , width=232)
        headingLabel_welcome.configure(background="#ffffff")
        headingLabel_welcome.configure(cursor="arrow")
        headingLabel_welcome.configure(disabledforeground="#a3a3a3")
        headingLabel_welcome.configure(font="-family {Verdana} -size 15 -weight bold")
        headingLabel_welcome.configure(foreground="#000000")
        headingLabel_welcome.configure(text='''Welcome to AZ Bank''')

        mottolabel_welcome = tk.Label(self)
        mottolabel_welcome.place(relx=0.258, rely=0.492, height=21
                                      , width=183)
        mottolabel_welcome.configure(activebackground="#f9f9f9")
        mottolabel_welcome.configure(activeforeground="black")
        mottolabel_welcome.configure(background="#ffffff")
        mottolabel_welcome.configure(disabledforeground="#a3a3a3")
        mottolabel_welcome.configure(font="-family {Verdana} -size 9")
        mottolabel_welcome.configure(foreground="#000000")
        mottolabel_welcome.configure(highlightbackground="#d9d9d9")
        mottolabel_welcome.configure(highlightcolor="black")
        mottolabel_welcome.configure(text='''Home of convenient banking.''')





        






app = Az_Bank()
app.mainloop()