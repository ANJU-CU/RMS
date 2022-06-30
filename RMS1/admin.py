 
from tkinter import*
from PIL import Image, ImageTk #pip install pilllow
from course import CourseClass

from result import resultClass

from tkinter import messagebox
import sqlite3
import os
#from . import version
#from collegeimages import*
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x790+0+0")
        self.root.title("Student Result Management System")
        self.root.config(bg="white")
        ###......icons.....
        self.logo_dash=ImageTk.PhotoImage(file="images/download.png")
       
        ###....title.....
        title=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash,font=('Britannic Bold',20),bg='#033054',fg="white").place(x=0,y=0,relwidth=1,height=80)
        #=====main manu======
        M_Frame=LabelFrame(self.root,text="Menus",font=('times new roman',16,"bold"),bg="white")
        M_Frame.place(x=10,y=70,width=1400,height=60)
        btn_course=Button(M_Frame,text="Course",font=("goudy old style",13,"bold"),bg="#0b5377",fg="white",cursor="hand2 ",command=self.add_course).place(x=20,y=5,width=100,height=40)
        
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",13,"bold"),bg="#0b5377",fg="white",cursor="hand2 ",command=self.add_result).place(x=460,y=5,width=100,height=40)
        
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",13,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=100,height=40)
       
        #====content image====

        self.bg_img=Image.open("images/image3.jpg")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)


        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=30,y=180,width=920,height=500)
       


        #=======Update details=======

        self.lbl_course=Label(self.root,text="Total Courses \n [0]",font=("Arial Narrow",15),bd=5,relief=GROOVE,bg="lavender",fg="black")
        self.lbl_course.place(x=400,y=530,width=300,height=90)
       
        self.lbl_student=Label(self.root,text="Total Students \n [0]",font=("Arial Narrow",15),bd=5,relief=GROOVE,bg="skyblue",fg="black")
        self.lbl_student.place(x=710,y=530,width=300,height=90)
        
        self.lbl_result=Label(self.root,text="Total Results \n [0]",font=("Arial Narrow",15),bd=5,relief=GROOVE,bg="lightblue",fg="black")
        self.lbl_result.place(x=1020,y=530,width=300,height=90)



        #===footer content====

        footer=Label(self.root,text="SRMS\nContact Us For Any Technical Issue \n Email id:-studentmanagement123@gmail.com\nPhone No:-4215875",font=("times new roman",12),bg='#033054',fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
#==================================================================================

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")


            cur.execute("select * from result ")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
           
                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
   
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    

    def logout(self):
        op=messagebox.askyesno("Confirm","Doyou really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


    

    
            
            






if __name__=="__main__":
    root=Tk()
    obj=RMS (root)
    root.mainloop()

       
        