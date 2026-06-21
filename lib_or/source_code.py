
import time
from csv import excel

from numpy.ma.core import count
from qrcode.console_scripts import error_correction
import os
import ctypes
import datetime as dt
import pyqrcode
from PIL.ImageMorph import ROTATION_MATRIX
from customtkinter import *
from doctest import master
from pyqrcode import *
from PIL import Image
from tkinter import Toplevel, image_names, Tk, mainloop
import pyautogui
from tkinter.filedialog import asksaveasfilename,askopenfiles,askopenfilenames
import base64
import qrcode
import cv2
from pyzbar.pyzbar import decode
from pyqrcode import *
import customtkinter
import time
from keyboard import *
import keyboard
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
os.environ['PATH'] += os.pathsep + os.getcwd()

ctypes.cdll.LoadLibrary(os.path.join(os.getcwd(), "libzbar-64.dll"))

fils=""

protall=""
tall=""
dat_join=""

def dat_ion():
    global dat_join
    dat_join = dt.date.today()


mr_mrs=""
nbx=""
numb=""
for_num_abx=""
qr_contents_qr=""
return_dat=""
tex_l=""
an_nbxx=""
san_nbxx=""
nnbx=""
name_is=""
def na_log():
    global name_is
def qrr(value):
    global qr_contents_qr
    qr_contents_qr=value

def glo_var(value):
    global mr_mrs
    global nbx
    global numb
    global for_num_abx
    global tex_l
    global an_nbxx
    global san_nbxx
    global nnbx
    global dat_join
    global return_dat
    return_dat =value
    dat_join=value
    tex_l = value
    an_nbxx=value
    san_nbxx=value
    nnbx=value

    mr_mrs = value
    nbx=value
    numb=value
    for_num_abx=value

def img():
    global fils

    fils = askopenfiles("rb", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                        title="Upload File")

    fils = Image.open(fils[0])

    fils = CTkImage(fils, size=(250, 250))




set_appearance_mode("white")


imopn = Image.open("library_app.png")
search=Image.open("search.png")
search=CTkImage(search,size=(30,30))
menu=Image.open("menu.png")
menu=CTkImage(menu,size=(30,30))
add_members=Image.open("members.png")
add_members=CTkImage(add_members,size=(100,100))
books=Image.open("book.png")
books=CTkImage(books,size=(100,100))
users=Image.open("scanuser.png")
users=CTkImage(users,size=(140,100))
homes=Image.open("home.png")
homes=CTkImage(homes,size=(40,30))
cam=Image.open("cam.png")
cam=CTkImage(cam,size=(40,30))
toda=Image.open("toda.png")
toda=CTkImage(toda,size=(34,34))
clocks=Image.open("clock.png")
clocks=CTkImage(clocks,size=(34,34))
booklists=Image.open("booklist.png")
booklists=CTkImage(booklists,size=(34,34))
booklists=Image.open("booklist.png")
booklists=CTkImage(booklists,size=(34,34))
details=Image.open("user.png")
details=CTkImage(details,size=(34,34))
wall=Image.open("libboard.png")
wall=CTkImage(wall,size=(1550,850))
in__out_time_img=Image.open("in_&_out_time_img.png")
in__out_time_img=CTkImage(in__out_time_img,size=(1550,850))
login_lib=Image.open("login_lib.png")
login_lib=CTkImage(login_lib,size=(1550,850))
wall_bought_turn=Image.open("libboard_bought_return.png")
wall_bought_turn=CTkImage(wall_bought_turn,size=(1550,850))
libboard_bought_return_scan=Image.open("libboard_bought_return_scan.png")
libboard_bought_return_scan=CTkImage(libboard_bought_return_scan,size=(1550,850))
libboard_bought_return_scan_instead=Image.open("libboard_bought_return_scan_instead.png")
libboard_bought_return_scan_instead=CTkImage(libboard_bought_return_scan_instead,size=(1550,850))
libboard_bought_return=Image.open("libboard_bought_return.png")
libboard_bought_return=CTkImage(libboard_bought_return,size=(1550,850))
libboard_bought_return200=Image.open("libboard_bought_return200.png")
libboard_bought_return200=CTkImage(libboard_bought_return200,size=(1550,850))
titles=Image.open("title.png")
titles=CTkImage(titles,size=(1650,70))
lib__member=Image.open("libboard_members.png")
lib__member=CTkImage(lib__member,size=(1550,850))
book_try=Image.open("book_entry.png")
book_try=CTkImage(book_try,size=(1550,850))
id_vis=Image.open("library user id.png")
id_vis=CTkImage(id_vis,size=(800,400))
upload=Image.open("uploadd.png")
upload=CTkImage(upload,size=(34,34))
verified_e=Image.open("verify_ed.png")
verified_e=CTkImage(verified_e,size=(34,34))

