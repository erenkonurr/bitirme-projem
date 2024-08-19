import tkinter as tk
from tkinter import *
import time  
from tkinter import messagebox
import numpy as np

def koordinat_düzlemi():
    global düzlem_tag,derece,katsayilar
    
    
    düzlem_tag="düzlem"
    canvas1.create_line(0 ,200,400,200,fill="black",width = 1,tags=düzlem_tag)
    canvas1.create_line(200 ,0,200,400,fill="black",width = 1,tags=düzlem_tag)

    for i in range(0,400,11):
        canvas1.create_oval(i,197.5,i+5,202.5,fill="lightgrey",tags=düzlem_tag)
        canvas1.create_oval(197.5,i,202.5,i+5,fill="lightgrey",tags=düzlem_tag)
        
def temizle():
    canvas1.delete(düzlem_tag)

def derece_kaydet():
    global derece
    try:
        
        derece=int(fonk_derece.get())
        if derece < 0:
            raise ValueError("Negatif değer")
            
            
            

        canvas2.create_line(160,57,167,64,fill="green",width=2,tags="tick") 
        canvas2.create_line(167,64,179,52,fill="green",width=2,tags="tick") 
        mesaj2=tk.Label(ekran,text="x in her bir derecesinin katsayısını büyük dereceden küçüğe sıra ile yazalım :",fg="purple",bg="white"  )
        canvas2.create_window(205,100,window=mesaj2,tags="katsayi_butonlar")
        canvas2.delete("tick2")
        katsayı_kaydet=tk.Button(ekran,text="katsayı onay",fg="darkblue",bg="yellow",command=katsayı_kayıt)
        canvas2.create_window(205,125,window=katsayı_kaydet,tags="katsayi_butonlar")
    


        katsayı_temizlemek=tk.Button(ekran,text="katsayı temizle",fg="darkblue",bg="yellow",command=katsayı_temizle)
        canvas2.create_window(210,155,window=katsayı_temizlemek,tags="katsayi_butonlar")

        def create_box():
            global derece,değer_listesi
            değer_listesi = []
    
    
    
            for z in range(derece+1):
                katdeğerleri=tk.Entry(ekran,bg="lightblue")
                canvas2.create_window(100,120+20*z,window=katdeğerleri,tags="katsayilar")
                değer_listesi.append(katdeğerleri)
    

        kök_hesapla = tk.Button(ekran, text="Kök Hesapla", fg="darkblue", bg="yellow", command=nokta_hesapla)
        canvas2.create_window(204, 185, window=kök_hesapla,tags="katsayi_butonlar")
        
    except ValueError:
        messagebox.showinfo("HATA!","Lütfen bir pozitif tam sayı giriniz")
        canvas2.create_line(160,58,170,68,fill="red",width=2,tags="tick2") 
        canvas2.create_line(170,58,160,68,fill="red",width=2,tags="tick2")
        canvas2.delete("katsayi_butonlar")
       

def create_box():
    global derece,değer_listesi
    değer_listesi = []
    
    
    
    for z in range(derece+1):
        katdeğerleri=tk.Entry(ekran,bg="lightblue")
        canvas2.create_window(100,120+20*z,window=katdeğerleri,tags="katsayilar")
        değer_listesi.append(katdeğerleri)
        
        
    

def katsayı_kayıt():
    global değer_listesi,katsayilar
    try:
        katsayilar = [float(entry.get()) for entry in değer_listesi]
        polinom_olustur()
        canvas2.create_line(265,122,272,129,fill="green",width=2,tags="tick3") 
        canvas2.create_line(272,129,284,117,fill="green",width=2,tags="tick3")
        canvas2.delete("tick4")
        
    except ValueError:
        messagebox.showinfo("HATA!","lutfen tam veya ondalıklı sayılar giriniz")
        canvas2.delete("tick3")
        canvas2.create_line(265,122,275,132,fill="red",width=2,tags="tick4") 
        canvas2.create_line(275,122,265,132,fill="red",width=2,tags="tick4")

    
    
    



def katsayı_temizle():
    canvas2.delete("katsayilar")    
    canvas2.delete("tick")
    canvas2.delete("tick2")
    label_polinom.config(text="")   
    canvas2.delete("katsayi_butonlar") 
    canvas2.delete("tick3")
    canvas2.delete("tick4")   

def buton_komutları():
    
    derece_kaydet()
    create_box()        

def polinom_olustur():
    global derece,katsayilar
    polinom = ""
    
    for i, katsayi in enumerate(katsayilar):
        exp = derece - i
        if katsayi != 0:
            if exp == 0:
                polinom += f"({katsayi:.2f}) "
            elif exp == 1:
                polinom += f"({katsayi:.2f}x) + "
            else:
                polinom += f"({katsayi:.2f}x^{exp}) + "
    
    
    if polinom.endswith(" + "):
        polinom = polinom[:-3]
        
    
    label_polinom.config(text=polinom)
    time.sleep(1)


