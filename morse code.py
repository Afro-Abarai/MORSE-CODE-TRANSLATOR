from tkinter import *
from tkinter import messagebox

root = Tk()
variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("Choose Language")
variable2.set("Choose Language")
OUR_D = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}



def clearAll():
    language1_field.delete(1.0, END)
    language2_field.delete(1.0, END)


def convert():
    message = language1_field.get("1.0", "end")[:-1]
    if variable1.get() == variable2.get():
        messagebox.showerror("INVALID INPUT")
        return
    elif variable1.get() == "English" and variable2.get() == "Morse":
        rslt = encode(message)
    elif variable1.get() == "Morse" and variable2.get() == "English":

        rslt = decode(message)
    else:
        messagebox.showerror("please choose valid language code..")
        return
    language2_field.insert('end -1 chars', rslt)


def encode(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += OUR_D[letter] + ' '
        else:
            cipher += ' '
    return cipher


def decode(message):
    message += ' '
    decipher = ''
    citext = ''

    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(OUR_D.keys())[list(OUR_D.values()).index(citext)]
                citext = ''
    return decipher


if __name__ == "__main__":
    root.configure(background='brown')
    root.geometry("400x400")
    root.title("MORSE CODE CONVERTER")
    headlabel = Label(root, text='MORSE CODE TRANSLATOR', fg='black', bg="red")
    label1 = Label(root, text="One Language ", fg='black', bg='yellow')
    label2 = Label(root, text="From Language", fg='black', bg='yellow')
    label3 = Label(root, text="To Language ", fg='black', bg='yellow')
    label4 = Label(root, text="Converted Language ", fg='black', bg='yellow')
    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)
    label4.grid(row=5, column=0)
    language1_field = Text(root, height=5, width=25, font="consolas")
    language2_field = Text(root, height=5, width=25, font="consolas")
    language1_field.grid(row=1, column=1, padx=10)
    language2_field.grid(row=5, column=1, padx=10)
    languageCode_list = ["English", "Morse"]
    FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
    ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)
    FromLanguage_option.grid(row=2, column=1, ipadx=10)
    ToLanguage_option.grid(row=3, column=1, ipadx=10)
    button1 = Button(root, text="CONVERT", bg="light green", fg="black", command=convert)
    button1.grid(row=4, column=1)
    button2 = Button(root, text="CLEAR", bg="salmon", fg="dark green", command=clearAll)
    button2.grid(row=6, column=1)
    root.mainloop()
