from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import socket
import requests
import matplotlib.pyplot as plt
import numpy as np
import bs4
import pandas as pd

res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
soup = bs4.BeautifulSoup(res.text, 'lxml')
quote = soup.find('img', {"class":"p-qotd"})
text = 'Quote of the day is : ' + quote['alt']



try:
	socket.create_connection( ("www.google.com", 80))
	city = "Mumbai"
	a1 = "https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	data = res1.json()
	main = data['main']
	#print(main)
	temp = main['temp']
	#print("temp=", temp)
	temp1 = str(city)  + "    " +  str(temp)  + "   " +  str(main)

except OSError as e:
	print("check network", e)



def f1():
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()

def f4():
	st.delete(1.0,END)
	root.deiconify()
	vist.withdraw()
def f3():
	vist.deiconify()
	root.withdraw()
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("u r connected ")
		cursor=con.cursor()
		sql="select * from student_2020"
		cursor.execute(sql)
		data=cursor.fetchall()
		mdata=""
		for d in data:
			mdata=mdata+" rno = "+str(d[0])+"\t"+  " name = "+d[1]+"\t"+  " marks = "+str(d[2])+"\n"	
		st.insert(INSERT, mdata)
	except cx_Oracle.DatabaseError as e:
		print("Wrong Data ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("U r disconnected ")


def f5():
	import cx_Oracle
	con = None
	cursor=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "insert into student_2020 values('%d', '%s', '%d')"

		rno = entAddRno.get()
		if rno.isdigit() and int(rno)>0:
			rno=int(rno)
		else:
			messagebox.showerror("Error","Enter a valid rno")
			entAddRno.delete(0,END)
			entAddRno.focus()
			return

		name = entAddName.get()
		if name.isalpha() and len(name)>1:
			name=name
		else:
			messagebox.showerror("Error","Enter valid name(min 2 letters)")
			entAddName.delete(0,END)
			entAddname.focus()
			return

		marks = entAddMarks.get()
		if marks.isdigit() and int(marks)>0 and int(marks)<101:
			marks=int(marks)
		else:
			messagebox.showerror("Error","Enter +ve marks(0-100)")
			entAddMarks.delete(0,END)
			entAddMarks.focus()
			return
		args = (rno, name, marks)

		cursor.execute(sql % args)

		msg=str(cursor.rowcount)+" records inserted "
		messagebox.showinfo("Successful", msg)
		entAddRno.delete(0, END)
		entAddName.delete(0, END)
		entAddMarks.delete(0, END)
		entAddRno.focus()
		entAddName.focus()
		entAddMarks.focus()
		con.commit()

	except ValueError:
		messagebox.showerror('Some Error there ')
		entAddRno.delete(0,END)
		entAddRno.focus()
		entAddName.delete(0,END)
		entAddName.focus()
		entAddMarks.delete(0,END)
		entAddMarks.focus()	

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)
		entAddRno.delete(0,END)
		entAddRno.focus()
		entAddName.delete(0,END)
		entAddName.focus()
		entAddMarks.delete(0,END)
		entAddmarks.focus()
		
		
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		

def f6():
	root.withdraw()
	udst.deiconify()

def f7():
	udst.withdraw()
	root.deiconify()

def f8():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("u r connected ")
		cursor=con.cursor()
		sql="update student_2020 set name='%s',marks=%d where rno=%d"
		rno=entUpdateRno.get()
		if rno.isdigit() and int(rno)>0:
			rno=int(rno)
		else:
			messagebox.showerror("Error","Enter a valid id")
			entUpdateRno.delete(0,END)
			entUpdateRno.focus()
			return

		name=entUpdateName.get()
		if name.isalpha() and len(name)>1:
			name=name
		else:
			messagebox.showerror("Error","Enter valid name (min 2 letters)")
			entUpdateName.delete(0,END)			
			entUpdateName.focus()
			return

		marks=entUpdateMarks.get()
		if marks.isdigit() and int(marks)>0 and int(marks)<101:
			marks=int(marks)
		else:
			messagebox.showerror("Error","Enter positive marks(0-100)")
			entUpdateMarks.delete(0,END)
			entUpdateMarks.focus()
			return

		
		args=(name,marks,rno)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+" records updated "
		messagebox.showinfo("Success", msg)
		entUpdateRno.delete(0,END)
		entUpdateRno.focus()
		entUpdateName.delete(0,END)
		entUpdateName.focus()
		entUpdateMarks.delete(0,END)
		entUpdateMarks.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)
		entUpdateRno.delete(0,END)
		entUpdateRno.focus()
		entUpdateName.delete(0,END)
		entUpdateName.focus()
		entUpdateMarks.delete(0,END)
		entUpdateMarks.focus()
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
			print("U r disconnected ")



def f9():
	root.withdraw()
	dldst.deiconify()

def f10():
	dldst.withdraw()
	root.deiconify()

