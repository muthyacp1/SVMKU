import tkinter as tk
from tkinter import Button, Entry, Frame, Label, StringVar, font as tkfont
from tkinter.constants import INSERT
from numpy.lib import Arrayterator

# Packages untuk analisa
import pandas as pd
import numpy as np
from numpy import asarray
from numpy import save
from numpy import load
from sklearn import svm

#for i in range(0, 20):
#       lst.append(ele)

lst = []
ele = int()

# def ya(ele):
#     ele = int(1)
# def tidak(ele):
#     ele = int(0) 
    

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, keterangan, G01, G02, G03, G04, G05, G06, G07, G08, G09, G10, G11, G12, G13, G14, G15, G16, G17, G18, G19, G20, hasil):
            
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="SISTEM DETEKSI DINI GANGGUAN MENTAL EMOSIONAL", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Deteksi",
                            command=lambda: controller.show_frame("keterangan"))
        button1.pack()



class keterangan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Pertanyaan berikut berhubungan dengan masalah 
        yang mungkin mengganggu selama 30 hari terakhir.
        Apabila kamu menganggap pertanyaan itu kamu 
        alami dalam 30 hari terakhir pilih jawaban YA,
        sebaliknya apabila kamu menganggap pertanyaan 
        ini tidak kamu alami pilih jawaban TIDAK""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Kembali", command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Lanjutkan",
                            command=lambda: controller.show_frame("G01"))
        button.pack()
        button2.pack()


class G01(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu sering sakit kepala?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="YA",
                            command=lambda: (lst.append(1),[controller.show_frame("G02")]),)
        button2 = tk.Button(self, text="TIDAK",
                            command=lambda: (lst.append(1),[controller.show_frame("G02")]))
        
        
        button1.pack()
        button2.pack()
        
        

class G02(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu merasa tidak nafsu makan?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G03")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G03")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G03(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu sulit untuk tidur?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G04")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G04")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G04(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu mudah merasa takut akan apapun?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G05")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G05")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G05(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu merasa tegang, cemas atau kuatir akan banyak hal?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G06")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G06")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G06(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apakah akhir-akhir ini tanganmu gemetar tanpa alasan?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G07")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G07")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G07(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini pencernaanmu terasa terganggu?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G08")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G08")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G08(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu sulit untuk berpikir jernih?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G09")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G09")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G09(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apakah kamu merasa tidak bahagia akhir akhir ini?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G10")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G10")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G10(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu menjadi sering menangis?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G11")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G11")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G11(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu menjadi sulit untuk menikmati kegiatan sehari-hari?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G12")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G12")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G12(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu sulit mengambil keputusan apapun bahkan yang sederhana?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G13")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G13")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G13(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apakah pekerjaan sehari-harimu menjadi terganggu karena pikiranmu?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G14")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G14")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G14(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apakah kamu merasa tidak melakukan hal-hal yang bermanfaat?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G15")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G15")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G15(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu menjadi kehilangan minat pada berbagai hal?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G16")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G16")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G16(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu merasa tidak berharga akan dirimu sendiri?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G17")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G17")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G17(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu pernah berpikir untuk mengakhiri hidupmu?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G18")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G18")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G18(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apakah kamu merasa lelah sepanjang waktu?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G19")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G19")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G19(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini perutmu terasa tidak enak?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("G20")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("G20")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class G20(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""Apa akhir-akhir ini kamu merasa menjadi mudah lelah?""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Ya", 
                            command=lambda: (ele==1,[controller.show_frame("hasil")]))
        button2 = tk.Button(self, text="Tidak",
                            command=lambda: (ele==0,[controller.show_frame("hasil")]))
        button1.pack()
        button2.pack()
        lst.append(ele)

class hasil(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="""HASIL KLASIFIKASI""", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        datalatih = pd.read_csv("datalatih.csv")
        clf = svm.SVC(kernel='poly')
        y = datalatih['Type'].to_numpy()
        x = datalatih[['G01','G02','G03','G04','G05','G06','G07','G08','G09','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20']].to_numpy()
        clf.fit(x,y)
        
        arr = asarray([lst])
        # hasil = clf.predict(arr)
        
        if hasil==1:
            label = tk.Label(self, text="""Anda mengalami gejala ganguan Cemas""", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)

        else:
            label = tk.Label(self, text="""Anda mengalami gejala gangguan Depresi""", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)


print(arr)
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()