import random
import tkinter

class Gen():

    def __init__(self):
        self.suffix = ['wski', 'wska']

        self.cons = ['b', 'c', 'cz', 'd', 'd', 'dz', 'dź', 'dż', 'f', 'g', 'ch', 'h', 'j', 'k', 'l', 'ł', 'm', 'n', 'p', 'r', 's', 'sz', 't', 'w', 'z', 'ź', 'ż']

        self.vowels = ['a', 'ą', 'e', 'ę', 'i','o', 'u', 'y', 'ó']


    def generator(self):
        m = 1
    
        word = ""
        bad = [ 'ź', 'dź', 'dż']
        first = False
        circles = 0

        while first != True:
            spin = random.choice(self.cons)
            if spin not in bad:
                word += spin
                word += random.choice(self.vowels)
                first = True


        while circles != int(m):
            spin = random.choice(self.cons)

            if spin != 'ź' and spin == 'dź':
                word += spin
                word += 'w'
                circles +=1
                word += random.choice(self.vowels)
            else:
                word += spin
                circles += 1

                word += random.choice(self.vowels)
        
        word += random.choice(self.suffix)
        okno.configure(text=f"Your new polsih last name is : {word}")

        
        

g = Gen()
root = tkinter.Tk()
root.title("Welcome to last name generator!")

polecenie = tkinter.Label(master=root, text="Generate your new Polish last name!!!",width=90)
polecenie.pack()

przycisk_losowania = tkinter.Button(master=root, text="generate", command=g.generator())
przycisk_losowania.pack()

okno = tkinter.Label(master=root)
okno.pack()
root.mainloop()