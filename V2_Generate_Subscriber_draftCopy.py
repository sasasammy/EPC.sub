import tkinter	
import sys

#import tkMessageBox
from tkinter import messagebox

import time
from tkinter import *

master = Tk()
master.title("Generater Subscriber (EPC) - test module (use at your risk)")
master.geometry("350x170")
vosi = IntVar()
vqua = IntVar()

#define button events
def Generate():
    nn = input_nn.get()
    try:
        nos = int(input_nos.get())
        sv = int(input_sv.get())
        cc = int(input_cc.get())
    except ValueError:
        tkMessageBox.showwarning("Wrong Data Type!", "please insert the correct data type")
    else:
        start_time = time.time()
        fo = open("subscriber.ldif", "w")
        for id in range(sv, sv + nos):
            if vosi.get() and vqua.get():
                fo.write("dn:EPC-SubscriberId=%s%s,EPC-SubscribersName=EPC-Subscribers,applicationName=EPC-EpcNode,"
                         "nodeName=%s\nobjectClass:EPC-Subscriber\nEPC-OperatorSpecificInfo:Test_OSI:1\n\n"
                         "dn:EPC-Name=EPC-SubscriberQualification,EPC-SubscriberId=%s%s,"
                         "EPC-SubscribersName=EPC-Subscribers,"
                         "applicationName=EPC-EpcNode,nodeName=%s\n"
                         "EPC-SubscriberQualificationData:QosProfileId:100\n"
                         "objectClass:EPC-SubscriberQualification\n\n" % (str(cc), str(id), str(nn), str(cc), str(id), str(nn)))
            elif vqua.get() and not vosi.get():
                fo.write("dn:EPC-SubscriberId=%s%s,EPC-SubscribersName=EPC-Subscribers,applicationName=EPC-EpcNode,"
                         "nodeName=%s\nobjectClass:EPC-Subscriber\n\n"
                         "dn:EPC-Name=EPC-SubscriberQualification,EPC-SubscriberId=%s%s,"
                         "EPC-SubscribersName=EPC-Subscribers,"
                         "applicationName=EPC-EpcNode,nodeName=%s\n"
                         "EPC-SubscriberQualificationData:QosProfileId:100\n"
                         "objectClass:EPC-SubscriberQualification\n\n" % (cc, id, nn, cc, id, nn))
            elif not vqua.get() and vosi.get():
                fo.write(
                    "dn:EPC-SubscriberId=%s%s,EPC-SubscribersName=EPC-Subscribers,applicationName=EPC-EpcNode,nodeName=%s\n"
                    "objectClass:EPC-Subscriber\nEPC-OperatorSpecificInfo:Test_OSI:1\n\n" % (str(cc), str(id), str(nn)))
            else:
                fo.write(
                    "dn:EPC-SubscriberId=%s%s,EPC-SubscribersName=EPC-Subscribers,applicationName=EPC-EpcNode,nodeName=%s\n"
                    "objectClass:EPC-Subscriber\n\n" % (str(cc), str(id), str(nn)))
        fo.close()
        t = time.time() - start_time
        messagebox.showinfo("Congratulations", "Subscriber Ldif file generated! cost %s seconds" % t)
        sys.exit()

def Exit():
    sys.exit()

#define checkbox
ck_osi = Checkbutton(master, text='OSI', variable=vosi)
ck_osi.pack()
ck_osi.place(x=20, y=20)

ck_qua = Checkbutton(master, text='Qualification', variable=vqua)
ck_qua.pack()
ck_qua.place(x=90, y=20)

#define label
lsv = Label(master, text='Start MSISDN')
lsv.pack()
lsv.place(x=20, y=60)

lnos = Label(master, text='Num Of Subs')
lnos.pack()
lnos.place(x=175, y=60)

lcc = Label(master, text='Country Code')
lcc.pack()
lcc.place(x=20, y=90)

lnn = Label(master, text='Node Name')
lnn.pack()
lnn.place(x=175, y=90)

#define textbox
input_sv = Entry(master, width=10)
input_sv.pack()
input_sv.place(x=100, y=60)
input_sv.insert(0, '0')


input_nos = Entry(master, width=10)
input_nos.pack()
input_nos.place(x=255, y=60)
input_nos.insert(0, '1')

input_cc = Entry(master, width=10)
input_cc.pack()
input_cc.place(x=100, y=90)
input_cc.insert(0, '86')

input_nn = Entry(master, width=10)
input_nn.pack()
input_nn.place(x=255, y=90)
input_nn.insert(0, 'jambala')

#define buttons
button_run = Button(master,text="Run", width=8, command=Generate)
button_run.pack()
button_run.place(x=20, y=130)

button_exit = Button(master,text="Exit", width=8, command=Exit)
button_exit.pack()
button_exit.place(x=90, y=130)

mainloop()
