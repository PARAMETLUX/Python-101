from tkinter import *
from tkinter import ttk #theme ของ tk
from tkinter import messagebox #ทำการเรียก function เเสดงผลกล่องข้อความ

#######################CSV#######################

import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data

#######################CSV#######################

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #การกำหนดชื่อของโปรแกรม
GUI.geometry('500x500') #การกำหนดขนาดของหน้าต่างโปรแกรม ก*ย

L1 = Label(GUI,text='โปรแกรมบันทึกข้อมูล เวอร์ชั่น 0',font=('Angsana New',30),fg='blue')
L1.place(x=70,y=0)

def Button1(): #การสร้างกล่องข้อความหลังจากทำการกดปุ่ม
    text = 'การบันทึกสำเร็จเเล้วครับ'
    messagebox.showinfo('บันทึกสำเร็จ',text)
FB1 = Frame(GUI)
FB1.place(x=100,y=300)
B1 = ttk.Button(FB1,text='บันทึก',command=Button1) #สร้างตัวเเปรของปุ่ม
B1.pack(ipadx=3,ipady=3) #เเสดงปุ่มบนหน้าต่าง (อยู่กึ่งกลางข้างบนสุด)


def Button2():
    text2 = 'ยกเลิกข้อมูลเสร็จสิ้น'
    messagebox.showwarning('การยกเลิกเสร็จสิ้น',text2)
FB2 = Frame(GUI)#กรอบที่ใช้เก็บ ปุ่ม ที่สร้างทำให้ปุ่มสามารถปรับขนาดได้
FB2.place(x=200,y=300)
B2 = ttk.Button(FB2,text='ยกเลิก',command=Button2) #สร้างตัวเเปรของปุ่ม
B2.pack(ipadx=3,ipady=3)

def Button3():
    text3 = 'ล้างข้อมูลเสร็จสิ้น'
    messagebox.showerror('การล้างข้อมูลเสร็จสิ้น',text3)
FB3 = Frame(GUI)
FB3.place(x=300,y=300)
B3 = ttk.Button(FB3,text='ล้างข้อมูล',command=Button3)
B3.pack(ipadx=3,ipady=3)

#######################section right#######################
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=100,y=100)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวเเปร v_data มาใช้งาน
    text = [data]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B1 = ttk.Button(LF1,text='บันทึก',command=SaveData) #ผูก function csv กับปุ่ม Button 1
B1.pack(ipadx=3,ipady=3) #เเสดงปุ่มบนหน้าต่าง (อยู่กึ่งกลางข้างบนสุด)

GUI.mainloop()
