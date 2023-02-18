#importing modules 


import qrcode 
from tkinter import * 
from tkinter import messagebox 

#function to generate the qrcode and and save it 
def generateCode():

 #creating a QRcode object of size specified by user 
 qr = qrcode.QRCode()

 #creating a QRcode object of the size specified by the user 
 qr = qrcode.QRCode(version = size.get(), box_size = 10, border = 5)
 #adding the data to be encoded 
 qr.add_data(text.get())

 #making the entire qr code space filled 
 qr.make(fit = True)
 #generate the qr code 
 img = qr.make_image()
 #getting the directory to save the file 
 fileDirec=loc.get()+'\\'+name.get()


 #saving the qr code 
 img.save(f'{fileDirec}.png')
 # showing up the message box 
 messagebox.showinfo("QR code is generator" , "QR code is generated successfully!")




#creating main window 
wn = Tk()
wn.title('QR code generator')
wn.geometry('1000x1000')
wn.config(bg ='black')

#Wiindows labels
headingFrame = Frame(wn , bg="DimGray", bd=5)
headingFrame.place (relx=0.15 , rely = 0.05 , relwidth = 0.7 , relheight = 0.1  )
headingLabel = Label(headingFrame , text = "Generate QR Code" , bg = 'DimGray' , font=('Helvetica', 20 , 'bold') )
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


# taking input of url for qr code genration
Frame1 = Frame(wn , bg="DimGray") 
Frame1.place(relx=0.1 , rely=0.15 , relwidth = 0.7 , relheight = 0.3 )
label1 = Label(Frame1 , text ="Enter the URL: " , bg="black" , fg="DimGray" , font=('Courier' , 13 , 'bold') )
label1.place(relx=0.05 , rely=0.2 , relheight = 0.08)

text = Entry(Frame1 , font=('Century 12'))
text.place(relx = 0.05 , rely=0.4 , relwidth = 1 , relheight = 0.2 )


#input location to save the qrcode 
Frame2 = Frame(wn , bg = 'black')
Frame2.place(relx=0.1 , rely = 0.35 , relwidth= 0.7 , relheight = 0.3 )

label2 = Label(Frame2 , text = "Enter the location to save the QR code: ", bg="black" , fg="DimGray" , font=('Courier', 13 , 'bold'))
label2.place(relx=0.1 , rely=0.05 , relwidth = 0.2 , relheight = 0.08)

loc = Entry(Frame2,font=('Century 12'))
loc.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)


#Getting input of the QR code image name 
Frame3 = Frame(wn , bg="black")
Frame3.place(relx=0.1 , rely=0.55 , relwidth=0.7 , relheight=0.3)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="black",fg='DimGray',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)


name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#getting input for the size of the qr code 
Frame4 = Frame(wn , bg="black")
Frame4.place(relx=0.1 , rely=0.75 , relwidth = 0.7 , relheight = 0.2 )


label4 = Label(Frame4,text="Enter the size from 1 to 40 with 1 being 21x21: ",bg="black",fg='Dimgray',font=('Courier',13,'bold'))
label4.place(relx=0.05,rely=0.2, relheight=0.08)

size = Entry(Frame4,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)
#Button to generate and save the QR Code
button = Button(wn, text='Generate Code',font=('Courier',15,'normal'),command=generateCode)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
wn.mainloop()














