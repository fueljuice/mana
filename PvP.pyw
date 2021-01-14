from tkinter import messagebox
from time import *
from tkinter import *


root2 = Tk()
root2.resizable(FALSE, FALSE)
root2.title("Log-In")
root2.geometry("300x550")

username = "python"
password = "888"

startnum2 = 10
startnum = 0
tries = 5
def login():
        global tries 
        global startnum
        global startnum2
        if password == password_guess.get() and username == username_guess.get():
                messagebox.showinfo("success" , "You entered your account succesfuly! CLOSE THE LOGIN WINDOW to start play!" , icon = 'warning')
                startnum = 10
                username_text.config(state=DISABLED)
                username_guess.config(state=DISABLED)
                password_guess.config(state=DISABLED)
                password_text.config(state=DISABLED)
                login_Button.config(state=DISABLED)
                root2.destroy()
                username_guess.delete(first=0,last=10000)
                password_guess.delete(first=0,last=10000)

        else:
                if tries > 0:
                        messagebox.showwarning("Error has been found" , "You have only " + str(tries) +  " tries")
                        tries = tries - 1
                        username_guess.delete(first=0,last=10000)
                        password_guess.delete(first=0,last=10000)
                else:
                        messagebox.showerror("NO" , " no more tries left")
                        
                        root2.destroy()
                        username_guess.delete(first=0,last=10000)
                        password_guess.delete(first=0,last=10000)
    
# יצירת אובייקטים
username_text = Label(root2, text="Username:")
password_text = Label(root2, text="Password:")
username_guess = Entry(root2,)
password_guess = Entry(root2, show = "*",)
login_Button = Button(root2, text="Login", command =  login)
# מפעל האריזה
username_text.pack()
username_guess.pack()
password_guess.pack()
password_text.pack()
login_Button.pack()

mainloop()