def home_pg():
    moon = CTkLabel(app2, image=wall, text="")
    moon.place(relx=0.0, rely=0.0)
    frame_top = CTkFrame(master=app2, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)

    name_label = CTkLabel(master=app2, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

    namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)
    frame = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="white", fg_color="black")
    frame.place(rely=0.860, relx=0.27)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=app2, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)

    def members():

        app3 = CTkLabel(app2, image=lib__member, text="")
        app3.place(relx=0.0, rely=0.0)
        frame_top = CTkFrame(master=app3, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")

        name_label = CTkLabel(master=app3, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))
        namlbl = CTkLabel(master=app3, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=app3, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)

        frame = CTkFrame(master=app3, width=700, height=50, corner_radius=12, bg_color="transparent", fg_color="black")
        frame.place(rely=0.860, relx=0.27)

        home = CTkButton(master=app3, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=app3, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=app3, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=app3, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)
        detail = CTkButton(master=app3, image=details, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)
        namlbl = CTkLabel(master=app3, text_color="white", text="Name", fg_color="black", font=("Arial", 24, "bold"),
                          height=30, width=75, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.170, rely=0.26)
        namebx = CTkEntry(master=app3, placeholder_text="Name", fg_color="white", border_color="black",
                          border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        namebx.place(relx=0.170, rely=0.3)
        datlbl = CTkLabel(master=app3, text_color="white", text="DOB", fg_color="black", font=("Arial", 24, "bold"),
                          height=30, width=75, corner_radius=32, bg_color="black")
        datlbl.place(relx=0.170, rely=0.46)
        dat = CTkEntry(master=app3, placeholder_text="DD/MM/YYYY", fg_color="white", border_color="black",
                       border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        dat.place(relx=0.170, rely=0.5)
        droplist = CTkLabel(master=app3, text_color="white", text="About", fg_color="black", font=("Arial", 24, "bold"),
                            height=30, width=75, corner_radius=32, bg_color="black")
        droplist.place(relx=0.170, rely=0.639)
        Iam = CTkComboBox(master=app3, width=350, height=60, corner_radius=0, fg_color="white",
                          dropdown_fg_color="white",
                          dropdown_hover_color="pink", dropdown_text_color="black",
                          values=["  ", "Student", "Working Professional", "Others"], button_color="black",
                          text_color="grey", font=("Arial", 20, "bold"))
        Iam.place(relx=0.170, rely=0.68)
        droplist_gen = CTkLabel(master=app3, text_color="white", text="Gender", fg_color="black",
                                font=("Arial", 24, "bold"),
                                height=30, width=75, corner_radius=32, bg_color="black")
        droplist_gen.place(relx=0.470, rely=0.26)

        datem = CTkEntry(master=app3, placeholder_text="example@gmail.com", fg_color="white", border_color="black",
                         border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")

        datem.place(relx=0.470, rely=0.56)

        namlblem = CTkLabel(master=app3, text_color="white", text="Gmail", fg_color="black", font=("Arial", 24, "bold"),
                            height=30, width=75, corner_radius=32, bg_color="black")
        namlblem.place(relx=0.470, rely=0.52)

        def vis_card():
            global mr_mrs
            global nbx
            global numb
            global fils
            global tex_l
            global an_nbxx
            global san_nbxx
            dat_ion()

            app4 = CTkLabel(app2, image=wall, text="")
            app4.place(relx=0.0, rely=0.0)
            frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                                 fg_color="black", border_color="black")
            frame_top.place(relx=0, rely=0)
            with open("account_details.txt", "r") as log_name:
                pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                pr_new_log = str(pr_new_log)
            with open("account_details.txt", "r") as log_name:
                pr_new_log_img = log_name.readline().replace("\n", "")
            lo_na_png = Image.open(f"{pr_new_log_img}.png")
            lo_na_png = CTkImage(lo_na_png, size=(50, 50))

            name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                                  bg_color="black", anchor="center")
            name_label.place(rely=0.02, relx=0.04)
            namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                              font=("Arial", 24, "bold"),
                              height=50, width=50, corner_radius=32, bg_color="black")
            namlbl.place(relx=0.88, rely=0.01)

            def des_t():
                app2.destroy()

            search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                                   fg_color="black",
                                   bg_color="black", command=des_t)
            search_btn.place(rely=0.01, relx=0.95)

            frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                             fg_color="black")
            frame.place(rely=0.860, relx=0.27)
            home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                             text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                             bg_color="transparent", border_color="black", border_width=2, command=home_pg)
            home.place(rely=0.864, relx=0.30)
            todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                               text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                               bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
            todays.place(rely=0.864, relx=0.39)
            clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                              text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                              bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
            clock.place(rely=0.864, relx=0.57)
            now_upp = datetime.now().strftime("%A")

            namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                              font=("Brush Script MT", 34, "bold"),
                              height=49, width=50, corner_radius=32, bg_color="black")
            namlbl.place(relx=0.44, rely=0.860)

            detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue", text="",
                               text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                               bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
            detail.place(rely=0.864, relx=0.66)
            card_lib = CTkLabel(master=app4, image=id_vis, text="")
            card_lib.place(rely=0.2, relx=0.240)
            card_lib = CTkLabel(master=app4, image=fils, text="")
            card_lib.place(rely=0.3, relx=0.250)
            with open("account_details.txt", "r") as log_name:
                pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                pr_new_log = str(pr_new_log)
            with open("account_details.txt", "r") as log_name:
                pr_new_log_img = log_name.readline().replace("\n", "")
            lo_na_png = Image.open(f"{pr_new_log_img}.png")
            lo_na_png = CTkImage(lo_na_png, size=(50, 50))

            name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 30, "bold"), text_color="white",
                                  bg_color="black", anchor="center")
            name_label.place(rely=0.225, relx=0.260)
            nbx = namebx.get()
            dbx = dat.get()
            dbx.replace("/", "").replace("-", "").replace(" ", "")
            namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                              font=("Arial", 24, "bold"),
                              height=50, width=50, corner_radius=32, bg_color="black")
            namlbl.place(relx=0.88, rely=0.01)

            name_nbx = CTkLabel(master=app4, text=f"{nbx}", font=("Georgia", 20, "bold"), text_color="black",
                                bg_color="#ffff66", anchor="center")
            name_nbx.place(rely=0.600, relx=0.290)

            if mr_mrs == "Male":
                name_gbx = CTkLabel(master=app4, text="Mr.", font=("Georgia", 20, "bold"), text_color="black",
                                    bg_color="#ffff66", anchor="center")
                name_gbx.place(rely=0.600, relx=0.265)
            elif mr_mrs == "Female":
                name_gbx = CTkLabel(master=app4, text="Mrs.", font=("Georgia", 20, "bold"), text_color="black",
                                    bg_color="#ffff66", anchor="center")
                name_gbx.place(rely=0.600, relx=0.260)

            selll = Iam.get()
            numb = int(con.get())
            emaill = datem.get()

            san_nbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")
            content = f"{nbx}\n{mr_mrs}\n{numb}\n{dbx}\n{selll}\n{dat_join}\n{emaill}"
            content2 = f"{nbx}{mr_mrs}{numb}{dbx}\n{selll}"
            text = open(f"{nbx}{numb}.txt", "w")

            text2 = open(f"{nbx}{numb}2.txt", "w")

            text.write(content)
            text2.write(content2)

            text.close()
            text2.close()

            contents = f"{nbx}{numb}"
            qr = pyqrcode.create(contents)
            qr.png(f"{san_nbx}.png", scale=6)
            img = Image.open(f"{san_nbx}.png")
            img = CTkImage(img, size=(200, 200))
            qqr = CTkLabel(app4, image=img, text="")
            qqr.place(relx=0.580, rely=0.350)

            generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                     border_color="black", text_color="white", text="Save",
                                     font=("Arial", 20, "bold"), command=com_vis)
            generate_but.place(relx=0.665, rely=0.72)
            tex = open(f"{nbx}{numb}.txt", "r")

            tex.close()

        def com_vis():

            roott = Toplevel(app2)
            roott.withdraw()
            global nbx
            global nnbx
            global dat_join

            nnbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")

            file_path = asksaveasfilename(defaultextension=".png",
                                          filetypes=[("PNG files", "*.png"), ("All files", "*.*")], title="Save As",
                                          initialfile=f"{nnbx}{numb}")
            region = (470, 250, 990, 465)
            screen_shot = pyautogui.screenshot(region=region)

            screen_shot.save(file_path)
            screen_shot.save(f"{nnbx}{numb}.png")
            region = (481, 344, 311, 311)
            screen_shot = pyautogui.screenshot(region=region)
            screen_shot.save(f"{nnbx}{mr_mrs}{numb}.png")
            # _________________________________________MAIL___________________________Automate_________________________________
            with open(f"{nbx}{numb}.txt", "r") as fi:
                em1 = fi.readline()
                em = fi.readline()
                em = fi.readline()
                em = fi.readline()
                em = fi.readline()
                em = fi.readline()
                em = fi.readline()
                print(f"{em1}")
                print(f"{em}")
            with open("account_details.txt", "r") as log_namee:
                lo1 = log_namee.readline()
                lo2 = log_namee.readline()
                lo3 = log_namee.readline()
                print(f"{lo2} mm")
                print(f"{lo3} pass")
            filename = f"{nnbx}{numb}.png"
            sender_maill = f"{lo2}"

            receiver_maill = f"{em}"
            passwords_m = f"{lo3}"
            subjects = "ID CARD"
            bodys = f"{em1} Here is your virtual library id card"
            me_ssage = MIMEMultipart()
            me_ssage["From"] = sender_maill
            me_ssage["To"] = receiver_maill
            me_ssage["Subject"] = subjects
            try:
                with open(filename, "rb") as attach_img:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attach_img.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment;filename={filename}")
                    me_ssage.attach(part)
            except Exception as e:
                print(f"Error : {e}")

            me_ssage.attach(MIMEText(bodys, "plain"))
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as servers:
                    servers.starttls()
                    servers.login(sender_maill, passwords_m)
                    servers.sendmail(sender_maill, receiver_maill, me_ssage.as_string())
                    print("successful")
            except Exception as e:
                print(f"Error {e}")

            fi.close()

        gen = CTkComboBox(master=app3, width=350, height=60, corner_radius=0, fg_color="white",
                          dropdown_fg_color="white", dropdown_hover_color="pink", dropdown_text_color="black",
                          values=["  ", "Male", "Female", "Others"], button_color="black", text_color="grey",
                          font=("Arial", 20, "bold"), command=glo_var)

        gen.place(relx=0.470, rely=0.3)
        droplist_con = CTkLabel(master=app3, text_color="white", text="Contact", fg_color="black",
                                font=("Arial", 24, "bold"),
                                height=30, width=75, corner_radius=32, bg_color="black")
        droplist_con.place(relx=0.470, rely=0.39)
        con = CTkEntry(master=app3, placeholder_text="Mobile NO", fg_color="white", border_color="black",
                       border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        con.place(relx=0.470, rely=0.43)

        generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Image",
                                 font=("Arial", 20, "bold"), image=upload, command=img)
        generate_but.place(relx=0.415, rely=0.68)

        generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Generate ID ✨",
                                 font=("Arial", 20, "bold"),
                                 command=vis_card)
        generate_but.place(relx=0.600, rely=0.68)

        app3.mainloop()

    def add_books():

        app3 = CTkLabel(app2, image=book_try, text="")
        app3.place(relx=0.0, rely=0.0)
        frame_top = CTkFrame(master=app3, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=app3, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=app3, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=app3, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)

        frame = CTkFrame(master=app3, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=app3, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=app3, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=app3, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=app3, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)

        detail = CTkButton(master=app3, image=details, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)
        namlbl = CTkLabel(master=app3, text_color="white", text="BOOK NAME", fg_color="black",
                          font=("Arial", 24, "bold"), height=30, width=75, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.170, rely=0.26)
        namebx = CTkEntry(master=app3, placeholder_text="BOOK NAME", fg_color="white", border_color="black",
                          border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        namebx.place(relx=0.170, rely=0.3)
        datlbl = CTkLabel(master=app3, text_color="white", text="CODE", fg_color="black", font=("Arial", 24, "bold"),
                          height=30, width=75, corner_radius=32, bg_color="black")
        datlbl.place(relx=0.170, rely=0.46)
        datt = CTkEntry(master=app3, placeholder_text="0000...", fg_color="white", border_color="black",
                        border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        datt.place(relx=0.170, rely=0.5)

        def vis_card():
            global mr_mrs
            global nbx
            global numb
            global for_num_abx

            app4 = CTkLabel(app2, image=wall, text="")
            app4.place(relx=0.0, rely=0.0)
            frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                                 fg_color="black", border_color="black")
            frame_top.place(relx=0, rely=0)
            with open("account_details.txt", "r") as log_name:
                pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                pr_new_log = str(pr_new_log)
            with open("account_details.txt", "r") as log_name:
                pr_new_log_img = log_name.readline().replace("\n", "")
            lo_na_png = Image.open(f"{pr_new_log_img}.png")
            lo_na_png = CTkImage(lo_na_png, size=(50, 50))

            name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                                  bg_color="black", anchor="center")
            name_label.place(rely=0.02, relx=0.04)
            namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                              font=("Arial", 24, "bold"),
                              height=50, width=50, corner_radius=32, bg_color="black")
            namlbl.place(relx=0.88, rely=0.01)

            def des_t():
                app2.destroy()

            search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                                   fg_color="black",
                                   bg_color="black", command=des_t)
            search_btn.place(rely=0.01, relx=0.95)

            frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                             fg_color="black")
            frame.place(rely=0.860, relx=0.27)
            home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                             text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                             bg_color="transparent", border_color="black", border_width=2, command=home_pg)
            home.place(rely=0.864, relx=0.30)
            todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                               text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                               bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
            todays.place(rely=0.864, relx=0.39)
            clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                              text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                              bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
            clock.place(rely=0.864, relx=0.57)
            now_upp = datetime.now().strftime("%A")

            namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                              font=("Brush Script MT", 34, "bold"),
                              height=49, width=50, corner_radius=32, bg_color="black")
            namlbl.place(relx=0.44, rely=0.860)
            detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue", text="",
                               text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                               bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
            detail.place(rely=0.864, relx=0.66)

            nbx = namebx.get()
            for_num_abx = int(datt.get())

            san_nbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")
            content = f"Book Name : {nbx}\nCode : {for_num_abx}"
            qr = pyqrcode.create(content)
            qr.png(f"{san_nbx}{for_num_abx}.png", scale=6)
            img = Image.open(f"{san_nbx}{for_num_abx}.png")
            img = CTkImage(img, size=(200, 200))
            qqr = CTkLabel(app4, image=img, text="")
            qqr.place(relx=0.430, rely=0.350)
            generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                     border_color="black", text_color="white", text="Save",
                                     font=("Arial", 20, "bold"), command=com_vis)
            generate_but.place(relx=0.445, rely=0.72)

        def com_vis():

            roott = Toplevel(app2)
            roott.withdraw()
            global nbx
            global nnbx
            global for_num_abx
            nnbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")

            file_path = asksaveasfilename(defaultextension=".png",
                                          filetypes=[("PNG files", "*.png"), ("All files", "*.*")], title="Save As",
                                          initialfile=f"{nnbx}{for_num_abx}")
            region = (830, 400, 245, 245)
            screen_shot = pyautogui.screenshot(region=region)
            if file_path:
                screen_shot.save(file_path)

            else:
                print("canceled")

        generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Generate ID ✨",
                                 font=("Arial", 20, "bold"),
                                 command=vis_card)
        generate_but.place(relx=0.600, rely=0.68)

        generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Generate QR ✨",
                                 font=("Arial", 20, "bold"), command=vis_card)
        generate_but.place(relx=0.600, rely=0.68)

        app3.mainloop()

    members = CTkButton(master=app2, image=add_members, corner_radius=32, hover_color="white", text="",
                        text_color="black",
                        height=200, width=200, font=("Arial", 40, "bold"), fg_color="sky blue", bg_color="dark blue",
                        border_color="dark blue", border_width=4, command=members)
    members.place(rely=0.3, relx=0.1)

    book = CTkButton(master=app2, image=books, corner_radius=32, hover_color="white", text="",
                     text_color="black", height=200, width=200, font=("Arial", 40, "bold"), fg_color="light green",
                     bg_color="dark green", border_color="dark green", border_width=4, command=add_books)
    book.place(rely=0.3, relx=0.4)

    def bought_return():

        appbot_re = CTkLabel(app2, image=libboard_bought_return_scan_instead, text="")
        appbot_re.place(relx=0.0, rely=0.0)
        frame_top = CTkFrame(master=appbot_re, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=appbot_re, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=appbot_re, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=appbot_re, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)
        frame = CTkFrame(master=appbot_re, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=appbot_re, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=appbot_re, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=appbot_re, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=appbot_re, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)
        detail = CTkButton(master=appbot_re, image=details, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)

        def retrive_details():
            global tex_l
            global qr_contents_qr
            global an_nbxx
            global san_nbxx
            global protall

            qrr(qr_contents_qr)

            cap_vid = cv2.VideoCapture(0)
            while True:
                ret, frame = cap_vid.read()
                decode_ing_vid_in_img = decode(frame)
                for deeecod in decode_ing_vid_in_img:
                    qr_contents_qr = deeecod.data.decode('utf-8')
                    qr_contents_qr = str(qr_contents_qr)
                    tex = open(f"{qr_contents_qr}.txt", "r")
                    texxll1 = tex.readline()
                    c11 = texxll1.replace("_", " ").replace("\n", "")
                    c1 = texxll1.replace(" ", "_").replace("\n", "")
                    texxll2 = tex.readline()
                    c2 = texxll2.replace(" ", "_").replace("\n", "")
                    texxll3 = tex.readline()
                    c3 = texxll3.replace(" ", "_").replace("\n", "")
                    texxll4 = tex.readline()
                    c4 = texxll4.replace(" ", "_").replace("\n", "")
                    texxll5 = tex.readline()
                    c5 = texxll5.replace(" ", " ").replace("\n", "")
                    texxll6 = tex.readline()
                    c6 = texxll6.replace(" ", " ").replace("\n", "")
                    allt = c1, c2, c3
                    allt2 = c11, c3
                    allt0enty = c11
                    allt1enty = c2
                    allt2enty = c3
                    allt3enty = c4
                    allt4enty = c5
                    allt5enty = c6
                    tall = ("".join(allt))
                    tall2 = ("".join(allt2))
                    tall0 = ("".join(allt0enty))
                    tall1 = ("".join(allt1enty))
                    tall22 = ("".join(allt2enty))
                    tall33 = ("".join(allt3enty))
                    tall44 = ("".join(allt4enty))
                    tall55 = ("".join(allt5enty))

                    tex.close()


                    app2n = CTkLabel(app2, image=libboard_bought_return, text="")
                    app2n.place(relx=0.0, rely=0.0)
                    frame_top = CTkFrame(master=app2n, width=2000, height=81, corner_radius=0, border_width=2,
                                         bg_color="white", fg_color="black", border_color="black")
                    frame_top.place(relx=0, rely=0)

                    with open("account_details.txt", "r") as log_name:
                        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                        pr_new_log = str(pr_new_log)
                    with open("account_details.txt", "r") as log_name:
                        pr_new_log_img = log_name.readline().replace("\n", "")
                    lo_na_png = Image.open(f"{pr_new_log_img}.png")
                    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                    name_label = CTkLabel(master=app2, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                          text_color="white", bg_color="black", anchor="center")
                    name_label.place(rely=0.02, relx=0.04)
                    namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                                      font=("Arial", 24, "bold"),
                                      height=50, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.88, rely=0.01)

                    def des_t():
                        app2.destroy()

                    search_btn = CTkButton(master=app2, image=search, hover_color="grey", height=50, width=50, text="",
                                           fg_color="black",
                                           bg_color="black", command=des_t)
                    search_btn.place(rely=0.01, relx=0.95)
                    framee = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="transparent",
                                      fg_color="black")
                    framee.place(rely=0.860, relx=0.27)
                    home = CTkButton(master=app2, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                     fg_color="black",
                                     bg_color="transparent", border_color="black", border_width=2, command=home_pg)
                    home.place(rely=0.864, relx=0.30)
                    todays = CTkButton(master=app2, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,
                                       command=getbook_putbook)
                    todays.place(rely=0.864, relx=0.39)
                    clock = CTkButton(master=app2, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                      fg_color="black",
                                      bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
                    clock.place(rely=0.864, relx=0.57)
                    now_upp = datetime.now().strftime("%A")

                    namlbl = CTkLabel(master=app2, text_color="black", text=now_upp, fg_color="white",
                                      font=("Brush Script MT", 34, "bold"),
                                      height=49, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.44, rely=0.860)
                    detail = CTkButton(master=app2, image=details, corner_radius=100, hover_color="dark blue", text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,
                                       command=loogin_setup)
                    detail.place(rely=0.864, relx=0.66)

                    protall = Image.open(f"{tall}.png")
                    protall = CTkImage(protall, size=(250, 250))

                    pro = CTkLabel(app2, image=protall, text="")
                    pro.place(relx=0.16, rely=0.24)

                    tec_pro = CTkLabel(master=app2, text=tall0, fg_color="black", text_color="white", height=30,
                                       width=250,
                                       font=("Georgia", 24))
                    tec_pro.place(relx=0.16, rely=0.60)
                    tec_pro = CTkLabel(master=app2, text="Name", fg_color="pink", bg_color="black", text_color="black",
                                       height=40,
                                       width=80, font=("Georgia", 19))
                    tec_pro.place(relx=0.16, rely=0.55)
                    tec_pro = CTkLabel(master=app2, text=tall1, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.16, rely=0.70)
                    tec_pro = CTkLabel(master=app2, text="Gender", fg_color="pink", bg_color="black",
                                       text_color="black",
                                       height=40,
                                       width=80, font=("Georgia", 19))
                    tec_pro.place(relx=0.16, rely=0.65)
                    tec_pro = CTkLabel(master=app2, text=tall22, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.52, rely=0.34)
                    tec_pro = CTkLabel(master=app2, text="Contact", fg_color="pink", bg_color="black",
                                       text_color="black",
                                       height=40,
                                       width=80, font=("Georgia", 19))
                    tec_pro.place(relx=0.52, rely=0.29)
                    tec_pro = CTkLabel(master=app2, text=tall33, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.52, rely=0.44)
                    tec_pro = CTkLabel(master=app2, text="DOB", fg_color="pink", bg_color="black",
                                       text_color="black",
                                       height=40,
                                       width=80, font=("Georgia", 19))
                    tec_pro.place(relx=0.52, rely=0.39)
                    tec_pro = CTkLabel(master=app2, text=tall44, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.52, rely=0.54)
                    tec_pro = CTkLabel(master=app2, text="About", fg_color="pink", bg_color="black",
                                       text_color="black",
                                       height=40,
                                       width=80, font=("Georgia", 19))
                    tec_pro.place(relx=0.52, rely=0.49)
                    tec_pro = CTkLabel(master=app2, text=tall55, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.52, rely=0.64)
                    tec_pro = CTkLabel(master=app2, text="Joined On", fg_color="pink", bg_color="black",
                                       text_color="black",
                                       height=40,
                                       width=80, font=("Georgia", 19))
                    tec_pro.place(relx=0.52, rely=0.59)

                    cv2.imshow('QR scanner press Q to exit', frame)
                    cap_vid.release()

                    cv2.destroyWindow('QR scanner press Q to exit')
                    return deeecod

                cv2.imshow('QR scanner press Q to exit', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap_vid.release()
            cv2.destroyAllWindows()

        generate_but = CTkButton(master=appbot_re, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Scan ID",
                                 font=("Arial", 20, "bold"), command=retrive_details)
        generate_but.place(relx=0.440, rely=0.58)

    user = CTkButton(master=app2, image=users, corner_radius=32, hover_color="white", text="",
                     text_color="black", height=200, width=200, font=("Arial", 40, "bold"), fg_color="light pink",
                     bg_color="red", border_color="red", border_width=4, command=bought_return)
    user.place(rely=0.3, relx=0.7)
    frame = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="transparent", fg_color="black")
    frame.place(rely=0.860, relx=0.27)
    home = CTkButton(master=app2, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2, command=home_pg)
    home.place(rely=0.864, relx=0.30)

    def getbook_putbook():

        appbot_re = CTkLabel(app2, image=libboard_bought_return_scan, text="")
        appbot_re.place(relx=0.0, rely=0.0)
        frame_top = CTkFrame(master=appbot_re, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=appbot_re, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=appbot_re, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=appbot_re, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)
        frame = CTkFrame(master=appbot_re, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=appbot_re, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=appbot_re, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=appbot_re, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=appbot_re, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)

        detail = CTkButton(master=appbot_re, image=details, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)

        def go_buy_put():
            global tex_l
            global qr_contents_qr
            global an_nbxx
            global san_nbxx
            global protall

            qrr(qr_contents_qr)

            cap_vid = cv2.VideoCapture(0)
            while True:
                ret, frame = cap_vid.read()
                decode_ing_vid_in_img = decode(frame)
                for deeecod in decode_ing_vid_in_img:
                    qr_contents_qr = deeecod.data.decode('utf-8')
                    qr_contents_qr = str(qr_contents_qr)
                    tex = open(f"{qr_contents_qr}.txt", "r")
                    texxll1 = tex.readline()
                    c11 = texxll1.replace("_", " ").replace("\n", "")

                    c1 = texxll1.replace(" ", "_").replace("\n", "")
                    texxll2 = tex.readline()
                    c2 = texxll2.replace(" ", "_").replace("\n", "")
                    texxll3 = tex.readline()
                    c3 = texxll3.replace(" ", "_").replace("\n", "")

                    allt = c1, c2, c3
                    tall_tall2 = c1, c3
                    allt0enty = c11
                    tall = ("".join(allt))
                    tall_tall = ("".join(tall_tall2)).replace("_", " ")
                    tall0 = ("".join(allt0enty))

                    app2n = CTkLabel(app2, image=libboard_bought_return200, text="")
                    app2n.place(relx=0.0, rely=0.0)
                    frame_top = CTkFrame(master=app2, width=2000, height=81, corner_radius=0, border_width=2,
                                         bg_color="white", fg_color="black", border_color="black")
                    frame_top.place(relx=0, rely=0)

                    with open("account_details.txt", "r") as log_name:
                        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                        pr_new_log = str(pr_new_log)
                    with open("account_details.txt", "r") as log_name:
                        pr_new_log_img = log_name.readline().replace("\n", "")
                    lo_na_png = Image.open(f"{pr_new_log_img}.png")
                    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                    name_label = CTkLabel(master=app2, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                          text_color="white", bg_color="black", anchor="center")
                    name_label.place(rely=0.02, relx=0.04)
                    namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                                      font=("Arial", 24, "bold"),
                                      height=50, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.88, rely=0.01)

                    def des_t():
                        app2.destroy()

                    search_btn = CTkButton(master=app2, image=search, hover_color="grey", height=50, width=50, text="",
                                           fg_color="black",
                                           bg_color="black", command=des_t)
                    search_btn.place(rely=0.01, relx=0.95)
                    framee = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="transparent",
                                      fg_color="black")
                    framee.place(rely=0.860, relx=0.27)
                    home = CTkButton(master=app2, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                     fg_color="black",
                                     bg_color="transparent", border_color="black", border_width=2, command=home_pg)
                    home.place(rely=0.864, relx=0.30)
                    todays = CTkButton(master=app2, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,
                                       command=getbook_putbook)
                    todays.place(rely=0.864, relx=0.39)
                    clock = CTkButton(master=app2, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                      fg_color="black",
                                      bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
                    clock.place(rely=0.864, relx=0.57)
                    now_upp = datetime.now().strftime("%A")

                    namlbl = CTkLabel(master=app2, text_color="black", text=now_upp, fg_color="white",
                                      font=("Brush Script MT", 34, "bold"),
                                      height=49, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.44, rely=0.860)

                    detail = CTkButton(master=app2, image=details, corner_radius=100, hover_color="dark blue", text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,
                                       command=loogin_setup)
                    detail.place(rely=0.864, relx=0.66)
                    protall = Image.open(f"{tall}.png")
                    protall = CTkImage(protall, size=(250, 250))

                    pro = CTkLabel(app2, image=protall, text="")
                    pro.place(relx=0.41, rely=0.29)
                    tec_pro = CTkLabel(master=app2, text=tall0, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.41, rely=0.60)

                    def get_book():

                        app4 = CTkLabel(app2, image=wall, text="")
                        app4.place(relx=0.0, rely=0.0)
                        frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                                             bg_color="white",
                                             fg_color="black", border_color="black")
                        frame_top.place(relx=0, rely=0)
                        # returninng date------------------------
                        dat = CTkEntry(master=app4, placeholder_text="Return YYYY-MM-DD", fg_color="white",
                                       border_color="black",
                                       border_width=2, height=60, width=350, font=("Arial", 20, "bold"),
                                       text_color="black", bg_color="black")

                        dat.place(relx=0.0, rely=0.1)
                        with open("account_details.txt", "r") as log_name:
                            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                            pr_new_log = str(pr_new_log)
                        with open("account_details.txt", "r") as log_name:
                            pr_new_log_img = log_name.readline().replace("\n", "")
                        lo_na_png = Image.open(f"{pr_new_log_img}.png")
                        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                              text_color="white",
                                              bg_color="black", anchor="center")
                        name_label.place(rely=0.02, relx=0.04)
                        namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                                          font=("Arial", 24, "bold"),
                                          height=50, width=50, corner_radius=32, bg_color="black")
                        namlbl.place(relx=0.88, rely=0.01)

                        def des_t():
                            app2.destroy()

                        search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50,
                                               text="",
                                               fg_color="black",
                                               bg_color="black", command=des_t)
                        search_btn.place(rely=0.01, relx=0.95)
                        frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                                         fg_color="black")
                        frame.place(rely=0.860, relx=0.27)
                        home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                         fg_color="black",
                                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
                        home.place(rely=0.864, relx=0.30)
                        todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                           fg_color="black",
                                           bg_color="transparent", border_color="black", border_width=2,
                                           command=getbook_putbook)
                        todays.place(rely=0.864, relx=0.39)
                        clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                                          text="",
                                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                          fg_color="black",
                                          bg_color="transparent", border_color="black", border_width=2,
                                          command=in_and_out)
                        clock.place(rely=0.864, relx=0.57)
                        now_upp = datetime.now().strftime("%A")

                        namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                                          font=("Brush Script MT", 34, "bold"),
                                          height=49, width=50, corner_radius=32, bg_color="black")
                        namlbl.place(relx=0.44, rely=0.860)
                        detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                                           text="",
                                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                           fg_color="black",
                                           bg_color="transparent", border_color="black", border_width=2,
                                           command=loogin_setup)
                        detail.place(rely=0.864, relx=0.66)

                        def scan_book_get():
                            global nbx
                            global namebx
                            global datt
                            global qr_contents_qr
                            global return_dat

                            qrr(qr_contents_qr)

                            cap_vid = cv2.VideoCapture(0)
                            while True:
                                ret, frame = cap_vid.read()
                                decode_ing_vid_in_img = decode(frame)
                                for deeecod in decode_ing_vid_in_img:
                                    qr_contents_qr = deeecod.data.decode('utf-8')
                                    qr_contents_qr = str(qr_contents_qr)
                                    nbx = qr_contents_qr

                                    san_nbx = nbx.replace(" ", "_").replace("/", "_").replace(":", "_").replace(".",
                                                                                                                "_").replace(
                                        "\n", "").replace("Book_Name_:_", "").replace("Code_:_", "")
                                    qr_contents_qr = str(qr_contents_qr)
                                    tex = open(f"{tall}transaction.txt", "a")
                                    dat_re_sub = dat.get()

                                    fromdat = dt.date.today()

                                    tex.write(
                                        f"{qr_contents_qr}\n*************************************************\nFrom : [{fromdat}]     To : [{dat_re_sub}]\n*************************************************\n")
                                    tex = open(f"{tall}transaction.txt", "r")
                                    print(tall)

                                    tec1 = tex.read()

                                    tex_box = customtkinter.CTkScrollableFrame(master=app4, corner_radius=32,
                                                                               border_width=4, bg_color="black",
                                                                               fg_color="black",
                                                                               border_color="black",
                                                                               scrollbar_button_color="gray",
                                                                               scrollbar_button_hover_color="gray",
                                                                               label_fg_color="white",
                                                                               label_text_color="black",

                                                                               label_font=("Arial", 20),
                                                                               label_anchor="center",
                                                                               orientation="vertical",
                                                                               scrollbar_fg_color="black", height=400,
                                                                               width=400)
                                    tex_box.place(relx=0.35, rely=0.15)
                                    dat_re_sub = dat.get()

                                    fromdat = dt.date.today()
                                    # date operation______________________________________________________

                                    customtkinter.CTkLabel(tex_box, text=f"{tec1}", text_color="white").pack(pady=10)
                                    print(f"h{tec1}")
                                    with open(f"{tall}transaction.txt", "r") as fii:
                                        fii = fii.read()
                                    with open(f"{tall_tall}.txt", "r") as fi:
                                        em1 = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        print(f"{em1}")
                                        print(f"{em}")

                                    with open("account_details.txt", "r") as log_namee:
                                        lo1 = log_namee.readline()
                                        lo2 = log_namee.readline()
                                        lo3 = log_namee.readline()
                                        print(f"{lo2} mm")
                                        print(f"{lo3} pass")
                                    filename = f"{nnbx}{numb}.png"
                                    sender_maill = f"{lo2}"

                                    receiver_maill = f"{em}"
                                    passwords_m = f"{lo3}"

                                    subjects = f"BOOK TRANSACTION OF\n {em1}"
                                    bodys = f"{fii}"
                                    me_ssage = MIMEMultipart()
                                    me_ssage["From"] = sender_maill
                                    me_ssage["To"] = receiver_maill
                                    me_ssage["Subject"] = subjects
                                    me_ssage.attach(MIMEText(bodys, "plain"))

                                    try:
                                        with smtplib.SMTP("smtp.gmail.com", 587) as servers:
                                            servers.starttls()
                                            servers.login(sender_maill, passwords_m)
                                            servers.sendmail(sender_maill, receiver_maill, me_ssage.as_string())
                                            print("successful")
                                    except Exception as e:
                                        print(f"Error {e}")

                                    fi.close()

                                    tex.close()

                                    cv2.imshow('QR scanner press Q to exit', frame)
                                    cap_vid.release()

                                    cv2.destroyWindow('QR scanner press Q to exit')
                                    return deeecod

                                cv2.imshow('QR scanner press Q to exit', frame)

                                if cv2.waitKey(1) & 0xFF == ord('q'):
                                    break

                            cap_vid.release()
                            cv2.destroyAllWindows()

                        generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72",
                                                 hover_color="pink",
                                                 border_color="black", text_color="white", text="Scan Book",
                                                 font=("Arial", 20, "bold"), command=scan_book_get)
                        generate_but.place(relx=0.450, rely=0.75)

                    generate_but = CTkButton(master=app2, width=150, height=60, fg_color="#b33b72",
                                             hover_color="pink",
                                             border_color="black", text_color="white", text="Get Book",
                                             font=("Arial", 20, "bold"), command=get_book)
                    generate_but.place(relx=0.360, rely=0.75)

                    def put_book():

                        app4 = CTkLabel(app2, image=wall, text="")
                        app4.place(relx=0.0, rely=0.0)

                        global qr_contents_qr
                        qrr(qr_contents_qr)

                        frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                                             bg_color="white",
                                             fg_color="black", border_color="black")
                        frame_top.place(relx=0, rely=0)
                        with open("account_details.txt", "r") as log_name:
                            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                            pr_new_log = str(pr_new_log)
                        with open("account_details.txt", "r") as log_name:
                            pr_new_log_img = log_name.readline().replace("\n", "")
                        lo_na_png = Image.open(f"{pr_new_log_img}.png")
                        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                              text_color="white",
                                              bg_color="black", anchor="center")
                        name_label.place(rely=0.02, relx=0.04)
                        namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                                          font=("Arial", 24, "bold"),
                                          height=50, width=50, corner_radius=32, bg_color="black")
                        namlbl.place(relx=0.88, rely=0.01)

                        def des_t():
                            app2.destroy()

                        search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50,
                                               text="",
                                               fg_color="black",
                                               bg_color="black", command=des_t)
                        search_btn.place(rely=0.01, relx=0.95)
                        frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                                         fg_color="black")
                        frame.place(rely=0.860, relx=0.27)
                        home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                         fg_color="black",
                                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
                        home.place(rely=0.864, relx=0.30)
                        todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                           fg_color="black",
                                           bg_color="transparent", border_color="black", border_width=2,
                                           command=getbook_putbook)
                        todays.place(rely=0.864, relx=0.39)
                        clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                                          text="",
                                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                          fg_color="black",
                                          bg_color="transparent", border_color="black", border_width=2,
                                          command=in_and_out)
                        clock.place(rely=0.864, relx=0.57)
                        now_upp = datetime.now().strftime("%A")

                        namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                                          font=("Brush Script MT", 34, "bold"),
                                          height=49, width=50, corner_radius=32, bg_color="black")
                        namlbl.place(relx=0.44, rely=0.860)
                        detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                                           text="",
                                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                           fg_color="black",
                                           bg_color="transparent", border_color="black", border_width=2,
                                           command=loogin_setup)
                        detail.place(rely=0.864, relx=0.66)

                        def put_scan_book():
                            global tex_l
                            global qr_contents_qr
                            global an_nbxx
                            global san_nbxx
                            global protall

                            qrr(qr_contents_qr)

                            cap_vid = cv2.VideoCapture(0)
                            while True:
                                ret, frame = cap_vid.read()
                                decode_ing_vid_in_img = decode(frame)
                                for deeecod in decode_ing_vid_in_img:
                                    qr_contents_qr = deeecod.data.decode('utf-8')
                                    qr_contents_qr = str(qr_contents_qr)
                                    tex = open(f"{qr_contents_qr}.txt", "r")
                                    texxll1 = tex.readline()
                                    c11 = texxll1.replace("_", " ").replace("\n", "")
                                    c1 = texxll1.replace(" ", "_").replace("\n", "")
                                    texxll2 = tex.readline()
                                    c2 = texxll2.replace(" ", "_").replace("\n", "")
                                    texxll3 = tex.readline()
                                    c3 = texxll3.replace(" ", "_").replace("\n", "")

                                    allt = c1, c2, c3

                                    tallputt = ("".join(allt))

                                    re_sen = open(f"{tallputt}transaction.txt", "a")
                                    dat_retun = dt.date.today()
                                    re_sen2 = open(f"{tallputt}transaction.txt", "r")
                                    del_tex2 = re_sen2.read()
                                    re_sen.write(
                                        f"\nReturned on {dat_retun}\nCheck above listed books are returned \n Then press Ok.")
                                    re_sen = open(f"{tallputt}transaction.txt", "r")
                                    del_tex = re_sen.read()
                                    tex_box = customtkinter.CTkScrollableFrame(master=app4, corner_radius=32,
                                                                               border_width=4, bg_color="black",
                                                                               fg_color="black",
                                                                               border_color="black",
                                                                               scrollbar_button_color="gray",
                                                                               scrollbar_button_hover_color="gray",
                                                                               label_fg_color="white",
                                                                               label_text_color="black",

                                                                               label_font=("Arial", 20),
                                                                               label_anchor="center",
                                                                               orientation="vertical",
                                                                               scrollbar_fg_color="black",
                                                                               height=400, width=400)
                                    tex_box.place(relx=0.35, rely=0.15)
                                    customtkinter.CTkLabel(tex_box, text=del_tex, text_color="white").pack(
                                        pady=10)
                                    re_sen.close()
                                    with open(f"{tallputt}transaction.txt", "r") as fii:
                                        fii = fii.read()
                                    with open(f"{tall_tall}.txt", "r") as fi:
                                        em1 = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        em = fi.readline()
                                        print(f"{em1}")
                                        print(f"{em}")

                                    with open("account_details.txt", "r") as log_namee:
                                        lo1 = log_namee.readline()
                                        lo2 = log_namee.readline()
                                        lo3 = log_namee.readline()
                                        print(f"{lo2} mm")
                                        print(f"{lo3} pass")
                                    filename = f"{nnbx}{numb}.png"
                                    sender_maill = f"{lo2}"

                                    receiver_maill = f"{em}"
                                    passwords_m = f"{lo3}"

                                    subjects = f"BOOK TRANSACTION OF {em1} Returned"
                                    bodys = f"{del_tex2} Returned on {dat_retun}"
                                    me_ssage = MIMEMultipart()
                                    me_ssage["From"] = sender_maill
                                    me_ssage["To"] = receiver_maill
                                    me_ssage["Subject"] = subjects
                                    me_ssage.attach(MIMEText(bodys, "plain"))

                                    try:
                                        with smtplib.SMTP("smtp.gmail.com", 587) as servers:
                                            servers.starttls()
                                            servers.login(sender_maill, passwords_m)
                                            servers.sendmail(sender_maill, receiver_maill, me_ssage.as_string())
                                            print("successful")
                                    except Exception as e:
                                        print(f"Error {e}")

                                    fi.close()

                                    tex.close()

                                    def clear_book():
                                        re_sen = open(f"{tallputt}transaction.txt", "w")
                                        re_sen.write("")
                                        re_sen = open(f"{tallputt}transaction.txt", "r")
                                        del_tex = re_sen.read()

                                        tex_box = customtkinter.CTkScrollableFrame(master=app4, corner_radius=32,
                                                                                   border_width=4, bg_color="black",
                                                                                   fg_color="black",
                                                                                   border_color="black",
                                                                                   scrollbar_button_color="gray",
                                                                                   scrollbar_button_hover_color="gray",
                                                                                   label_fg_color="white",
                                                                                   label_text_color="black",

                                                                                   label_font=("Arial", 20),
                                                                                   label_anchor="center",
                                                                                   orientation="vertical",
                                                                                   scrollbar_fg_color="black",
                                                                                   height=400, width=400)
                                        tex_box.place(relx=0.35, rely=0.15)
                                        customtkinter.CTkLabel(tex_box, text=del_tex, text_color="white").pack(
                                            pady=10)

                                        re_sen.close()

                                    generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72",
                                                             hover_color="pink",
                                                             border_color="black", text_color="white", text="Ok",
                                                             font=("Arial", 20, "bold"), command=clear_book)
                                    generate_but.place(relx=0.550, rely=0.75)

                                    cv2.imshow('QR scanner press Q to exit', frame)
                                    cap_vid.release()

                                    cv2.destroyWindow('QR scanner press Q to exit')
                                    return deeecod

                                cv2.imshow('QR scanner press Q to exit', frame)

                                if cv2.waitKey(1) & 0xFF == ord('q'):
                                    break

                            cap_vid.release()
                            cv2.destroyAllWindows()

                        generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72",
                                                 hover_color="pink",
                                                 border_color="black", text_color="white", text="Scan id",
                                                 font=("Arial", 20, "bold"), command=put_scan_book)
                        generate_but.place(relx=0.450, rely=0.75)

                    generate_but = CTkButton(master=app2, width=150, height=60, fg_color="#b33b72",
                                             hover_color="pink",
                                             border_color="black", text_color="white", text="Return Book",
                                             font=("Arial", 20, "bold"), command=put_book)

                    generate_but.place(relx=0.560, rely=0.75)

                    cv2.imshow('QR scanner press Q to exit', frame)
                    cap_vid.release()

                    cv2.destroyWindow('QR scanner press Q to exit')
                    return deeecod

                cv2.imshow('QR scanner press Q to exit', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap_vid.release()
            cv2.destroyAllWindows()

        generate_but = CTkButton(master=appbot_re, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Scan ID",
                                 font=("Arial", 20, "bold"), command=go_buy_put)
        generate_but.place(relx=0.440, rely=0.58)

    todays = CTkButton(master=app2, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)

    # ____________________________Get IN and OUT____________________________________________________________
    def in_and_out():

        app4 = CTkLabel(app2, image=in__out_time_img, text="")
        app4.place(relx=0.0, rely=0.0)

        global qr_contents_qr
        qrr(qr_contents_qr)

        frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                             bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                              text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)

        frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                         fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                           fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                          text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                          fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)

        detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                           text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                           fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)

        def go_buy_put_start():

            global qr_contents_qr
            qrr(qr_contents_qr)

            cap_vid = cv2.VideoCapture(0)

            while True:
                keyboard.add_hotkey('s', go_buy_put_start)
                ret, frame = cap_vid.read()
                decode_ing_vid_in_img = decode(frame)
                for deeecod in decode_ing_vid_in_img:
                    qr_contents_qr = deeecod.data.decode('utf-8')
                    qr_contents_qr = str(qr_contents_qr)
                    tex = open(f"{qr_contents_qr}.txt", "r")
                    texxll1 = tex.readline()
                    c11 = texxll1.replace("_", " ").replace("\n", "")
                    c1 = texxll1.replace(" ", "_").replace("\n", "")
                    texxll2 = tex.readline()
                    c2 = texxll2.replace(" ", "_").replace("\n", "")
                    texxll3 = tex.readline()
                    c3 = texxll3.replace(" ", "_").replace("\n", "")
                    texxll4 = tex.readline()
                    c4 = texxll4.replace(" ", "_").replace("\n", "")
                    texxll5 = tex.readline()
                    c5 = texxll5.replace(" ", " ").replace("\n", "")
                    texxll6 = tex.readline()
                    c6 = texxll6.replace(" ", " ").replace("\n", "")
                    texxll7 = tex.readline()
                    c7 = texxll7.replace(" ", " ").replace("\n", "")
                    allt = c1, c2, c3
                    allt2 = c11, c3
                    allt0enty = c11
                    allt1enty = c2
                    allt2enty = c3
                    allt3enty = c4
                    allt4enty = c5
                    allt5enty = c6
                    allt5enty = c7

                    tall = ("".join(allt))
                    tall2 = ("".join(allt2))
                    tall0 = ("".join(allt0enty))
                    tall1 = ("".join(allt1enty))
                    tall22 = ("".join(allt2enty))
                    tall33 = ("".join(allt3enty))
                    tall44 = ("".join(allt4enty))
                    tall55 = ("".join(allt5enty))
                    tall66 = ("".join(allt5enty))

                    time.sleep(2)
                    protall = Image.open(f"{tall}.png")
                    protall = CTkImage(protall, size=(250, 250))
                    pro = CTkLabel(app4, image=protall, text="")
                    pro.place(relx=0.16, rely=0.24)
                    pro = CTkLabel(app4, image=protall, text="")
                    pro.place(relx=0.16, rely=0.24)
                    tec_pro = CTkLabel(master=app4, text=tall0, fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.16, rely=0.60)

                    in_ut_dat = dt.date.today()
                    day_nam = in_ut_dat.strftime("%a ,%d %b %Y")
                    now = datetime.now()

                    hour = now.hour
                    minute = now.minute
                    second = now.second
                    re_sen = open(f"{qr_contents_qr}.txt", "a")
                    tim_fin = re_sen.write(f"{hour}:{minute}:{second}")
                    re_sen = open(f"{qr_contents_qr}.txt", "r")
                    texxll5 = re_sen.readline()
                    c5 = texxll5.replace(" ", " ").replace("\n", "")
                    texxll6 = tex.readline()
                    c6 = texxll6.replace(" ", " ").replace("\n", "")
                    texxll7 = tex.readline()
                    c7 = texxll7.replace(" ", " ").replace("\n", "")

                    re_lin_no = 7
                    re_sen_re = open(f"{qr_contents_qr}.txt", "a")
                    with open(f"{qr_contents_qr}.txt", "r") as file:
                        lines = file.readlines()
                    with open(f"{qr_contents_qr}.txt", "w") as file:
                        for i, line in enumerate(lines, start=1):
                            if i != re_lin_no:
                                file.write(line)

                    re_sen_re.close()
                    file.close()

                    tec_pro = CTkLabel(master=app4, text=f"{day_nam}", fg_color="black", text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.44, rely=0.30)
                    tec_pro = CTkLabel(master=app4, text="In Time", fg_color="green",
                                       text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.34, rely=0.36)
                    now2 = datetime.now()
                    h2 = str(now2.hour).zfill(2)

                    m2 = str(now2.minute).zfill(2)
                    s2 = str(now2.second).zfill(2)
                    open(f"{qr_contents_qr}incoming_outgoing.txt", "a")
                    open(f"{qr_contents_qr}outgoing.txt", "a")
                    open(f"{qr_contents_qr}ranking_h.txt", "a")
                    open(f"{qr_contents_qr}ranking_m.txt", "a")
                    open(f"{qr_contents_qr}ranking_s.txt", "a")

                    with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as fileot:
                        in_wait_read = fileot.readline()
                        if in_wait_read:
                            print("have")
                            with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as fileot:
                                in_wait_read_20 = fileot.readline()
                                tec_pro = CTkLabel(master=app4, text=f"{in_wait_read_20}", fg_color="green",
                                                   text_color="white", height=30,
                                                   width=250, font=("Georgia", 24))
                                tec_pro.place(relx=0.34, rely=0.40)
                        else:

                            print("not have")
                            with open(f"{qr_contents_qr}incoming_outgoing.txt", "w") as fileot:
                                fileot.write(f"{h2}:{m2}:{s2}")
                            with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as fileot:
                                in_wait_read_20 = fileot.readline()

                                tec_pro = CTkLabel(master=app4, text=f"{in_wait_read_20}", fg_color="green",
                                                   text_color="white", height=30,
                                                   width=250, font=("Georgia", 24))
                                tec_pro.place(relx=0.34, rely=0.40)

                    tec_pro = CTkLabel(master=app4, text="Out Time", fg_color="red",
                                       text_color="white", height=30,
                                       width=250, font=("Georgia", 24))
                    tec_pro.place(relx=0.54, rely=0.36)
                    now22 = datetime.now()
                    hh2 = str(now22.hour).zfill(2)

                    mm2 = str(now22.minute).zfill(2)

                    ss2 = str(now22.second).zfill(2)

                    with open(f"{qr_contents_qr}outgoing.txt", "w") as fileot:
                        fileot.write(f"{hh2}:{mm2}:{ss2}")
                    with open(f"{qr_contents_qr}outgoing.txt", "r") as fileot:

                        in_wait_read_loc = fileot.readline()

                        if in_wait_read_loc == in_wait_read_20:
                            tec_pro = CTkLabel(master=app4, text="", fg_color="red",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.54, rely=0.40)

                        else:
                            with open(f"{qr_contents_qr}outgoing.txt", "r") as fileot:
                                in_wait_read_loc_ = fileot.readline()

                            tec_pro = CTkLabel(master=app4, text=in_wait_read_loc_, fg_color="red",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.54, rely=0.40)
                            with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as linx:

                                linxs2hh = linx.readline(2)
                                linxsc = linx.readline(1)
                                linxsmm = linx.readline(2)
                                linxscc = linx.readline(1)
                                linxsss = linx.readline(2)

                                gl1 = int(linxs2hh)
                                gl2 = int(linxsmm)
                                gl3 = int(linxsss)

                            with open(f"{qr_contents_qr}outgoing.txt", "r") as linxout:
                                linxout0 = linxout.readline(2)
                                linxout1 = linxout.readline(1)
                                linxout2 = linxout.readline(2)
                                linxout3 = linxout.readline(1)
                                linxout4 = linxout.readline(2)

                                glot1 = int(linxout0)
                                glot2 = int(linxout2)
                                glot3 = int(linxout4)

                                total1 = gl1 - glot1
                                total2 = gl2 - glot2
                                total3 = gl3 - glot3
                                total_str1 = str(total1)
                                total_str2 = str(total2)
                                total_str3 = str(total3)
                                tot1 = total_str1.replace("-", "")
                                tot2 = total_str2.replace("-", "")
                                tot3 = total_str3.replace("-", "")
                                tot11 = int(tot1)
                                tot22 = int(tot2)
                                tot33 = int(tot3)

                            with open(f"{qr_contents_qr}ranking_h.txt", "a") as rank:
                                rank.write(f"{int(tot11):02}\n")
                            with open(f"{qr_contents_qr}ranking_m.txt", "a") as rank:
                                rank.write(f"{int(tot22):02}\n")
                            with open(f"{qr_contents_qr}ranking_s.txt", "a") as rank:
                                rank.write(f"{int(tot33):02}\n")

                            with open(f"{qr_contents_qr}ranking_h.txt", "r") as rank:

                                rankk_h = rank.read()
                                numbers = [int(num) for num in rankk_h.split() if num.isdigit()]
                                aa_h = sum(numbers)
                                print(aa_h)

                            with open(f"{qr_contents_qr}ranking_m.txt", "r") as rank:
                                rankk_m = rank.read()
                                numbers = [int(num) for num in rankk_m.split() if num.isdigit()]
                                aa_m = sum(numbers)
                                print(aa_m)

                            with open(f"{qr_contents_qr}ranking_s.txt", "r") as rank:
                                rankk_sp = rank.read()

                                numbers = [int(num) for num in rankk_sp.split() if num.isdigit()]
                                aa_s = sum(numbers)
                                print(aa_s)
                            tec_pro = CTkLabel(master=app4, text=f"{tot11}:{tot22}:{tot33}", fg_color="#950995",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.34, rely=0.60)
                            tec_pro = CTkLabel(master=app4, text=f"Current Duration", fg_color="#950995",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.34, rely=0.55)
                            tec_pro = CTkLabel(master=app4, text=f"{aa_h}:{aa_m}:{aa_s}", fg_color="#27B78E",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.54, rely=0.60)
                            tec_pro = CTkLabel(master=app4, text=f"Total Duration", fg_color="#27B78E",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.54, rely=0.55)

                            open(f"{qr_contents_qr}ranking.txt", "a")

                            re_lin_no = 1

                            with open(f"{qr_contents_qr}outgoing.txt", "r") as file:
                                lines = file.readlines()
                            with open(f"{qr_contents_qr}outgoing.txt", "w") as file:
                                for i, line in enumerate(lines, start=1):
                                    if i != re_lin_no:
                                        file.write(line)

                            re_sen_re.close()
                            file.close()
                            re_lin_no = 1

                            with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as file:
                                lines = file.readlines()
                            with open(f"{qr_contents_qr}incoming_outgoing.txt", "w") as file:
                                for i, line in enumerate(lines, start=1):
                                    if i != re_lin_no:
                                        file.write(line)

                            re_sen_re.close()
                            file.close()
                            rank.close()

                cv2.imshow('QR scanner press x to exit', frame)
                if keyboard.is_pressed('x'):
                    exit(cv2)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap_vid.release()

            cv2.destroyAllWindows()

        generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Start Scan",
                                 font=("Arial", 20, "bold"), command=go_buy_put_start)
        generate_but.place(relx=0.150, rely=0.764)

    clock = CTkButton(master=app2, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
    clock.place(rely=0.864, relx=0.57)

    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=app2, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)

    # login details_____________________________________________login_part________________________________________________login_setup_
    def loogin_setup():

        app4 = CTkLabel(app2, image=login_lib, text="")
        app4.place(relx=0.0, rely=0.0)

        global qr_contents_qr
        qrr(qr_contents_qr)

        frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                             bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                              text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)

        frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                         fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2, command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                           fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                          text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                          fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)

        detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                           text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                           fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)

        def cam_img():
            global fils

            fils = askopenfiles("rb", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                                title="Upload File")

            fils = Image.open(fils[0])

            fils = CTkImage(fils, size=(250, 250))

            name_label = CTkLabel(master=app4, image=fils, text="", font=("Georgia", 34, "bold"), text_color="white",
                                  bg_color="black", anchor="center")
            name_label.place(rely=0.269, relx=0.17)

        detail = CTkButton(master=app4, image=cam, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="blue",
                           bg_color="transparent", border_color="black", border_width=2, command=cam_img)
        detail.place(rely=0.600, relx=0.22)
        datlbl = CTkLabel(master=app4, text_color="white", text="LIBRARY NAME", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=30, width=75, corner_radius=32, bg_color="black")
        datlbl.place(relx=0.40, rely=0.290)
        lib_name = CTkEntry(master=app4, placeholder_text="Enter Library Name", fg_color="white", border_color="black",
                            border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        lib_name.place(relx=0.40, rely=0.340)
        mail = CTkLabel(master=app4, text_color="white", text="E-Mail ID", fg_color="black",
                        font=("Arial", 24, "bold"),
                        height=30, width=75, corner_radius=32, bg_color="black")
        mail.place(relx=0.40, rely=0.425)
        mail = CTkEntry(master=app4, placeholder_text="Enter E-Mail", fg_color="white", border_color="black",
                        border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        mail.place(relx=0.40, rely=0.470)
        datlbl = CTkLabel(master=app4, text_color="white", text="Password", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=30, width=75, corner_radius=32, bg_color="black")
        datlbl.place(relx=0.40, rely=0.550)
        password = CTkEntry(master=app4, placeholder_text="Enter Mail Password", fg_color="white", border_color="black",
                            border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        password.place(relx=0.40, rely=0.595)
        mobile = CTkLabel(master=app4, text_color="white", text="Mobile No", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=30, width=75, corner_radius=32, bg_color="black")
        mobile.place(relx=0.40, rely=0.672)
        mobile = CTkEntry(master=app4, placeholder_text="Enter Mobile No", fg_color="white", border_color="black",
                          border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
        mobile.place(relx=0.40, rely=0.717)

        def login_set_in_txt():
            na_log()
            global name_is
            name_is = lib_name.get()
            mail_is = mail.get()
            password_is = password.get()
            mobile_is = mobile.get()

            name_is = name_is.replace(" ", "_").replace(".", "").replace(",", "")
            open(f"{name_is}.txt", "a")
            open("account_details.txt", "a")
            with open(f"{name_is}.txt", "w") as log_name:
                log_name.write(f"{name_is}\n{mail_is}\n{password_is}\n{mobile_is}")

            region = (330, 313, 308, 311)
            screen_shot = pyautogui.screenshot(region=region)
            screen_shot.save(f"{name_is}.png")
            with open(f"{name_is}.txt", "r") as log_name:
                lo_na = log_name.read()

            with open("account_details.txt", "w") as log_name:
                log_name.write(lo_na)
            with open("account_details.txt", "r") as log_name:
                new_org_nam = log_name.readline().replace("\n", "")

            with open(f"{new_org_nam}.txt", "r") as log_name:
                pr_new_log = log_name.read()
                print(pr_new_log)

            log_name.close()

        detail = CTkButton(master=app4, hover_color="dark blue", text="Save",
                           text_color="white", height=40, width=100, font=("Arial", 20, "bold"), fg_color="blue",
                           bg_color="transparent", command=login_set_in_txt)
        detail.place(rely=0.72, relx=0.665)

    detail = CTkButton(master=app2, image=details, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)

    app2.mainloop()


with open("account_details.txt", "r") as log_name:
    pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
    pr_new_log = str(pr_new_log)
with open("account_details.txt", "r") as log_name:
    pr_new_log_img = log_name.readline().replace("\n", "")

app2 = Tk()
app2.geometry("1080x1080")
app2.title("LIBRARY MANAGEMENT")
app2.wm_state('zoomed')
app2.wm_iconbitmap("iconlib.ico")





moon = CTkLabel(app2, image=wall, text="")
moon.place(relx=0.0, rely=0.0)
frame_top = CTkFrame(master=app2, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                     fg_color="black", border_color="black")
frame_top.place(relx=0, rely=0)

name_label = CTkLabel(master=app2, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                      bg_color="black", anchor="center")
name_label.place(rely=0.02, relx=0.04)
lo_na_png = Image.open(f"{pr_new_log_img}.png")
lo_na_png = CTkImage(lo_na_png, size=(50, 50))

namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                  font=("Arial", 24, "bold"),
                  height=50, width=50, corner_radius=32, bg_color="black")
namlbl.place(relx=0.88, rely=0.01)
frame = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="white", fg_color="black")
frame.place(rely=0.860, relx=0.27)
def des_t():
    app2.destroy()
search_btn = CTkButton(master=app2, image=search, hover_color="grey", height=50, width=50, text="", fg_color="black",
                       bg_color="black",command=des_t)
search_btn.place(rely=0.01, relx=0.95)



def members():

    app3 = CTkLabel(app2, image=lib__member, text="")
    app3.place(relx=0.0, rely=0.0)
    frame_top = CTkFrame(master=app3, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)
    with open("account_details.txt", "r") as log_name:
        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
        pr_new_log = str(pr_new_log)
    with open("account_details.txt", "r") as log_name:
        pr_new_log_img = log_name.readline().replace("\n", "")

    name_label = CTkLabel(master=app3, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))
    namlbl = CTkLabel(master=app3, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=app3, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)

    frame = CTkFrame(master=app3, width=700, height=50, corner_radius=12, bg_color="transparent", fg_color="black")
    frame.place(rely=0.860, relx=0.27)

    home = CTkButton(master=app3, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
    home.place(rely=0.864, relx=0.30)
    todays = CTkButton(master=app3, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)
    clock = CTkButton(master=app3, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
    clock.place(rely=0.864, relx=0.57)
    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=app3, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)
    detail = CTkButton(master=app3, image=details, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)
    namlbl = CTkLabel(master=app3, text_color="white", text="Name", fg_color="black", font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.170, rely=0.26)
    namebx = CTkEntry(master=app3, placeholder_text="Name", fg_color="white", border_color="black",
                      border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    namebx.place(relx=0.170, rely=0.3)
    datlbl = CTkLabel(master=app3, text_color="white", text="DOB", fg_color="black", font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    datlbl.place(relx=0.170, rely=0.46)
    dat = CTkEntry(master=app3, placeholder_text="DD/MM/YYYY", fg_color="white", border_color="black",
                   border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    dat.place(relx=0.170, rely=0.5)
    droplist = CTkLabel(master=app3, text_color="white", text="About", fg_color="black", font=("Arial", 24, "bold"),
                        height=30, width=75, corner_radius=32, bg_color="black")
    droplist.place(relx=0.170, rely=0.639)
    Iam = CTkComboBox(master=app3, width=350, height=60, corner_radius=0, fg_color="white", dropdown_fg_color="white",
                      dropdown_hover_color="pink", dropdown_text_color="black",
                      values=["  ", "Student", "Working Professional", "Others"], button_color="black",
                      text_color="grey", font=("Arial", 20, "bold"))
    Iam.place(relx=0.170, rely=0.68)
    droplist_gen = CTkLabel(master=app3, text_color="white", text="Gender", fg_color="black",
                            font=("Arial", 24, "bold"),
                            height=30, width=75, corner_radius=32, bg_color="black")
    droplist_gen.place(relx=0.470, rely=0.26)

    datem = CTkEntry(master=app3, placeholder_text="example@gmail.com", fg_color="white", border_color="black",
                   border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")

    datem.place(relx=0.470, rely=0.56)

    namlblem = CTkLabel(master=app3, text_color="white", text="Gmail", fg_color="black", font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    namlblem.place(relx=0.470, rely=0.52)


    def vis_card():
        global mr_mrs
        global nbx
        global numb
        global fils
        global tex_l
        global an_nbxx
        global san_nbxx
        dat_ion()

        app4 = CTkLabel(app2, image=wall, text="")
        app4.place(relx=0.0, rely=0.0)
        frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)

        frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2,command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)

        detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)
        card_lib = CTkLabel(master=app4, image=id_vis, text="")
        card_lib.place(rely=0.2, relx=0.240)
        card_lib = CTkLabel(master=app4, image=fils, text="")
        card_lib.place(rely=0.3, relx=0.250)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 30, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.225, relx=0.260)
        nbx = namebx.get()
        dbx = dat.get()
        dbx.replace("/", "").replace("-", "").replace(" ", "")
        namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        name_nbx = CTkLabel(master=app4, text=f"{nbx}", font=("Georgia", 20, "bold"), text_color="black",
                            bg_color="#ffff66", anchor="center")
        name_nbx.place(rely=0.600, relx=0.290)

        if mr_mrs == "Male":
            name_gbx = CTkLabel(master=app4, text="Mr.", font=("Georgia", 20, "bold"), text_color="black",
                                bg_color="#ffff66", anchor="center")
            name_gbx.place(rely=0.600, relx=0.265)
        elif mr_mrs == "Female":
            name_gbx = CTkLabel(master=app4, text="Mrs.", font=("Georgia", 20, "bold"), text_color="black",
                                bg_color="#ffff66", anchor="center")
            name_gbx.place(rely=0.600, relx=0.260)

        selll = Iam.get()
        numb = int(con.get())
        emaill = datem.get()


        san_nbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")
        content = f"{nbx}\n{mr_mrs}\n{numb}\n{dbx}\n{selll}\n{dat_join}\n{emaill}"
        content2 = f"{nbx}{mr_mrs}{numb}{dbx}\n{selll}"
        text = open(f"{nbx}{numb}.txt", "w")

        text2 = open(f"{nbx}{numb}2.txt", "w")


        text.write(content)
        text2.write(content2)

        text.close()
        text2.close()

        contents = f"{nbx}{numb}"
        qr = pyqrcode.create(contents)
        qr.png(f"{san_nbx}.png", scale=6)
        img = Image.open(f"{san_nbx}.png")
        img = CTkImage(img, size=(200, 200))
        qqr = CTkLabel(app4, image=img, text="")
        qqr.place(relx=0.580, rely=0.350)

        generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Save",
                                 font=("Arial", 20, "bold"), command=com_vis)
        generate_but.place(relx=0.665, rely=0.72)
        tex = open(f"{nbx}{numb}.txt", "r")

        tex.close()

    def com_vis():

        roott = Toplevel(app2)
        roott.withdraw()
        global nbx
        global nnbx
        global dat_join

        nnbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")

        file_path = asksaveasfilename(defaultextension=".png",
                                      filetypes=[("PNG files", "*.png"), ("All files", "*.*")], title="Save As",
                                      initialfile=f"{nnbx}{numb}")
        region = (470, 250, 990, 465)
        screen_shot = pyautogui.screenshot(region=region)

        screen_shot.save(file_path)
        screen_shot.save(f"{nnbx}{numb}.png")
        region = (481, 344, 311, 311)
        screen_shot = pyautogui.screenshot(region=region)
        screen_shot.save(f"{nnbx}{mr_mrs}{numb}.png")
        #_________________________________________MAIL___________________________Automate_________________________________
        with open(f"{nbx}{numb}.txt", "r") as fi:
            em1 = fi.readline()
            em = fi.readline()
            em = fi.readline()
            em = fi.readline()
            em = fi.readline()
            em = fi.readline()
            em = fi.readline()
            print(f"{em1}")
            print(f"{em}")

        with open("account_details.txt", "r") as log_namee:
            lo1 = log_namee.readline()
            lo2 = log_namee.readline()
            lo3 = log_namee.readline()
            print(f"{lo2} mm")
            print(f"{lo3} pass")
        filename = f"{nnbx}{numb}.png"
        sender_maill = f"{lo2}"

        receiver_maill = f"{em}"
        passwords_m = f"{lo3}"

        subjects = "ID CARD"
        bodys = f"{em1} Here is your virtual library id card"
        me_ssage = MIMEMultipart()
        me_ssage["From"] = sender_maill
        me_ssage["To"] = receiver_maill
        me_ssage["Subject"] = subjects
        try:
            with open(filename, "rb") as attach_img:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attach_img.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment;filename={filename}")
                me_ssage.attach(part)
        except Exception as e:
            print(f"Error : {e}")

        me_ssage.attach(MIMEText(bodys, "plain"))
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as servers:
                servers.starttls()
                servers.login(sender_maill, passwords_m)
                servers.sendmail(sender_maill, receiver_maill, me_ssage.as_string())
                print("successful")
        except Exception as e:
            print(f"Error {e}")

        fi.close()

    gen = CTkComboBox(master=app3, width=350, height=60, corner_radius=0, fg_color="white",
                      dropdown_fg_color="white", dropdown_hover_color="pink", dropdown_text_color="black",
                      values=["  ", "Male", "Female", "Others"], button_color="black", text_color="grey",
                      font=("Arial", 20, "bold"), command=glo_var)

    gen.place(relx=0.470, rely=0.3)
    droplist_con = CTkLabel(master=app3, text_color="white", text="Contact", fg_color="black",
                            font=("Arial", 24, "bold"),
                            height=30, width=75, corner_radius=32, bg_color="black")
    droplist_con.place(relx=0.470, rely=0.39)
    con = CTkEntry(master=app3, placeholder_text="Mobile NO", fg_color="white", border_color="black",
                   border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    con.place(relx=0.470, rely=0.43)

    generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Image",
                             font=("Arial", 20, "bold"), image=upload, command=img)
    generate_but.place(relx=0.415, rely=0.68)

    generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Generate ID ✨", font=("Arial", 20, "bold"),
                             command=vis_card)
    generate_but.place(relx=0.600, rely=0.68)

    app3.mainloop()


def add_books():

    app3 = CTkLabel(app2, image=book_try, text="")
    app3.place(relx=0.0, rely=0.0)
    frame_top = CTkFrame(master=app3, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)
    with open("account_details.txt", "r") as log_name:
        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
        pr_new_log = str(pr_new_log)
    with open("account_details.txt", "r") as log_name:
        pr_new_log_img = log_name.readline().replace("\n", "")
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

    name_label = CTkLabel(master=app3, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    namlbl = CTkLabel(master=app3, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=app3, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)

    frame = CTkFrame(master=app3, width=700, height=50, corner_radius=12, bg_color="transparent",
                     fg_color="black")
    frame.place(rely=0.860, relx=0.27)
    home = CTkButton(master=app3, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
    home.place(rely=0.864, relx=0.30)
    todays = CTkButton(master=app3, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)
    clock = CTkButton(master=app3, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
    clock.place(rely=0.864, relx=0.57)
    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=app3, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)

    detail = CTkButton(master=app3, image=details, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)
    namlbl = CTkLabel(master=app3, text_color="white", text="BOOK NAME", fg_color="black",
                      font=("Arial", 24, "bold"), height=30, width=75, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.170, rely=0.26)
    namebx = CTkEntry(master=app3, placeholder_text="BOOK NAME", fg_color="white", border_color="black",
                      border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    namebx.place(relx=0.170, rely=0.3)
    datlbl = CTkLabel(master=app3, text_color="white", text="CODE", fg_color="black", font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    datlbl.place(relx=0.170, rely=0.46)
    datt = CTkEntry(master=app3, placeholder_text="0000...", fg_color="white", border_color="black",
                    border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    datt.place(relx=0.170, rely=0.5)

    def vis_card():
        global mr_mrs
        global nbx
        global numb
        global for_num_abx

        app4 = CTkLabel(app2, image=wall, text="")
        app4.place(relx=0.0, rely=0.0)
        frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                             fg_color="black", border_color="black")
        frame_top.place(relx=0, rely=0)
        with open("account_details.txt", "r") as log_name:
            pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
            pr_new_log = str(pr_new_log)
        with open("account_details.txt", "r") as log_name:
            pr_new_log_img = log_name.readline().replace("\n", "")
        lo_na_png = Image.open(f"{pr_new_log_img}.png")
        lo_na_png = CTkImage(lo_na_png, size=(50, 50))

        name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.02, relx=0.04)
        namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=50, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.88, rely=0.01)

        def des_t():
            app2.destroy()

        search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                               fg_color="black",
                               bg_color="black", command=des_t)
        search_btn.place(rely=0.01, relx=0.95)

        frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                         fg_color="black")
        frame.place(rely=0.860, relx=0.27)
        home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                         text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                         bg_color="transparent", border_color="black", border_width=2,command=home_pg)
        home.place(rely=0.864, relx=0.30)
        todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
        todays.place(rely=0.864, relx=0.39)
        clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                          text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                          bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
        clock.place(rely=0.864, relx=0.57)
        now_upp = datetime.now().strftime("%A")

        namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                          font=("Brush Script MT", 34, "bold"),
                          height=49, width=50, corner_radius=32, bg_color="black")
        namlbl.place(relx=0.44, rely=0.860)
        detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue", text="",
                           text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                           bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
        detail.place(rely=0.864, relx=0.66)

        nbx = namebx.get()
        for_num_abx = int(datt.get())

        san_nbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")
        content = f"Book Name : {nbx}\nCode : {for_num_abx}"
        qr = pyqrcode.create(content)
        qr.png(f"{san_nbx}{for_num_abx}.png", scale=6)
        img = Image.open(f"{san_nbx}{for_num_abx}.png")
        img = CTkImage(img, size=(200, 200))
        qqr = CTkLabel(app4, image=img, text="")
        qqr.place(relx=0.430, rely=0.350)
        generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                                 border_color="black", text_color="white", text="Save",
                                 font=("Arial", 20, "bold"), command=com_vis)
        generate_but.place(relx=0.445, rely=0.72)

    def com_vis():

        roott = Toplevel(app2)
        roott.withdraw()
        global nbx
        global nnbx
        global for_num_abx
        nnbx = nbx.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(".", "_")

        file_path = asksaveasfilename(defaultextension=".png",
                                      filetypes=[("PNG files", "*.png"), ("All files", "*.*")], title="Save As",
                                      initialfile=f"{nnbx}{for_num_abx}")
        region = (830, 400, 245, 245)
        screen_shot = pyautogui.screenshot(region=region)
        if file_path:
            screen_shot.save(file_path)

        else:
            print("canceled")

    generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Generate ID ✨", font=("Arial", 20, "bold"),
                             command=vis_card)
    generate_but.place(relx=0.600, rely=0.68)

    generate_but = CTkButton(master=app3, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Generate QR ✨",
                             font=("Arial", 20, "bold"), command=vis_card)
    generate_but.place(relx=0.600, rely=0.68)

    app3.mainloop()