def nokta_hesapla():
    global katsayilar,gerçek_kökler
    try:
        kökler = np.roots(katsayilar)
        gerçek_kökler = [kök.real for kök in kökler if kök.imag == 0]
    
        if gerçek_kökler:
            messagebox.showinfo("Kökler", f"Polinomun kökleri: {', '.join(map(str, gerçek_kökler))}")
        else:
            messagebox.showinfo("Kökler", "Polinomun gerçek kökü yok.")
    except NameError:
         messagebox.showinfo("polinom bulunamadı", "henüz katsayısı bilgilerini girmediniz.")   
    

def plot_graph():
    global derece, katsayilar, gerçek_kökler
   
    
    m = None
    n = None
    
    last_y_label = None
    
    for x in range(-200, 200):
        try:
            y = sum(katsayı * (x/11)**(derece - i) for i, katsayı in enumerate(katsayilar))
            x_değeri = 200+x
            y_değeri = 200 - y*11 
        
            if y_değeri > 400 :
                continue
        
        except NameError:
            messagebox.showinfo("polinom bulunamadı","henüz katsayısı bilgilerini girmediniz")        
        


        if x == 0:
            if last_y_label is None or abs(y_değeri - last_y_label) > 20:
                canvas1.create_oval(196, y_değeri-4 , 204, y_değeri + 4, fill="#723d46", tags="graph")
                canvas1.create_text(38, 560, text=f"(0, {y:.2f})", font=("Arial", 13), fill="#723d46", tags="graph")
               
                last_y_label = y_değeri
            
        
        if m is not None and n is not None:
            canvas1.create_line(m,n, x_değeri, y_değeri, fill="darkblue", tags="graph",width=1)
        
        m = x_değeri
        n = y_değeri
    
    colors = ["red", "lightgreen", "blue", "orange", "cyan", "pink", "brown", "purple"]
    color_index = 0
    z=0
    try:
        for kök in gerçek_kökler:

            x_koordinat = 200 + kök * 11
            y_koordinat = 200
        
            color = colors[color_index % len(colors)]
            color_index += 1
    
            canvas1.create_oval(x_koordinat - 4, y_koordinat - 4, x_koordinat + 4, y_koordinat + 4, fill=color, tags="graph")
            canvas1.create_text(38+80*z,490 , text=f"({kök:.2f}, 0)", font=("Arial", 13), fill=color, tags="graph")
            z+=1
            
    except NameError:
        messagebox.showinfo("kökler hesaplanamadı!","'Kök Hesapla' tusuna basmazsanız \n fonksiyonun köklerini göremezsiniz")
def polinom_temizle():
    canvas1.delete("graph")        


      
    
       

ekran = tk.Tk()

ekran.title("polinom olusturma uyg.")


canvas1 = tk.Canvas(ekran, width=400, height=600, bg='white')
canvas1.grid(row=0, column=0, rowspan=2)


canvas2 = tk.Canvas(ekran, width=600, height=600, bg='white')
canvas2.grid(row=0, column=1, rowspan=2)




button_olustur = tk.Button(ekran, text="düzlem olustur",fg="darkblue",bg="yellow", command=koordinat_düzlemi)
canvas2.create_window(400, 350, window=button_olustur)

button_delete = tk.Button(ekran, text="düzlemi sil",fg="darkblue",bg="yellow",command=temizle)
canvas2.create_window(490, 350, window=button_delete)


mesaj=tk.Label(ekran,text="fonk kaçıncı derece :",fg="purple",bg="white")
canvas2.create_window(60,30,window=mesaj)

fonk_derece= tk.Entry(ekran,bg="lightblue")
canvas2.create_window(180,30,window=fonk_derece)

derece_kayıt=tk.Button(ekran, text="derece onay",fg="darkblue",bg="yellow",command=buton_komutları)
canvas2.create_window(100, 60, window=derece_kayıt)



polinom_yapmak=tk.Button(ekran,text="polinomu olustur",fg="darkblue",bg="yellow",command=plot_graph)
canvas2.create_window(390,390,window=polinom_yapmak)

label_polinom = tk.Label(ekran, text="", font=("Arial", 10),bg="white")
canvas1.create_window(200, 425, window=label_polinom,tags="zaha")

polinom_silmek=tk.Button(ekran,text="polinomu sil",fg="darkblue",bg="yellow",command=polinom_temizle)
canvas2.create_window(490,390,window=polinom_silmek)

mesaj3=tk.Label(ekran,text="polinomun köklerinin koordinatları",bg="white",font=("Arial",12))
canvas1.create_window(125,460,window=mesaj3)

mesaj4=tk.Label(ekran,text="y ekseninin kesildiği koordinat:",bg="white",font=("Arial",12))
canvas1.create_window(115,530,window=mesaj4)




ekran.mainloop()