while startnum ==  startnum2:
        

        root = Tk()   # יצרתי אובייקט של טקינטר
        root.title("איקס עיגול")
        root.resizable(False, False)
        root.geometry("315x350")

        x_turn = 1
        count = 0
        def end():

                b1.config(state=DISABLED)
                b2.config(state=DISABLED)
                b3.config(state=DISABLED)
                b4.config(state=DISABLED)
                b5.config(state=DISABLED)
                b6.config(state=DISABLED)
                b7.config(state=DISABLED)
                b8.config(state=DISABLED)
                b9.config(state=DISABLED)

                root.title("ניצחון!")
                


        def winCheck():
                # בדיקה של השורות
                if b1 ["text"] == b2 ["text"] == b3 ["text"] != " " or b4 ["text"] == b5 ["text"] == b6 ["text"] != " " or b7 ["text"] == b8 ["text"] == b9 ["text"] != " " :
                        end()
                
                # בדיקה של העמודות
                if b1 ["text"] == b4 ["text"] == b7 ["text"] != " " or b2 ["text"] == b5 ["text"] == b8 ["text"] != " " or b3 ["text"] == b6 ["text"] == b9 ["text"] != " " :
                        end()

                # בדיקה של האלכסונים
                if b1 ["text"] == b5 ["text"] == b9 ["text"] != " " or b3 ["text"] == b5 ["text"] == b7 ["text"] != " ":
                        end()


        def click(b):
                #global x_turn
                global count
                
                

                if b["text"] == " ":
                        b.config(text = "X")
                        count += 1


                        if b3["text"] == b6["text"] == "O" or b1["text"] == b5["text"] == "O" or b7["text"] == b8["text"] =="O" and b9["text"] == " ":
                                b9.config(text = "O")
                                sleep(0.5)

                        elif b5["text"] == b2["text"] == "O" and b8["text"] == " ":
                                b8.config(text = "O")
                                sleep(0.5)
        
                        elif b1["text"] == b3["text"] == "O" or b3["text"] == b5["text"] == "O" or b9["text"] == b8["text"] =="O" and b7["text"] == " ":
                                b7.config(text = "O")
                                sleep(0.5)

                        elif b5["text"] == b4["text"] == "O" and b5["text"] == " ":   
                                b6.config(text = "O")
                                sleep(0.5)

                        #לא צריך B5 כי הוא האמצע

                        #elif b6["text"] == b5["text"] == "O" and b4["text"] == " ": X
                        #        b4.config(text = "O")
                        #        sleep(0.5)

                        elif b6["text"] == b9["text"] == "O" or b1["text"] == b2["text"] == "O" or b7["text"] == b4["text"] =="O" and b1["text"] == " ":  
                                b1.config(text = "O")
                                sleep(0.5)
                        
                        elif b5["text"] == b8["text"] == "O" and b2["text"] == " ": 
                                b2.config(text = "O")
                                sleep(0.5)
                        
                        elif b2["text"] == b3["text"] == "O" or b7["text"] == b5["text"] == "O" or b9["text"] == b5["text"] =="O" and b3["text"] == " ":  
                                b3.config(text = "O")
                                sleep(0.5)
                        
                        


                        # HERE THE SPACE


                        elif b3["text"] == b6["text"] == "X" or b1["text"] == b5["text"] == "X" or b7["text"] == b8["text"] =="X" and b9["text"] == " ":
                                b9.config(text = "O")
                                sleep(0.5)

                        elif b5["text"] == b2["text"] == "X" and b8["text"] == " ":
                                b8.config(text = "O")
                                sleep(0.5)
        
                        elif b1["text"] == b3["text"] == "X" or b3["text"] == b5["text"] == "X" or b9["text"] == b8["text"] =="X" and b7["text"] == " ":
                                b7.config(text = "O")
                                sleep(0.5)

                        elif b5["text"] == b4["text"] == "X" and b5["text"] == " ":   
                                b6.config(text = "O")
                                sleep(0.5)

                        #לא צריך B5 כי הוא האמצע

                        elif b6["text"] == b5["text"] == "X" and b4["text"] == " ":
                                b4.config(text = "O")
                                sleep(0.5)

                        elif b6["text"] == b9["text"] == "X" or b1["text"] == b2["text"] == "X" or b7["text"] == b5["text"] =="X" and b3["text"] == " ":  
                                b3.config(text = "O")
                                sleep(0.5)
                        
                        elif b5["text"] == b8["text"] == "X" and b2["text"] == " ": 
                                b2.config(text = "O")
                                sleep(0.5)


                        #מתקן את העיגולים שלא יעשו בעיות




                        
                        
                        
                


                        elif b5["text"] == " " :
                                b5.config(text = "O")
                        elif b4 ["text"] == " ":
                                b4.config(text = "O")
                        
                        elif b1["text"] == " ":
                                b1.config(text = "O")

                        elif b2["text"] == " ": 
                                b2.config(text = "O")
                        elif b3["text"] == " ":
                                b3.config(text = "O")
                        elif b4["text"] == " ":
                                b4.config(text = "O")
                        elif b5["text"] == " ":
                                b5.config(text = "O")
                        elif b6["text"] == " ":
                                b6.config(text = "O")
                        elif b7["text"] == " ":
                                b7.config(text = "O")
                        elif b8["text"] == " ":
                                b8.config(text = "O")
                        elif b9["text"] == " ":
                                b9.config(text = "O")

                        
                winCheck()

                if count == 9:
                        
                        end()
                        root.title("תיקו")

        # אובייקטים

        b1 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b1))
        b2 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b2))
        b3 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b3))

        b4 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b4))
        b5 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b5))
        b6 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b6))

        b7 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b7))
        b8 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b8))
        b9 = Button(root, text = " " ,font = ( "Helvetica", 20), height=3, width=6, command = lambda: click(b9))



        b1.grid(row = 0, column = 0)
        b2.grid(row = 0, column = 1)
        b3.grid(row = 0, column = 2)

        b4.grid(row = 1, column = 0)
        b5.grid(row = 1, column = 1)
        b6.grid(row = 1, column = 2)

        b7.grid(row = 2, column = 0)
        b8.grid(row = 2, column = 1)
        b9.grid(row = 2, column = 2)


        mainloop()
        break
        