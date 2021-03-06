import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.screen = tk.Text(master, state='disabled', width=30, height=3, background="gray", foreground="black")
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')
        self.equation = ''
        b1 = self.create_button(7)
        b2 = self.create_button(8)
        b3 = self.create_button(9)
        b4 = self.create_button(u"\u232B", None)
        b5 = self.create_button(4)
        b6 = self.create_button(5)
        b7 = self.create_button(6)
        b8 = self.create_button(u"\u00F7")
        b9 = self.create_button(1)
        b10 = self.create_button(2)
        b11 = self.create_button(3)
        b12 = self.create_button('*')
        b13 = self.create_button('.')
        b14 = self.create_button(0)
        b15 = self.create_button('+')
        b16 = self.create_button('-')
        b17 = self.create_button('=', None, 34)


        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]


        count = 0

        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1

        buttons[16].grid(row=5, column=0, columnspan=4)

    def create_button(self, val, write=True, width=7):
        return tk.Button(self.master, text=val, command=lambda: self.click(val, write), width=width)

    def click(self, text, write):
        if write == None:
            if text == '=' and self.equation:
                self.equation = tk.re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u"\u232B":
                self.clear_screen()
        else:
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', tk.END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(tk.END, value)
        self.equation += str(value)
        self.screen.configure(state='disabled')


root = tk.Tk()
app = Calculator(root)
root.mainloop()