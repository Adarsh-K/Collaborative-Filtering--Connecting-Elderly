import tkinter as tk, subprocess, os, csv
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Match with Movies")
root.configure(background="wheat")
root.minsize(800, 650)
img = ImageTk.PhotoImage(Image.open("oldman.jpg").resize((400, 250)))
label=ttk.Label(root,image=img)
label.pack()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Hi James,", style="BW.TLabel", font="Times 26", width=30, anchor=NW)
l1.pack()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black")
l2 = ttk.Label(text="Please rate some movies below:", style="BW.TLabel", font="Times 26", width=30, anchor=NW, background="white")
l2.pack(pady=10)

scrollbar = ttk.Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )

movies_List = open('movie_ids.txt','r',encoding = "ISO-8859-1") 
Lines = movies_List.readlines() 
count = 0
for line in Lines:  
    mylist.insert(END, line)
mylist.pack(fill = BOTH)
scrollbar.config(command = mylist.yview)

l3=ttk.Label(root, text="Movie ID", style="BW.TLabel", font="Times 20", width=10)
l3.pack(side="left", pady=5, padx=10)
e1 = ttk.Entry(root, width=10)
e1.pack(side="left", pady=5, padx=10)
l4=ttk.Label(root, text="Stars(1 to 5)", style="BW.TLabel", font="Times 20", width=10)
l4.pack(side="left", pady=5, padx=10)
e2 = ttk.Entry(root, width=10)
e2.pack(side="left", pady=5, padx=10)

file=open('outputgui.csv', 'w', newline='') 
writer = csv.writer(file)
def addRating():
	writer.writerow([e1.get(), e2.get()])
	file.flush()
	e1.delete(0, 'end')
	e2.delete(0, 'end')

def done():
	root.destroy()
	os.system('/Applications/MATLAB_R2018b.app/bin/matlab -nojvm -nodesktop -nosplash -nodisplay -r "run ex8_cofi.m;quit;"')
	
B = ttk.Button(root, text ="Add Rating", command = addRating, width=15)
B.pack(side="left")

B1 = ttk.Button(root, text ="Done", command = done, width=15)
B1.pack(side="left")

root.mainloop()

####################
root = tk.Tk()

root.title("Match with Movies")
root.configure(background="wheat")
root.minsize(800, 650)
img = ImageTk.PhotoImage(Image.open("oldman.jpg").resize((400, 250)))
label=ttk.Label(root,image=img)
label.pack()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Hi James,", style="BW.TLabel", font="Times 26", width=30, anchor=NW)
l1.pack()

style = ttk.Style()
style.configure("BW.TLabel", foreground="black")
l2 = ttk.Label(text="Movies you might like based on your ratings:", style="BW.TLabel", font="Times 26", width=30, anchor=NW, background="white")
l2.pack(pady=10)

scrollbar = ttk.Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )

movies_List = open('my_recom.txt','r',encoding = "ISO-8859-1") 
Lines = movies_List.readlines() 
count = 0
for line in Lines:  
    mylist.insert(END, line)
mylist.pack(fill = BOTH)
scrollbar.config(command = mylist.yview)

def makeFriends():
	root.destroy()

B = ttk.Button(root, text ="Wanna make new Friends tonight?", command = makeFriends, width=30)
B.pack(pady=10)

root.mainloop()
###################
root = tk.Tk()

root.title("Match with Movies")
movies_List = open('output.txt','r',encoding = "ISO-8859-1") 
Lines = movies_List.readlines() 
 
num=[]
movies=[]
for line in Lines:  
    if not(line[0].isdigit()):
    	movies.append(line)
    	continue
    num.append(int(line))
num.sort()
print(num)
print(movies)

names=open('names.txt','r',encoding = "ISO-8859-1")
Lines1=names.readlines()
count=0
c=0
users=[]
for n in Lines1:
	count+=1
	if count==num[c]:
		users.append(n)
		c+=1
		if c>=len(num):
			break
print(users)

root.configure(background="wheat")
root.minsize(800, 650)

style1 = ttk.Style()
style1.configure("BW.TLabel", foreground="black", background="white")
l0 = ttk.Label(text="3 People with similar movie taste found within 2 miles of your house!", style="BW.TLabel", font="Times 20", width=59)
l0.grid(row=0, column=1, pady=10)

img = ImageTk.PhotoImage(Image.open("user1.png").resize((400, 300)))
label=ttk.Label(root,image=img)
label.grid(row=1, column=0)
style = ttk.Style()
style.configure("BW.TLabel", foreground="black")
l4 = ttk.Label(text=users[0], style="BW.TLabel", font="Times 20",  background="white")
l4.grid(row=2, column=0)

img1 = ImageTk.PhotoImage(Image.open("user2.png").resize(( 400, 300)))
label1=ttk.Label(root,image=img1)
label1.grid(row=1, column=1)
style = ttk.Style()
style.configure("BW.TLabel", foreground="black")
l5 = ttk.Label(text=users[1], style="BW.TLabel", font="Times 20",  background="white")
l5.grid(row=2, column=1)

img2 = ImageTk.PhotoImage(Image.open("user3.png").resize((400, 300)))
label2=ttk.Label(root,image=img2)
label2.grid(row=1, column=2)
style = ttk.Style()
style.configure("BW.TLabel", foreground="black")
l6 = ttk.Label(text=users[2], style="BW.TLabel", font="Times 20", background="white")
l6.grid(row=2, column=2)

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Send an Invitation?", style="BW.TLabel", font="Times 26", width=20)
l1.grid(row=3, column=1,pady=5)

mov=""
for m in movies:  
    mov=mov+m
mov="Movies recommended for you all:\n\n"+mov
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l6 = ttk.Label(text=mov, style="BW.TLabel", font="Times 18", width=40)
l6.grid(row=3, column=0, rowspan=2,pady=5)

e1 = ttk.Entry(root, width=50)
e1.grid(row=4,column=1,  pady = 5)

def send():
	root.destroy()

B = ttk.Button(root, text ="Send invite", command = send, width=15)
B.grid(row=6,column=1,pady=3)

root.mainloop()
#########################
root = tk.Tk()

root.title("Match with Movies")
root.configure(background="wheat")
root.minsize(800, 650)
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
l1 = ttk.Label(text="Invitation send! You'll soon hear from them when they reply.", style="BW.TLabel", font="Times 26", width=100)
l1.pack()
img = ImageTk.PhotoImage(Image.open("cel.png").resize((500, 400)))
label=ttk.Label(root,image=img)
label.pack(pady=10)

root.mainloop()