def f11():
	import cx_Oracle
	con = None
	cursor=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		sql = "delete from student_2020 where rno=%s"
		rno = entDeleteRno.get()
		if rno.isdigit() and int(rno)>0:
			args=(rno)
			cursor.execute(sql%args)
			con.commit()
		else:
			messagebox.showerror("Error","Enter a valid rno")
			entDeleteRno.delete(0,END)
			entDeleteRno.focus()
			return
		
		msg=str(cursor.rowcount)+" records deleted "
		messagebox.showinfo("Successful", msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
		
		
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
		
def f12():
	import cx_Oracle
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor = con.cursor()
		cursor.execute("select count(*) from student_2020 ")
		for row in cursor:
			totalstudents=row[0]
		t=np.arange(totalstudents)
		cursor.execute("SELECT * FROM(SELECT rno, name, marks FROM student_2020 ORDER BY marks DESC) WHERE ROWNUM <=3 ")
		#cursor.execute(sql)
		#con.commit()

		rno=[]
		name=[]
		marks=[]
		
		for row in cursor:
			rno.append(row[0])
			name.append(row[1])
			marks.append(row[2])
		bar_width=0.4
		t = np.arange(len(name))
		plt.bar(t,marks,bar_width,label = "Marks", color = 'g', alpha=0.8)
		plt.xticks(t,name,fontsize = 10)
		plt.xlabel("Name")
		plt.ylabel("Marks")
		plt.title("Top 3 Student's Marks")
		plt.legend()
		plt.grid()
		
		xs=[x for x in range(0,totalstudents)]
		for x,y in zip(xs,marks):
			plt.annotate(marks[x],(x-bar_width/2,y))

		plt.show()

	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)




root = Tk()
root.title("Student Management System ")
root.geometry("500x400+200+200")

lbltitle=Label(root,text="--- Student Management System ---",font=("arial", 18, 'bold'))

btnAdd = Button(root, text="Add", font=("arial", 18, 'bold'),width=10, command=f1)
btnView = Button(root, text="View", font=("arial", 18, 'bold'),width=10, command=f3)
btnUpdate = Button(root, text="Update", font=("arial", 18, 'bold'),width=10, command=f6)
btnDelete = Button(root, text="Delete", font=("arial", 18, 'bold'),width=10, command=f9)
lblQuote = Label(root,text = text, font=("arial", 18, 'bold'))
lblTemperature = Label(root,text = temp1, font=("arial", 18, 'bold'))
btnGraph = Button(root, text="Graph", font=("arial", 18, 'bold'),width=20, command=f12)


btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
lblQuote.pack(pady=10)
lblTemperature.pack(pady=10)
btnGraph.pack(pady=10)


adst = Toplevel(root)
adst.title("Add Student.")
adst.geometry("500x400+200+200")
adst.withdraw()

lblAddRno = Label(adst, text="enter rno", font=("arial",18,'bold') )
entAddRno = Entry(adst, bd=10, font=("arial", 18, 'bold'))

lblAddName = Label(adst, text="enter name", font=("arial",18,'bold') )
entAddName = Entry(adst, bd=10, font=("arial", 18, 'bold'))

lblAddMarks = Label(adst, text="enter marks", font=("arial",18,'bold') )
entAddMarks = Entry(adst, bd=10, font=("arial", 18, 'bold'))
btnAddSave = Button(adst, text="Save" , font=("arial", 18,'bold'), command=f5)
btnAddBack = Button(adst, text="Back" , font=("arial", 18, 'bold'), command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)



vist = Toplevel(root)
vist.title("View Student.")
vist.geometry("500x400+200+200")
vist.withdraw()

st = scrolledtext.ScrolledText(vist, width=50, height=10,font=("arial", 14, 'italic'))
btnViewBack = Button(vist, text="Back",font=("arial", 18, 'bold') , command=f4)
st.pack(pady=10)
btnViewBack.pack(pady=10)

udst = Toplevel(root)
udst.title("Update Student.")
udst.geometry("500x400+200+200")
udst.withdraw()

lblUpdateRno = Label(udst, text="enter rno", font=("arial",18,'bold') )
entUpdateRno = Entry(udst, bd=10, font=("arial", 18, 'bold'))
lblUpdateName = Label(udst, text="enter name", font=("arial",18,'bold') )
entUpdateName = Entry(udst, bd=10, font=("arial", 18, 'bold'))
lblUpdateMarks = Label(udst, text="enter marks", font=("arial",18,'bold') )
entUpdateMarks = Entry(udst, bd=10, font=("arial", 18, 'bold'))
btnUpdateSave = Button(udst, text="Save" , font=("arial", 18,'bold'), command=f8)
btnUpdateBack = Button(udst, text="Back" , font=("arial", 18, 'bold'), command=f7)

lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
lblUpdateMarks.pack(pady=10)
entUpdateMarks.pack(pady=10)
btnUpdateSave.pack(pady=10)
btnUpdateBack.pack(pady=10)


dldst = Toplevel(root)
dldst.title("Delete Student.")
dldst.geometry("500x400+200+200")
dldst.withdraw()

lblDeleteRno = Label(dldst, text="enter rno", font=("arial",18,'bold') )
entDeleteRno = Entry(dldst, bd=10, font=("arial", 18, 'bold'))
btnDeleteSave = Button(dldst, text="Save" , font=("arial", 18,'bold'), command=f11)
btnDeleteBack = Button(dldst, text="Back" , font=("arial", 18, 'bold'), command=f10)

lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDeleteSave.pack(pady=10)
btnDeleteBack.pack(pady=10)

graphst = Toplevel(root)
graphst.title("Graph of top 3 students")
graphst.geometry("500x400+200+200")
graphst.withdraw()





root.mainloop()









