# Documentation LinK: https://docs.google.com/document/d/1d1VlOMnOZjgNAv5aZTm-3gwCg-JFuRfsWr4u1ed_Fy4/edit?usp=sharing 
from tkinter import * 
import tkinter.messagebox

# Create the main window
root = Tk()
root.title("Encryption & Decryption")
root.geometry("1920x1000")
# root.config(bg="silver")

# Create the Functions
def reset():
    key_entry.delete(0, END)                              #Clear Entry Widget
    plaintext_text.delete("1.0", END)                     #Clear Text Widget
    ciphertext_text.delete("1.0", END)                    #Clear Text Widget
    decrypted_text.delete("1.0", END)                     #Clear Text Widget

def iexit():
    iexit = tkinter.messagebox.askyesno("Encryption/Decryption", "Confirm if you want to exit")
    if iexit > 0:
        root.destroy()
        return

def encrypt_decrypt(text, key):
    encrypted = ''.join(chr(ord(x) ^ key) for x in text)
    return encrypted

def encrypt():
    try:
        key = int(key_entry.get())
        plaintext = plaintext_text.get("1.0",END).strip()  
        encrypted = encrypt_decrypt(plaintext, key)
        ciphertext_text.delete("1.0",END)
        ciphertext_text.insert("1.0", encrypted)
    except Exception as e:
        tkinter.messagebox.showerror('Error',str(e))

def decrypt():
    try:
        key = int(key_entry.get())
        ciphertext = ciphertext_text.get("1.0",END).strip()  
        decrypted = encrypt_decrypt(ciphertext, key)
        decrypted_text.delete("1.0",END)
        decrypted_text.insert("1.0", decrypted)
    except Exception as e:
        tkinter.messagebox.showerror('Error',str(e))



# Create the Widget
key_label = Label(root, font=('arial',24,'bold'), text = "Key:")
key_label.pack()

key_entry = Entry(root, font=('arial',24,'bold'), width = 50 ,justify = 'center')
key_entry.pack()
key_entry.focus()

plaintext_label = Label(root, font=('arial',24,'bold'), text = "Plaintext:")
plaintext_label.pack()

plaintext_text = Text(root, font=('arial',24,'bold'), height = 5, width = 80)
plaintext_text.pack()

encrypt_button  = Button(root, font=('arial',24,'bold'), width = 10, text = "Encrypt", command=encrypt)
encrypt_button.pack()

ciphertext_label = Label(root, font=('arial',24,'bold'), text = "Ciphertext:")
ciphertext_label.pack()

ciphertext_text = Text(root, font=('arial',24,'bold'), height = 5, width = 80)
ciphertext_text.pack()

decrypt_button  = Button(root, font=('arial',24,'bold'), width = 10, text = "Decrypt", command=decrypt)
decrypt_button.pack()

decrypted_label = Label(root, font=('arial',24,'bold'), text = "Decrypted:")
decrypted_label.pack()

decrypted_text = Text(root, font=('arial',24,'bold'), height = 5, width = 80)
decrypted_text.pack()

button_frame = Frame(root)
button_frame.pack()

reset_button  = Button(button_frame, font=('arial',24,'bold'), width = 10, text = "Reset", command=reset)
reset_button.pack(side = LEFT, padx=10)

exit_button  = Button(button_frame, font=('arial',24,'bold'), width = 10, text = "Exit", command= iexit)
exit_button.pack(side = LEFT, padx=10)

root.mainloop()
