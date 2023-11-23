import tkinter as tk

from main import Search


class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("1000x500")
        self.root.configure(background="white")
        self.root.resizable(False, False)

        self.create_login_widgets()

    def loginUser(self):
        username = self.user.get()
        password = self.code.get()

        if username == "admin" and password == "123":
            print("Habla Causa GAAAAAAAAAAAAAAAAAAAAA")
            self.root.destroy()  # Cerrar la ventana de login
            Search()
        else:
            print("Error de Credenciales")

    def create_login_widgets(self):
        image_path = "login.png"
        img = tk.PhotoImage(file=image_path)

        frame = tk.Frame(self.root, width=550, height=750, background="white")
        frame1 = tk.Frame(self.root, width=600, height=750, background="#10243d")

        label_image = tk.Label(frame, image=img, background="white")
        label_image.place(relx=0.5, rely=0.3, anchor="center")

        frame.grid(row=0, column=1)
        frame1.grid(row=0, column=2)

        heading = tk.Label(frame1, text="LOGIN", fg="white", background="#10243d",
                           font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=170, y=100)

        self.user = tk.Entry(frame1, width=25, fg="white", border=0, background="#10243d",
                             font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=80, y=150)
        self.user.insert(0, "Ingrese Usuario")
        self.user.bind("<FocusIn>", self.on_enter)
        self.user.bind("<FocusOut>", self.on_leave)

        tk.Frame(frame1, width=295, height=2, bg="white").place(x=80, y=177)

        self.code = tk.Entry(frame1, width=25, fg="white", border=0, background="#10243d",
                             font=("Microsoft YaHei UI Light", 11), show="")
        self.code.place(x=80, y=220)
        self.code.insert(0, "Ingrese Contraseña")
        self.code.bind("<FocusIn>", self.on_enter)
        self.code.bind("<FocusOut>", self.on_leave)

        tk.Frame(frame1, width=295, height=2, bg="white").place(x=80, y=247)

        tk.Button(frame1, width=39, pady=7, text="Iniciar Sesion", background="#da5953", fg="white", border=0,
                  command=self.loginUser).place(x=80, y=274)

        self.root.mainloop()

    def on_enter(self, e):
        widget = e.widget
        var = widget.get()
        if var == "Ingrese Usuario" or var == "Ingrese Contraseña":
            widget.delete(0, "end")

    def on_leave(self, e):
        widget = e.widget
        if widget.get() == '':
            if widget == self.user:
                widget.insert(0, "Ingrese Usuario")
            elif widget == self.code:
                widget.insert(0, "Ingrese Contraseña")


if __name__ == "__main__":
    login = Login()