members = CTkButton(master=app2, image=add_members, corner_radius=32, hover_color="white", text="", text_color="black",
                    height=200, width=200, font=("Arial", 40, "bold"), fg_color="sky blue", bg_color="dark blue",
                    border_color="dark blue", border_width=4, command=members)
members.place(rely=0.3, relx=0.1)

book = CTkButton(master=app2, image=books, corner_radius=32, hover_color="white", text="",
                 text_color="black", height=200, width=200, font=("Arial", 40, "bold"), fg_color="light green",
                 bg_color="dark green", border_color="dark green", border_width=4, command=add_books)
book.place(rely=0.3, relx=0.4)


def bought_return():

    appbot_re = CTkLabel(app2, image=libboard_bought_return_scan_instead, text="")
    appbot_re.place(relx=0.0, rely=0.0)
    frame_top = CTkFrame(master=appbot_re, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)
    with open("account_details.txt", "r") as log_name:
        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
        pr_new_log = str(pr_new_log)
    with open("account_details.txt", "r") as log_name:
        pr_new_log_img = log_name.readline().replace("\n", "")
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

    name_label = CTkLabel(master=appbot_re, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    namlbl = CTkLabel(master=appbot_re, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=appbot_re, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)
    frame = CTkFrame(master=appbot_re, width=700, height=50, corner_radius=12, bg_color="transparent",
                     fg_color="black")
    frame.place(rely=0.860, relx=0.27)
    home = CTkButton(master=appbot_re, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
    home.place(rely=0.864, relx=0.30)
    todays = CTkButton(master=appbot_re, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)
    clock = CTkButton(master=appbot_re, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
    clock.place(rely=0.864, relx=0.57)
    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=appbot_re, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)
    detail = CTkButton(master=appbot_re, image=details, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)

    def retrive_details():
        global tex_l
        global qr_contents_qr
        global an_nbxx
        global san_nbxx
        global protall

        qrr(qr_contents_qr)

        cap_vid = cv2.VideoCapture(0)
        while True:
            ret, frame = cap_vid.read()
            decode_ing_vid_in_img = decode(frame)
            for deeecod in decode_ing_vid_in_img:
                qr_contents_qr = deeecod.data.decode('utf-8')
                qr_contents_qr = str(qr_contents_qr)
                tex = open(f"{qr_contents_qr}.txt", "r")
                texxll1 = tex.readline()
                c11 = texxll1.replace("_", " ").replace("\n", "")
                c1 = texxll1.replace(" ", "_").replace("\n", "")
                texxll2 = tex.readline()
                c2 = texxll2.replace(" ", "_").replace("\n", "")
                texxll3 = tex.readline()
                c3 = texxll3.replace(" ", "_").replace("\n", "")
                texxll4 = tex.readline()
                c4 = texxll4.replace(" ", "_").replace("\n", "")
                texxll5 = tex.readline()
                c5 = texxll5.replace(" ", " ").replace("\n", "")
                texxll6 = tex.readline()
                c6 = texxll6.replace(" ", " ").replace("\n", "")
                allt = c1, c2, c3
                allt2 = c11, c3
                allt0enty = c11
                allt1enty = c2
                allt2enty = c3
                allt3enty = c4
                allt4enty = c5
                allt5enty = c6
                tall = ("".join(allt))
                tall2 = ("".join(allt2))
                tall0 = ("".join(allt0enty))
                tall1 = ("".join(allt1enty))
                tall22 = ("".join(allt2enty))
                tall33 = ("".join(allt3enty))
                tall44 = ("".join(allt4enty))
                tall55 = ("".join(allt5enty))

                tex.close()


                app2n = CTkLabel(app2, image=libboard_bought_return, text="")
                app2n.place(relx=0.0, rely=0.0)
                frame_top = CTkFrame(master=app2n, width=2000, height=81, corner_radius=0, border_width=2,
                                     bg_color="white", fg_color="black", border_color="black")
                frame_top.place(relx=0, rely=0)

                with open("account_details.txt", "r") as log_name:
                    pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                    pr_new_log = str(pr_new_log)
                with open("account_details.txt", "r") as log_name:
                    pr_new_log_img = log_name.readline().replace("\n", "")
                lo_na_png = Image.open(f"{pr_new_log_img}.png")
                lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                name_label = CTkLabel(master=app2, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                      text_color="white", bg_color="black", anchor="center")
                name_label.place(rely=0.02, relx=0.04)
                namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                                  font=("Arial", 24, "bold"),
                                  height=50, width=50, corner_radius=32, bg_color="black")
                namlbl.place(relx=0.88, rely=0.01)

                def des_t():
                    app2.destroy()

                search_btn = CTkButton(master=app2, image=search, hover_color="grey", height=50, width=50, text="",
                                       fg_color="black",
                                       bg_color="black", command=des_t)
                search_btn.place(rely=0.01, relx=0.95)
                framee = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="transparent",
                                  fg_color="black")
                framee.place(rely=0.860, relx=0.27)
                home = CTkButton(master=app2, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                 text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                 fg_color="black",
                                 bg_color="transparent", border_color="black", border_width=2,command=home_pg)
                home.place(rely=0.864, relx=0.30)
                todays = CTkButton(master=app2, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                   text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                   fg_color="black",
                                   bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
                todays.place(rely=0.864, relx=0.39)
                clock = CTkButton(master=app2, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                                  text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                  fg_color="black",
                                  bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
                clock.place(rely=0.864, relx=0.57)
                now_upp = datetime.now().strftime("%A")

                namlbl = CTkLabel(master=app2, text_color="black", text=now_upp, fg_color="white",
                                  font=("Brush Script MT", 34, "bold"),
                                  height=49, width=50, corner_radius=32, bg_color="black")
                namlbl.place(relx=0.44, rely=0.860)
                detail = CTkButton(master=app2, image=details, corner_radius=100, hover_color="dark blue", text="",
                                   text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                   fg_color="black",
                                   bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
                detail.place(rely=0.864, relx=0.66)

                protall = Image.open(f"{tall}.png")
                protall = CTkImage(protall, size=(250, 250))

                pro = CTkLabel(app2, image=protall, text="")
                pro.place(relx=0.16, rely=0.24)

                tec_pro = CTkLabel(master=app2, text=tall0, fg_color="black", text_color="white", height=30, width=250,
                                   font=("Georgia", 24))
                tec_pro.place(relx=0.16, rely=0.60)
                tec_pro = CTkLabel(master=app2, text="Name", fg_color="pink", bg_color="black", text_color="black",
                                   height=40,
                                   width=80, font=("Georgia", 19))
                tec_pro.place(relx=0.16, rely=0.55)
                tec_pro = CTkLabel(master=app2, text=tall1, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.16, rely=0.70)
                tec_pro = CTkLabel(master=app2, text="Gender", fg_color="pink", bg_color="black", text_color="black",
                                   height=40,
                                   width=80, font=("Georgia", 19))
                tec_pro.place(relx=0.16, rely=0.65)
                tec_pro = CTkLabel(master=app2, text=tall22, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.52, rely=0.34)
                tec_pro = CTkLabel(master=app2, text="Contact", fg_color="pink", bg_color="black",
                                   text_color="black",
                                   height=40,
                                   width=80, font=("Georgia", 19))
                tec_pro.place(relx=0.52, rely=0.29)
                tec_pro = CTkLabel(master=app2, text=tall33, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.52, rely=0.44)
                tec_pro = CTkLabel(master=app2, text="DOB", fg_color="pink", bg_color="black",
                                   text_color="black",
                                   height=40,
                                   width=80, font=("Georgia", 19))
                tec_pro.place(relx=0.52, rely=0.39)
                tec_pro = CTkLabel(master=app2, text=tall44, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.52, rely=0.54)
                tec_pro = CTkLabel(master=app2, text="About", fg_color="pink", bg_color="black",
                                   text_color="black",
                                   height=40,
                                   width=80, font=("Georgia", 19))
                tec_pro.place(relx=0.52, rely=0.49)
                tec_pro = CTkLabel(master=app2, text=tall55, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.52, rely=0.64)
                tec_pro = CTkLabel(master=app2, text="Joined On", fg_color="pink", bg_color="black",
                                   text_color="black",
                                   height=40,
                                   width=80, font=("Georgia", 19))
                tec_pro.place(relx=0.52, rely=0.59)

                cv2.imshow('QR scanner press Q to exit', frame)
                cap_vid.release()

                cv2.destroyWindow('QR scanner press Q to exit')
                return deeecod

            cv2.imshow('QR scanner press Q to exit', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap_vid.release()
        cv2.destroyAllWindows()

    generate_but = CTkButton(master=appbot_re, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Scan ID",
                             font=("Arial", 20, "bold"), command=retrive_details)
    generate_but.place(relx=0.440, rely=0.58)


user = CTkButton(master=app2, image=users, corner_radius=32, hover_color="white", text="",
                 text_color="black", height=200, width=200, font=("Arial", 40, "bold"), fg_color="light pink",
                 bg_color="red", border_color="red", border_width=4, command=bought_return)
user.place(rely=0.3, relx=0.7)
frame = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="transparent", fg_color="black")
frame.place(rely=0.860, relx=0.27)
home = CTkButton(master=app2, image=homes, corner_radius=100, hover_color="dark blue", text="",
                 text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                 bg_color="transparent", border_color="black", border_width=2,command=home_pg)
home.place(rely=0.864, relx=0.30)


def getbook_putbook():

    appbot_re = CTkLabel(app2, image=libboard_bought_return_scan, text="")
    appbot_re.place(relx=0.0, rely=0.0)
    frame_top = CTkFrame(master=appbot_re, width=2000, height=81, corner_radius=0, border_width=2, bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)
    with open("account_details.txt", "r") as log_name:
        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
        pr_new_log = str(pr_new_log)
    with open("account_details.txt", "r") as log_name:
        pr_new_log_img = log_name.readline().replace("\n", "")
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

    name_label = CTkLabel(master=appbot_re, text=f"{pr_new_log}", font=("Georgia", 34, "bold"), text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    namlbl = CTkLabel(master=appbot_re, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=appbot_re, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)
    frame = CTkFrame(master=appbot_re, width=700, height=50, corner_radius=12, bg_color="transparent",
                     fg_color="black")
    frame.place(rely=0.860, relx=0.27)
    home = CTkButton(master=appbot_re, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
    home.place(rely=0.864, relx=0.30)
    todays = CTkButton(master=appbot_re, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)
    clock = CTkButton(master=appbot_re, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
    clock.place(rely=0.864, relx=0.57)
    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=appbot_re, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)

    detail = CTkButton(master=appbot_re, image=details, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)

    def go_buy_put():
        global tex_l
        global qr_contents_qr
        global an_nbxx
        global san_nbxx
        global protall

        qrr(qr_contents_qr)

        cap_vid = cv2.VideoCapture(0)
        while True:
            ret, frame = cap_vid.read()
            decode_ing_vid_in_img = decode(frame)
            for deeecod in decode_ing_vid_in_img:
                qr_contents_qr = deeecod.data.decode('utf-8')
                qr_contents_qr = str(qr_contents_qr)
                tex = open(f"{qr_contents_qr}.txt", "r")
                texxll1 = tex.readline()
                c11 = texxll1.replace("_", " ").replace("\n", "")

                c1 = texxll1.replace(" ", "_").replace("\n", "")
                texxll2 = tex.readline()
                c2 = texxll2.replace(" ", "_").replace("\n", "")
                texxll3 = tex.readline()
                c3 = texxll3.replace(" ", "_").replace("\n", "")

                allt = c1, c2, c3
                tall_tall2 = c1,c3
                allt0enty = c11
                tall = ("".join(allt))
                tall_tall = ("".join(tall_tall2)).replace("_"," ")
                tall0 = ("".join(allt0enty))


                app2n = CTkLabel(app2, image=libboard_bought_return200, text="")
                app2n.place(relx=0.0, rely=0.0)
                frame_top = CTkFrame(master=app2, width=2000, height=81, corner_radius=0, border_width=2,
                                     bg_color="white", fg_color="black", border_color="black")
                frame_top.place(relx=0, rely=0)

                with open("account_details.txt", "r") as log_name:
                    pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                    pr_new_log = str(pr_new_log)
                with open("account_details.txt", "r") as log_name:
                    pr_new_log_img = log_name.readline().replace("\n", "")
                lo_na_png = Image.open(f"{pr_new_log_img}.png")
                lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                name_label = CTkLabel(master=app2, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                      text_color="white", bg_color="black", anchor="center")
                name_label.place(rely=0.02, relx=0.04)
                namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                                  font=("Arial", 24, "bold"),
                                  height=50, width=50, corner_radius=32, bg_color="black")
                namlbl.place(relx=0.88, rely=0.01)

                def des_t():
                    app2.destroy()

                search_btn = CTkButton(master=app2, image=search, hover_color="grey", height=50, width=50, text="",
                                       fg_color="black",
                                       bg_color="black", command=des_t)
                search_btn.place(rely=0.01, relx=0.95)
                framee = CTkFrame(master=app2, width=700, height=50, corner_radius=12, bg_color="transparent",
                                  fg_color="black")
                framee.place(rely=0.860, relx=0.27)
                home = CTkButton(master=app2, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                 text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                 fg_color="black",
                                 bg_color="transparent", border_color="black", border_width=2,command=home_pg)
                home.place(rely=0.864, relx=0.30)
                todays = CTkButton(master=app2, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                   text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                   fg_color="black",
                                   bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
                todays.place(rely=0.864, relx=0.39)
                clock = CTkButton(master=app2, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                                  text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                  fg_color="black",
                                  bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
                clock.place(rely=0.864, relx=0.57)
                now_upp = datetime.now().strftime("%A")

                namlbl = CTkLabel(master=app2, text_color="black", text=now_upp, fg_color="white",
                                  font=("Brush Script MT", 34, "bold"),
                                  height=49, width=50, corner_radius=32, bg_color="black")
                namlbl.place(relx=0.44, rely=0.860)

                detail = CTkButton(master=app2, image=details, corner_radius=100, hover_color="dark blue", text="",
                                   text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                   fg_color="black",
                                   bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
                detail.place(rely=0.864, relx=0.66)
                protall = Image.open(f"{tall}.png")
                protall = CTkImage(protall, size=(250, 250))

                pro = CTkLabel(app2, image=protall, text="")
                pro.place(relx=0.41, rely=0.29)
                tec_pro = CTkLabel(master=app2, text=tall0, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.41, rely=0.60)

                def get_book():

                    app4 = CTkLabel(app2, image=wall, text="")
                    app4.place(relx=0.0, rely=0.0)
                    frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                                         bg_color="white",
                                         fg_color="black", border_color="black")
                    frame_top.place(relx=0, rely=0)
                    # returninng date------------------------
                    dat = CTkEntry(master=app4, placeholder_text="Return YYYY-MM-DD", fg_color="white",
                                   border_color="black",
                                   border_width=2, height=60, width=350, font=("Arial", 20, "bold"),
                                   text_color="black", bg_color="black")

                    dat.place(relx=0.0, rely=0.1)
                    with open("account_details.txt", "r") as log_name:
                        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                        pr_new_log = str(pr_new_log)
                    with open("account_details.txt", "r") as log_name:
                        pr_new_log_img = log_name.readline().replace("\n", "")
                    lo_na_png = Image.open(f"{pr_new_log_img}.png")
                    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                    name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                          text_color="white",
                                          bg_color="black", anchor="center")
                    name_label.place(rely=0.02, relx=0.04)
                    namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                                      font=("Arial", 24, "bold"),
                                      height=50, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.88, rely=0.01)

                    def des_t():
                        app2.destroy()

                    search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                                           fg_color="black",
                                           bg_color="black", command=des_t)
                    search_btn.place(rely=0.01, relx=0.95)
                    frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                                     fg_color="black")
                    frame.place(rely=0.860, relx=0.27)
                    home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                     fg_color="black",
                                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
                    home.place(rely=0.864, relx=0.30)
                    todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
                    todays.place(rely=0.864, relx=0.39)
                    clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                                      text="",
                                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                      fg_color="black",
                                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
                    clock.place(rely=0.864, relx=0.57)
                    now_upp = datetime.now().strftime("%A")

                    namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                                      font=("Brush Script MT", 34, "bold"),
                                      height=49, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.44, rely=0.860)
                    detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                                       text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
                    detail.place(rely=0.864, relx=0.66)

                    def scan_book_get():
                        global nbx
                        global namebx
                        global datt
                        global qr_contents_qr
                        global return_dat

                        qrr(qr_contents_qr)

                        cap_vid = cv2.VideoCapture(0)
                        while True:
                            ret, frame = cap_vid.read()
                            decode_ing_vid_in_img = decode(frame)
                            for deeecod in decode_ing_vid_in_img:
                                qr_contents_qr = deeecod.data.decode('utf-8')
                                qr_contents_qr = str(qr_contents_qr)
                                nbx = qr_contents_qr

                                san_nbx = nbx.replace(" ", "_").replace("/", "_").replace(":", "_").replace(".",
                                                                                                            "_").replace(
                                    "\n", "").replace("Book_Name_:_", "").replace("Code_:_", "")
                                qr_contents_qr = str(qr_contents_qr)
                                tex = open(f"{tall}transaction.txt", "a")
                                dat_re_sub = dat.get()

                                fromdat = dt.date.today()

                                tex.write(
                                    f"{qr_contents_qr}\n*************************************************\nFrom : [{fromdat}]     To : [{dat_re_sub}]\n*************************************************\n")
                                tex = open(f"{tall}transaction.txt", "r")
                                print(tall)

                                tec1 = tex.read()

                                tex_box = customtkinter.CTkScrollableFrame(master=app4, corner_radius=32,
                                                                           border_width=4, bg_color="black",
                                                                           fg_color="black",
                                                                           border_color="black",
                                                                           scrollbar_button_color="gray",
                                                                           scrollbar_button_hover_color="gray",
                                                                           label_fg_color="white",
                                                                           label_text_color="black",

                                                                           label_font=("Arial", 20),
                                                                           label_anchor="center",
                                                                           orientation="vertical",
                                                                           scrollbar_fg_color="black", height=400,
                                                                           width=400)
                                tex_box.place(relx=0.35, rely=0.15)
                                dat_re_sub = dat.get()

                                fromdat = dt.date.today()
                                # date operation______________________________________________________

                                customtkinter.CTkLabel(tex_box, text=f"{tec1}", text_color="white").pack(pady=10)
                                print(f"h{tec1}")
                                with open(f"{tall}transaction.txt", "r") as fii:
                                    fii=fii.read()
                                with open(f"{tall_tall}.txt", "r") as fi:
                                    em1 = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    print(f"{em1}")
                                    print(f"{em}")

                                with open("account_details.txt", "r") as log_namee:
                                    lo1 = log_namee.readline()
                                    lo2 = log_namee.readline()
                                    lo3 = log_namee.readline()
                                    print(f"{lo2} mm")
                                    print(f"{lo3} pass")
                                filename = f"{nnbx}{numb}.png"
                                sender_maill = f"{lo2}"

                                receiver_maill = f"{em}"
                                passwords_m = f"{lo3}"

                                subjects = f"BOOK TRANSACTION OF\n {em1}"
                                bodys = f"{fii}"
                                me_ssage = MIMEMultipart()
                                me_ssage["From"] = sender_maill
                                me_ssage["To"] = receiver_maill
                                me_ssage["Subject"] = subjects
                                me_ssage.attach(MIMEText(bodys,"plain"))

                                try:
                                    with smtplib.SMTP("smtp.gmail.com", 587) as servers:
                                        servers.starttls()
                                        servers.login(sender_maill, passwords_m)
                                        servers.sendmail(sender_maill, receiver_maill, me_ssage.as_string())
                                        print("successful")
                                except Exception as e:
                                    print(f"Error {e}")

                                fi.close()


                                tex.close()

                                cv2.imshow('QR scanner press Q to exit', frame)
                                cap_vid.release()

                                cv2.destroyWindow('QR scanner press Q to exit')
                                return deeecod

                            cv2.imshow('QR scanner press Q to exit', frame)

                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break

                        cap_vid.release()
                        cv2.destroyAllWindows()

                    generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72",
                                             hover_color="pink",
                                             border_color="black", text_color="white", text="Scan Book",
                                             font=("Arial", 20, "bold"), command=scan_book_get)
                    generate_but.place(relx=0.450, rely=0.75)

                generate_but = CTkButton(master=app2, width=150, height=60, fg_color="#b33b72",
                                         hover_color="pink",
                                         border_color="black", text_color="white", text="Get Book",
                                         font=("Arial", 20, "bold"), command=get_book)
                generate_but.place(relx=0.360, rely=0.75)

                def put_book():

                    app4 = CTkLabel(app2, image=wall, text="")
                    app4.place(relx=0.0, rely=0.0)

                    global qr_contents_qr
                    qrr(qr_contents_qr)

                    frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                                         bg_color="white",
                                         fg_color="black", border_color="black")
                    frame_top.place(relx=0, rely=0)
                    with open("account_details.txt", "r") as log_name:
                        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
                        pr_new_log = str(pr_new_log)
                    with open("account_details.txt", "r") as log_name:
                        pr_new_log_img = log_name.readline().replace("\n", "")
                    lo_na_png = Image.open(f"{pr_new_log_img}.png")
                    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

                    name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                                          text_color="white",
                                          bg_color="black", anchor="center")
                    name_label.place(rely=0.02, relx=0.04)
                    namlbl = CTkLabel(master=app2, image=lo_na_png, text_color="white", text="", fg_color="black",
                                      font=("Arial", 24, "bold"),
                                      height=50, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.88, rely=0.01)

                    def des_t():
                        app2.destroy()

                    search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                                           fg_color="black",
                                           bg_color="black", command=des_t)
                    search_btn.place(rely=0.01, relx=0.95)
                    frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                                     fg_color="black")
                    frame.place(rely=0.860, relx=0.27)
                    home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                     fg_color="black",
                                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
                    home.place(rely=0.864, relx=0.30)
                    todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
                    todays.place(rely=0.864, relx=0.39)
                    clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                                      text="",
                                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                      fg_color="black",
                                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
                    clock.place(rely=0.864, relx=0.57)
                    now_upp = datetime.now().strftime("%A")

                    namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                                      font=("Brush Script MT", 34, "bold"),
                                      height=49, width=50, corner_radius=32, bg_color="black")
                    namlbl.place(relx=0.44, rely=0.860)
                    detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                                       text="",
                                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                                       fg_color="black",
                                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
                    detail.place(rely=0.864, relx=0.66)

                    def put_scan_book():
                        global tex_l
                        global qr_contents_qr
                        global an_nbxx
                        global san_nbxx
                        global protall

                        qrr(qr_contents_qr)

                        cap_vid = cv2.VideoCapture(0)
                        while True:
                            ret, frame = cap_vid.read()
                            decode_ing_vid_in_img = decode(frame)
                            for deeecod in decode_ing_vid_in_img:
                                qr_contents_qr = deeecod.data.decode('utf-8')
                                qr_contents_qr = str(qr_contents_qr)
                                tex = open(f"{qr_contents_qr}.txt", "r")
                                texxll1 = tex.readline()
                                c11 = texxll1.replace("_", " ").replace("\n", "")
                                c1 = texxll1.replace(" ", "_").replace("\n", "")
                                texxll2 = tex.readline()
                                c2 = texxll2.replace(" ", "_").replace("\n", "")
                                texxll3 = tex.readline()
                                c3 = texxll3.replace(" ", "_").replace("\n", "")

                                allt = c1, c2, c3

                                tallputt = ("".join(allt))

                                re_sen = open(f"{tallputt}transaction.txt", "a")
                                dat_retun = dt.date.today()
                                re_sen2 = open(f"{tallputt}transaction.txt", "r")
                                del_tex2 = re_sen2.read()
                                re_sen.write(
                                    f"\nReturned on {dat_retun}\nCheck above listed books are returned \n Then press Ok.")
                                re_sen = open(f"{tallputt}transaction.txt", "r")
                                del_tex = re_sen.read()
                                tex_box = customtkinter.CTkScrollableFrame(master=app4, corner_radius=32,
                                                                           border_width=4, bg_color="black",
                                                                           fg_color="black",
                                                                           border_color="black",
                                                                           scrollbar_button_color="gray",
                                                                           scrollbar_button_hover_color="gray",
                                                                           label_fg_color="white",
                                                                           label_text_color="black",

                                                                           label_font=("Arial", 20),
                                                                           label_anchor="center",
                                                                           orientation="vertical",
                                                                           scrollbar_fg_color="black",
                                                                           height=400, width=400)
                                tex_box.place(relx=0.35, rely=0.15)
                                customtkinter.CTkLabel(tex_box, text=del_tex, text_color="white").pack(
                                    pady=10)
                                re_sen.close()
                                with open(f"{tallputt}transaction.txt", "r") as fii:
                                    fii=fii.read()
                                with open(f"{tall_tall}.txt", "r") as fi:
                                    em1 = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    em = fi.readline()
                                    print(f"{em1}")
                                    print(f"{em}")

                                with open("account_details.txt", "r") as log_namee:
                                    lo1 = log_namee.readline()
                                    lo2 = log_namee.readline()
                                    lo3 = log_namee.readline()
                                    print(f"{lo2} mm")
                                    print(f"{lo3} pass")
                                filename = f"{nnbx}{numb}.png"
                                sender_maill = f"{lo2}"

                                receiver_maill = f"{em}"
                                passwords_m = f"{lo3}"

                                subjects = f"BOOK TRANSACTION OF {em1} Returned"
                                bodys = f"{del_tex2} Returned on {dat_retun}"
                                me_ssage = MIMEMultipart()
                                me_ssage["From"] = sender_maill
                                me_ssage["To"] = receiver_maill
                                me_ssage["Subject"] = subjects
                                me_ssage.attach(MIMEText(bodys,"plain"))

                                try:
                                    with smtplib.SMTP("smtp.gmail.com", 587) as servers:
                                        servers.starttls()
                                        servers.login(sender_maill, passwords_m)
                                        servers.sendmail(sender_maill, receiver_maill, me_ssage.as_string())
                                        print("successful")
                                except Exception as e:
                                    print(f"Error {e}")

                                fi.close()


                                tex.close()

                                def clear_book():
                                    re_sen = open(f"{tallputt}transaction.txt", "w")
                                    re_sen.write("")
                                    re_sen = open(f"{tallputt}transaction.txt", "r")
                                    del_tex = re_sen.read()

                                    tex_box = customtkinter.CTkScrollableFrame(master=app4, corner_radius=32,
                                                                               border_width=4, bg_color="black",
                                                                               fg_color="black",
                                                                               border_color="black",
                                                                               scrollbar_button_color="gray",
                                                                               scrollbar_button_hover_color="gray",
                                                                               label_fg_color="white",
                                                                               label_text_color="black",

                                                                               label_font=("Arial", 20),
                                                                               label_anchor="center",
                                                                               orientation="vertical",
                                                                               scrollbar_fg_color="black",
                                                                               height=400, width=400)
                                    tex_box.place(relx=0.35, rely=0.15)
                                    customtkinter.CTkLabel(tex_box, text=del_tex, text_color="white").pack(
                                        pady=10)

                                    re_sen.close()

                                generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72",
                                                         hover_color="pink",
                                                         border_color="black", text_color="white", text="Ok",
                                                         font=("Arial", 20, "bold"), command=clear_book)
                                generate_but.place(relx=0.550, rely=0.75)

                                cv2.imshow('QR scanner press Q to exit', frame)
                                cap_vid.release()

                                cv2.destroyWindow('QR scanner press Q to exit')
                                return deeecod

                            cv2.imshow('QR scanner press Q to exit', frame)

                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break

                        cap_vid.release()
                        cv2.destroyAllWindows()

                    generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72",
                                             hover_color="pink",
                                             border_color="black", text_color="white", text="Scan id",
                                             font=("Arial", 20, "bold"), command=put_scan_book)
                    generate_but.place(relx=0.450, rely=0.75)

                generate_but = CTkButton(master=app2, width=150, height=60, fg_color="#b33b72",
                                         hover_color="pink",
                                         border_color="black", text_color="white", text="Return Book",
                                         font=("Arial", 20, "bold"), command=put_book)

                generate_but.place(relx=0.560, rely=0.75)

                cv2.imshow('QR scanner press Q to exit', frame)
                cap_vid.release()

                cv2.destroyWindow('QR scanner press Q to exit')
                return deeecod

            cv2.imshow('QR scanner press Q to exit', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap_vid.release()
        cv2.destroyAllWindows()

    generate_but = CTkButton(master=appbot_re, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Scan ID",
                             font=("Arial", 20, "bold"), command=go_buy_put)
    generate_but.place(relx=0.440, rely=0.58)


todays = CTkButton(master=app2, image=toda, corner_radius=100, hover_color="dark blue", text="",
                   text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                   bg_color="transparent", border_color="black", border_width=2, command=getbook_putbook)
todays.place(rely=0.864, relx=0.39)


# ____________________________Get IN and OUT____________________________________________________________
def in_and_out():

    app4 = CTkLabel(app2, image=in__out_time_img, text="")
    app4.place(relx=0.0, rely=0.0)

    global qr_contents_qr
    qrr(qr_contents_qr)

    frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                         bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)
    with open("account_details.txt", "r") as log_name:
        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
        pr_new_log = str(pr_new_log)
    with open("account_details.txt", "r") as log_name:
        pr_new_log_img = log_name.readline().replace("\n", "")
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

    name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                          text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)

    frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                     fg_color="black")
    frame.place(rely=0.860, relx=0.27)
    home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                     fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
    home.place(rely=0.864, relx=0.30)
    todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                       fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)
    clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                      text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                      fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
    clock.place(rely=0.864, relx=0.57)
    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)

    detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                       text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                       fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)

    def go_buy_put_start():

        global qr_contents_qr
        qrr(qr_contents_qr)

        cap_vid = cv2.VideoCapture(0)

        while True:
            keyboard.add_hotkey('s', go_buy_put_start)
            ret, frame = cap_vid.read()
            decode_ing_vid_in_img = decode(frame)
            for deeecod in decode_ing_vid_in_img:
                qr_contents_qr = deeecod.data.decode('utf-8')
                qr_contents_qr = str(qr_contents_qr)
                tex = open(f"{qr_contents_qr}.txt", "r")
                texxll1 = tex.readline()
                c11 = texxll1.replace("_", " ").replace("\n", "")
                c1 = texxll1.replace(" ", "_").replace("\n", "")
                texxll2 = tex.readline()
                c2 = texxll2.replace(" ", "_").replace("\n", "")
                texxll3 = tex.readline()
                c3 = texxll3.replace(" ", "_").replace("\n", "")
                texxll4 = tex.readline()
                c4 = texxll4.replace(" ", "_").replace("\n", "")
                texxll5 = tex.readline()
                c5 = texxll5.replace(" ", " ").replace("\n", "")
                texxll6 = tex.readline()
                c6 = texxll6.replace(" ", " ").replace("\n", "")
                texxll7 = tex.readline()
                c7 = texxll7.replace(" ", " ").replace("\n", "")
                allt = c1, c2, c3
                allt2 = c11, c3
                allt0enty = c11
                allt1enty = c2
                allt2enty = c3
                allt3enty = c4
                allt4enty = c5
                allt5enty = c6
                allt5enty = c7

                tall = ("".join(allt))
                tall2 = ("".join(allt2))
                tall0 = ("".join(allt0enty))
                tall1 = ("".join(allt1enty))
                tall22 = ("".join(allt2enty))
                tall33 = ("".join(allt3enty))
                tall44 = ("".join(allt4enty))
                tall55 = ("".join(allt5enty))
                tall66 = ("".join(allt5enty))

                time.sleep(2)
                protall = Image.open(f"{tall}.png")
                protall = CTkImage(protall, size=(250, 250))
                pro = CTkLabel(app4, image=protall, text="")
                pro.place(relx=0.16, rely=0.24)
                pro = CTkLabel(app4, image=protall, text="")
                pro.place(relx=0.16, rely=0.24)
                tec_pro = CTkLabel(master=app4, text=tall0, fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.16, rely=0.60)

                in_ut_dat = dt.date.today()
                day_nam = in_ut_dat.strftime("%a ,%d %b %Y")
                now = datetime.now()

                hour = now.hour
                minute = now.minute
                second = now.second
                re_sen = open(f"{qr_contents_qr}.txt", "a")
                tim_fin = re_sen.write(f"{hour}:{minute}:{second}")
                re_sen = open(f"{qr_contents_qr}.txt", "r")
                texxll5 = re_sen.readline()
                c5 = texxll5.replace(" ", " ").replace("\n", "")
                texxll6 = tex.readline()
                c6 = texxll6.replace(" ", " ").replace("\n", "")
                texxll7 = tex.readline()
                c7 = texxll7.replace(" ", " ").replace("\n", "")

                re_lin_no = 7
                re_sen_re = open(f"{qr_contents_qr}.txt", "a")
                with open(f"{qr_contents_qr}.txt", "r") as file:
                    lines = file.readlines()
                with open(f"{qr_contents_qr}.txt", "w") as file:
                    for i, line in enumerate(lines, start=1):
                        if i != re_lin_no:
                            file.write(line)

                re_sen_re.close()
                file.close()

                tec_pro = CTkLabel(master=app4, text=f"{day_nam}", fg_color="black", text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.44, rely=0.30)
                tec_pro = CTkLabel(master=app4, text="In Time", fg_color="green",
                                   text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.34, rely=0.36)
                now2 = datetime.now()
                h2 = str(now2.hour).zfill(2)

                m2 = str(now2.minute).zfill(2)
                s2 = str(now2.second).zfill(2)
                open(f"{qr_contents_qr}incoming_outgoing.txt", "a")
                open(f"{qr_contents_qr}outgoing.txt", "a")
                open(f"{qr_contents_qr}ranking_h.txt", "a")
                open(f"{qr_contents_qr}ranking_m.txt", "a")
                open(f"{qr_contents_qr}ranking_s.txt", "a")

                with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as fileot:
                    in_wait_read = fileot.readline()
                    if in_wait_read:
                        print("have")
                        with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as fileot:
                            in_wait_read_20 = fileot.readline()
                            tec_pro = CTkLabel(master=app4, text=f"{in_wait_read_20}", fg_color="green",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.34, rely=0.40)
                    else:

                        print("not have")
                        with open(f"{qr_contents_qr}incoming_outgoing.txt", "w") as fileot:
                            fileot.write(f"{h2}:{m2}:{s2}")
                        with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as fileot:
                            in_wait_read_20 = fileot.readline()

                            tec_pro = CTkLabel(master=app4, text=f"{in_wait_read_20}", fg_color="green",
                                               text_color="white", height=30,
                                               width=250, font=("Georgia", 24))
                            tec_pro.place(relx=0.34, rely=0.40)

                tec_pro = CTkLabel(master=app4, text="Out Time", fg_color="red",
                                   text_color="white", height=30,
                                   width=250, font=("Georgia", 24))
                tec_pro.place(relx=0.54, rely=0.36)
                now22 = datetime.now()
                hh2 = str(now22.hour).zfill(2)

                mm2 = str(now22.minute).zfill(2)

                ss2 = str(now22.second).zfill(2)

                with open(f"{qr_contents_qr}outgoing.txt", "w") as fileot:
                    fileot.write(f"{hh2}:{mm2}:{ss2}")
                with open(f"{qr_contents_qr}outgoing.txt", "r") as fileot:

                    in_wait_read_loc = fileot.readline()

                    if in_wait_read_loc == in_wait_read_20:
                        tec_pro = CTkLabel(master=app4, text="", fg_color="red",
                                           text_color="white", height=30,
                                           width=250, font=("Georgia", 24))
                        tec_pro.place(relx=0.54, rely=0.40)

                    else:
                        with open(f"{qr_contents_qr}outgoing.txt", "r") as fileot:
                            in_wait_read_loc_ = fileot.readline()

                        tec_pro = CTkLabel(master=app4, text=in_wait_read_loc_, fg_color="red",
                                           text_color="white", height=30,
                                           width=250, font=("Georgia", 24))
                        tec_pro.place(relx=0.54, rely=0.40)
                        with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as linx:

                            linxs2hh = linx.readline(2)
                            linxsc = linx.readline(1)
                            linxsmm = linx.readline(2)
                            linxscc = linx.readline(1)
                            linxsss = linx.readline(2)

                            gl1 = int(linxs2hh)
                            gl2 = int(linxsmm)
                            gl3 = int(linxsss)

                        with open(f"{qr_contents_qr}outgoing.txt", "r") as linxout:
                            linxout0 = linxout.readline(2)
                            linxout1 = linxout.readline(1)
                            linxout2 = linxout.readline(2)
                            linxout3 = linxout.readline(1)
                            linxout4 = linxout.readline(2)

                            glot1 = int(linxout0)
                            glot2 = int(linxout2)
                            glot3 = int(linxout4)

                            total1 = gl1 - glot1
                            total2 = gl2 - glot2
                            total3 = gl3 - glot3
                            total_str1 = str(total1)
                            total_str2 = str(total2)
                            total_str3 = str(total3)
                            tot1 = total_str1.replace("-", "")
                            tot2 = total_str2.replace("-", "")
                            tot3 = total_str3.replace("-", "")
                            tot11 = int(tot1)
                            tot22 = int(tot2)
                            tot33 = int(tot3)

                        with open(f"{qr_contents_qr}ranking_h.txt", "a") as rank:
                            rank.write(f"{int(tot11):02}\n")
                        with open(f"{qr_contents_qr}ranking_m.txt", "a") as rank:
                            rank.write(f"{int(tot22):02}\n")
                        with open(f"{qr_contents_qr}ranking_s.txt", "a") as rank:
                            rank.write(f"{int(tot33):02}\n")

                        with open(f"{qr_contents_qr}ranking_h.txt", "r") as rank:

                            rankk_h = rank.read()
                            numbers = [int(num) for num in rankk_h.split() if num.isdigit()]
                            aa_h = sum(numbers)
                            print(aa_h)

                        with open(f"{qr_contents_qr}ranking_m.txt", "r") as rank:
                            rankk_m = rank.read()
                            numbers = [int(num) for num in rankk_m.split() if num.isdigit()]
                            aa_m = sum(numbers)
                            print(aa_m)

                        with open(f"{qr_contents_qr}ranking_s.txt", "r") as rank:
                            rankk_sp = rank.read()

                            numbers = [int(num) for num in rankk_sp.split() if num.isdigit()]
                            aa_s = sum(numbers)
                            print(aa_s)
                        tec_pro = CTkLabel(master=app4, text=f"{tot11}:{tot22}:{tot33}", fg_color="#950995",
                                           text_color="white", height=30,
                                           width=250, font=("Georgia", 24))
                        tec_pro.place(relx=0.34, rely=0.60)
                        tec_pro = CTkLabel(master=app4, text=f"Current Duration", fg_color="#950995",
                                           text_color="white", height=30,
                                           width=250, font=("Georgia", 24))
                        tec_pro.place(relx=0.34, rely=0.55)
                        tec_pro = CTkLabel(master=app4, text=f"{aa_h}:{aa_m}:{aa_s}", fg_color="#27B78E",
                                           text_color="white", height=30,
                                           width=250, font=("Georgia", 24))
                        tec_pro.place(relx=0.54, rely=0.60)
                        tec_pro = CTkLabel(master=app4, text=f"Total Duration", fg_color="#27B78E",
                                           text_color="white", height=30,
                                           width=250, font=("Georgia", 24))
                        tec_pro.place(relx=0.54, rely=0.55)

                        open(f"{qr_contents_qr}ranking.txt", "a")

                        re_lin_no = 1

                        with open(f"{qr_contents_qr}outgoing.txt", "r") as file:
                            lines = file.readlines()
                        with open(f"{qr_contents_qr}outgoing.txt", "w") as file:
                            for i, line in enumerate(lines, start=1):
                                if i != re_lin_no:
                                    file.write(line)

                        re_sen_re.close()
                        file.close()
                        re_lin_no = 1

                        with open(f"{qr_contents_qr}incoming_outgoing.txt", "r") as file:
                            lines = file.readlines()
                        with open(f"{qr_contents_qr}incoming_outgoing.txt", "w") as file:
                            for i, line in enumerate(lines, start=1):
                                if i != re_lin_no:
                                    file.write(line)

                        re_sen_re.close()
                        file.close()
                        rank.close()

            cv2.imshow('QR scanner press x to exit', frame)
            if keyboard.is_pressed('x'):
                exit(cv2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap_vid.release()

        cv2.destroyAllWindows()

    generate_but = CTkButton(master=app4, width=150, height=60, fg_color="#b33b72", hover_color="pink",
                             border_color="black", text_color="white", text="Start Scan",
                             font=("Arial", 20, "bold"), command=go_buy_put_start)
    generate_but.place(relx=0.150, rely=0.764)


clock = CTkButton(master=app2, image=clocks, corner_radius=100, hover_color="dark blue", text="",
                  text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                  bg_color="transparent", border_color="black", border_width=2, command=in_and_out)
clock.place(rely=0.864, relx=0.57)

now_upp = datetime.now().strftime("%A")


namlbl = CTkLabel(master=app2, text_color="black", text=now_upp, fg_color="white",
                  font=("Brush Script MT", 34, "bold"),
                  height=49, width=50, corner_radius=32, bg_color="black")
namlbl.place(relx=0.44, rely=0.860)



# login details_____________________________________________login_part________________________________________________login_setup_
def loogin_setup():

    app4 = CTkLabel(app2, image=login_lib, text="")
    app4.place(relx=0.0, rely=0.0)

    global qr_contents_qr
    qrr(qr_contents_qr)

    frame_top = CTkFrame(master=app4, width=2000, height=81, corner_radius=0, border_width=2,
                         bg_color="white",
                         fg_color="black", border_color="black")
    frame_top.place(relx=0, rely=0)
    with open("account_details.txt", "r") as log_name:
        pr_new_log = log_name.readline().replace("_", " ").replace("\n", "")
        pr_new_log = str(pr_new_log)
    with open("account_details.txt", "r") as log_name:
        pr_new_log_img = log_name.readline().replace("\n", "")
    lo_na_png = Image.open(f"{pr_new_log_img}.png")
    lo_na_png = CTkImage(lo_na_png, size=(50, 50))

    name_label = CTkLabel(master=app4, text=f"{pr_new_log}", font=("Georgia", 34, "bold"),
                          text_color="white",
                          bg_color="black", anchor="center")
    name_label.place(rely=0.02, relx=0.04)
    namlbl = CTkLabel(master=app4, image=lo_na_png, text_color="white", text="", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=50, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.88, rely=0.01)

    def des_t():
        app2.destroy()

    search_btn = CTkButton(master=app4, image=search, hover_color="grey", height=50, width=50, text="",
                           fg_color="black",
                           bg_color="black", command=des_t)
    search_btn.place(rely=0.01, relx=0.95)

    frame = CTkFrame(master=app4, width=700, height=50, corner_radius=12, bg_color="transparent",
                     fg_color="black")
    frame.place(rely=0.860, relx=0.27)
    home = CTkButton(master=app4, image=homes, corner_radius=100, hover_color="dark blue", text="",
                     text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                     fg_color="black",
                     bg_color="transparent", border_color="black", border_width=2,command=home_pg)
    home.place(rely=0.864, relx=0.30)
    todays = CTkButton(master=app4, image=toda, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                       fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=getbook_putbook)
    todays.place(rely=0.864, relx=0.39)
    clock = CTkButton(master=app4, image=clocks, corner_radius=100, hover_color="dark blue",
                      text="",
                      text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                      fg_color="black",
                      bg_color="transparent", border_color="black", border_width=2,command=in_and_out)
    clock.place(rely=0.864, relx=0.57)
    now_upp = datetime.now().strftime("%A")

    namlbl = CTkLabel(master=app4, text_color="black", text=now_upp, fg_color="white",
                      font=("Brush Script MT", 34, "bold"),
                      height=49, width=50, corner_radius=32, bg_color="black")
    namlbl.place(relx=0.44, rely=0.860)

    detail = CTkButton(master=app4, image=details, corner_radius=100, hover_color="dark blue",
                       text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"),
                       fg_color="black",
                       bg_color="transparent", border_color="black", border_width=2,command=loogin_setup)
    detail.place(rely=0.864, relx=0.66)

    def cam_img():
        global fils

        fils = askopenfiles("rb", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                            title="Upload File")

        fils = Image.open(fils[0])

        fils = CTkImage(fils, size=(250, 250))

        name_label = CTkLabel(master=app4, image=fils, text="", font=("Georgia", 34, "bold"), text_color="white",
                              bg_color="black", anchor="center")
        name_label.place(rely=0.269, relx=0.17)

    detail = CTkButton(master=app4, image=cam, corner_radius=100, hover_color="dark blue", text="",
                       text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="blue",
                       bg_color="transparent", border_color="black", border_width=2, command=cam_img)
    detail.place(rely=0.600, relx=0.22)
    datlbl = CTkLabel(master=app4, text_color="white", text="LIBRARY NAME", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    datlbl.place(relx=0.40, rely=0.290)
    lib_name = CTkEntry(master=app4, placeholder_text="Enter Library Name", fg_color="white", border_color="black",
                        border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    lib_name.place(relx=0.40, rely=0.340)
    mail = CTkLabel(master=app4, text_color="white", text="E-Mail ID", fg_color="black",
                    font=("Arial", 24, "bold"),
                    height=30, width=75, corner_radius=32, bg_color="black")
    mail.place(relx=0.40, rely=0.425)
    mail = CTkEntry(master=app4, placeholder_text="Enter E-Mail", fg_color="white", border_color="black",
                    border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    mail.place(relx=0.40, rely=0.470)
    datlbl = CTkLabel(master=app4, text_color="white", text="Password", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    datlbl.place(relx=0.40, rely=0.550)
    password = CTkEntry(master=app4, placeholder_text="Enter Mail Password", fg_color="white", border_color="black",
                        border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    password.place(relx=0.40, rely=0.595)
    mobile = CTkLabel(master=app4, text_color="white", text="Mobile No", fg_color="black",
                      font=("Arial", 24, "bold"),
                      height=30, width=75, corner_radius=32, bg_color="black")
    mobile.place(relx=0.40, rely=0.672)
    mobile = CTkEntry(master=app4, placeholder_text="Enter Mobile No", fg_color="white", border_color="black",
                      border_width=2, height=60, width=350, font=("Arial", 20, "bold"), text_color="black")
    mobile.place(relx=0.40, rely=0.717)

    def login_set_in_txt():
        na_log()
        global name_is
        name_is = lib_name.get()
        mail_is = mail.get()
        password_is = password.get()
        mobile_is = mobile.get()

        name_is = name_is.replace(" ", "_").replace(".", "").replace(",", "")
        open(f"{name_is}.txt", "a")
        open("account_details.txt", "a")
        with open(f"{name_is}.txt", "w") as log_name:
            log_name.write(f"{name_is}\n{mail_is}\n{password_is}\n{mobile_is}")

        region = (330, 313, 308, 311)
        screen_shot = pyautogui.screenshot(region=region)
        screen_shot.save(f"{name_is}.png")
        with open(f"{name_is}.txt", "r") as log_name:
            lo_na = log_name.read()

        with open("account_details.txt", "w") as log_name:
            log_name.write(lo_na)
        with open("account_details.txt", "r") as log_name:
            new_org_nam = log_name.readline().replace("\n", "")

        with open(f"{new_org_nam}.txt", "r") as log_name:
            pr_new_log = log_name.read()
            print(pr_new_log)
        datlbl = CTkLabel(master=app4, text_color="white",image=verified_e, text="", fg_color="black",
                          font=("Arial", 24, "bold"),
                          height=40, width=100, corner_radius=32, bg_color="transparent")
        datlbl.place(relx=0.665, rely=0.72)

        log_name.close()

    detail = CTkButton(master=app4, hover_color="dark blue", text="Save",
                       text_color="white", height=40, width=100, font=("Arial", 20, "bold"), fg_color="blue",
                       bg_color="transparent", command=login_set_in_txt)
    detail.place(rely=0.72, relx=0.665)


detail = CTkButton(master=app2, image=details, corner_radius=100, hover_color="dark blue", text="",
                   text_color="black", height=5, width=5, font=("Arial", 40, "bold"), fg_color="black",
                   bg_color="transparent", border_color="black", border_width=2, command=loogin_setup)
detail.place(rely=0.864, relx=0.66)




app2.mainloop()
