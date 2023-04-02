import tkinter.messagebox as messagebox
import random
import string
import requests
import os
import tkinter as tk

def obfuscate(url, times=100):
    return url.split(chr(47))[0]+chr(47)*2+"".join([("".join([(random.choice([chr(i) for i in range(97, 123)]+[(chr(i)) for i in range(48, 58)])) for i in range(times)])+"."+"".join([(random.choice([chr(i) for i in range(97, 123)]+[chr(i) for i in range(48, 58)]+['.com', 'discord', 'bit.ly', 'api', 'webhook', 'download', '.exe', 'telegram', 'org'])) for i in range(times)])+"@") for i in range(3)])+url.lower().replace(chr(119)*3+chr(ord("".join([chr(int(i)) for i in b"776597651006510165326598651216532656665108659765110651076532".decode().replace(str(65), chr(32)).split()])[::-1][11])-ord(str(6))), '').replace(url.split(chr(47))[0]+chr(47)*2, '', 1)+chr(35)+"".join([(random.choice([chr(i) for i in range(33, 127)]+[url.lower().replace(chr(119)*3+chr(ord("".join([chr(int(i)) for i in b"776597651006510165326598651216532656665108659765110651076532".decode().replace(str(65), chr(32)).split()])[::-1][11])-ord(str(6))), '').replace(url.split(chr(47))[0]+chr(47)*2, '', 1).split('/')[0]]*5+["discord.com/api/webhooks/"+"".join([random.choice(string.digits) for i in range(18)])+"/"+"".join([random.choice(string.ascii_letters) for i in range(68)])for i in range(15)])) for i in range(times)])



def get():
    
    # Display a simple alert message
    messagebox.showinfo("BEST OF", "Best coder GitHub:@ysf72byk")





def button_click():
    
    input_url = entry.get()
    try:
        r=requests.get(input_url)
        aa = obfuscate(input_url)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, aa+"Warezim")
    except Exception:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, 'URL adresi geçersiz')

       
#desinged by ysf72byk
window = tk.Tk()
window.title('URL Obfuscator by BiG')
window.geometry('800x670')
window.configure(bg='#292F36')

input_label = tk.Label(window, text="URL Gir:", fg='white', bg='#292F36', font=('Helvetica', 18))
input_label.pack(pady=20)


entry = tk.Entry(window, width=50, font=('Helvetica', 16), bd=2, relief=tk.GROOVE)
entry.pack()

button_frame = tk.Frame(window, bg='#292F36')
button_frame.pack(pady=30)

button = tk.Button(button_frame, text='Obfuscate', command=button_click, bg='#FFC107', fg='white', font=('Helvetica', 16), bd=2, relief=tk.GROOVE)
button.pack(padx=20, pady=10)

button = tk.Button(button_frame, text=':)', command=get, bg='#FFC107', fg='white', font=('Helvetica', 16), bd=2, relief=tk.GROOVE)
button.pack(padx=20, pady=10)

result_label = tk.Label(window, text='Obfuscated URL:', fg='white', bg='#292F36', font=('Helvetica', 18))
result_label.pack(pady=20)

result_text = tk.Text(window, height=20, width=120, font=('Helvetica', 8), bd=2, relief=tk.GROOVE)

result_text.pack()



window.mainloop()
