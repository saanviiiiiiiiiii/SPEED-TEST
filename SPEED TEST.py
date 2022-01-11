from tkinter import *
import speedtest

root = Tk()
root.configure(bg = "navy blue")
root.geometry("500x300")
root.title("Internet Speed Test")

label = Label(root, text = " Internet Speed Check",font =("noteworthy",20 , "bold" , "italic"), fg="light blue",bg="navy blue")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label_download = Label(root, text = " Download Speed ↓",font =("cursive",20 , "bold" , "italic"), fg="light blue",bg="navy blue")
label_download.place(relx=0.25,rely=0.5,anchor=CENTER)

label_upload = Label(root, text = " Upload Speed ↑",font =("cursive",20 , "bold" , "italic"), fg="light blue",bg="navy blue")
label_upload.place(relx=0.75,rely=0.5,anchor=CENTER)


label_download_speed = Label(root,font =("Luxorious Roman",19 , "bold" ),bg="navy blue")
label_download_speed.place(relx=0.25,rely=0.6,anchor=CENTER)

label_upload_speed = Label(root,font =("Luxorious Roman",19 , "bold" ),bg="navy blue")
label_upload_speed.place(relx=0.75,rely=0.6,anchor=CENTER)

def speedCheck():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed['text'] = str(upload_speed) + "mbps"
    
btn_speed = Button(root,text="check speed",command = speedCheck,bg="white",relief = FLAT) 
btn_speed.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()
