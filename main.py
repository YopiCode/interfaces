import tkinter as tk
from datetime import datetime
from unidecode import unidecode


class Search:
    def __init__(self):
        self.pacientes = [
            {"id": 1, "nombre": "Juan", "fecha_nacimiento": "1990-05-15", "direccion": "Calle 123"},
            {"id": 2, "nombre": "María", "fecha_nacimiento": "1985-10-20", "direccion": "Avenida XYZ"},
        ]

        self.root = tk.Tk()
        self.root.title("Consulta de Pacientes")
        self.root.geometry("400x720")
        self.root.configure(background="#10243d")
        self.root.resizable(False, False)

        self.create_search_widgets()

    def buscar_paciente(self):
        nombre_buscar = unidecode(self.entry_nombre.get().lower())
        encontrado = False
        for paciente in self.pacientes:
            if unidecode(paciente["nombre"].lower()) == nombre_buscar:
                edad = self.calcular_edad(paciente["fecha_nacimiento"])
                self.mostrar_datos(paciente["nombre"], edad, paciente["direccion"])
                encontrado = True
                break

        if encontrado:
            print("wenas")
            self.ocultar_mensaje()  # Oculta el mensaje si se encuentra un paciente
            self.mostrar_datos(paciente["nombre"], edad, paciente["direccion"])
        else:
            self.limpiar_datos()
            self.mostrar_mensaje("Paciente no existe")
            self.ocultar_historial()

    def calcular_edad(self, fecha_nacimiento):
        fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.today()
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
        return edad

    def mostrar_datos(self, nombre, edad, direccion):
        self.limpiar_datos()
        self.label_nombre.config(text=f"Nombre: {nombre}")
        self.label_edad.config(text=f"Edad: {edad} años")
        self.label_direccion.config(text=f"Dirección: {direccion}")
        self.btn_historial.pack(pady=10, side=tk.BOTTOM)
        self.mostrar_historial()

    def mostrar_mensaje(self, mensaje):
        self.label_mensaje.config(text=mensaje)
        self.label_mensaje.pack(pady=10, side=tk.BOTTOM)

    def ocultar_mensaje(self):
        self.label_mensaje.pack_forget()

    def limpiar_datos(self):
        self.label_nombre.config(text="")
        self.label_edad.config(text="")
        self.label_direccion.config(text="")
        self.btn_historial.grid_forget()
        self.ocultar_historial()

    def mostrar_historial(self):
        self.btn_historial.pack(pady=10, side=tk.BOTTOM)

    def ocultar_historial(self):
        self.btn_historial.pack_forget()

    def create_search_widgets(self):
        self.frame = tk.Frame(self.root, width=400, height=720, background="#10243d")
        self.frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.label_titulo = tk.Label(self.frame, text="Buscar Paciente", fg="white", background="#10243d",
                                     font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)

        self.entry_nombre = tk.Entry(self.frame, width=30, font=("Arial", 12))
        self.entry_nombre.pack(padx=10, pady=5)

        self.btn_buscar = tk.Button(self.frame, text="Buscar", width=15, command=self.buscar_paciente,
                                    background="#da5953", fg="white", border=0, font=("Arial", 10))
        self.btn_buscar.pack(padx=10, pady=8)

        self.label_titulo1 = tk.Label(self.frame, text="", fg="white", background="#10243d",
                                      font=("Arial", 18, "bold"))
        self.label_titulo1.pack(pady=10)

        self.label_mensaje = tk.Label(self.frame, text="", fg="white", background="#10243d", font=("Arial", 12))
        self.label_mensaje.pack(pady=10)

        self.label_nombre = tk.Label(self.frame, text="", fg="white", background="#10243d", font=("Arial", 12))
        self.label_nombre.pack(pady=5)

        self.label_edad = tk.Label(self.frame, text="", fg="white", background="#10243d", font=("Arial", 12))
        self.label_edad.pack(pady=5)

        self.label_direccion = tk.Label(self.frame, text="", fg="white", background="#10243d", font=("Arial", 12))
        self.label_direccion.pack(pady=5)

        self.label_titulo2 = tk.Label(self.frame, text="", fg="white", background="#10243d",
                                      font=("Arial", 18, "bold"))
        self.label_titulo2.pack(pady=10)

        self.btn_historial = tk.Button(self.frame, text="Ver Historial de Revisiones", font=("Microsoft YaHei UI", 11),
                                       width=25, background="#CCA43B", fg="white", border=0)
        self.btn_historial.pack(pady=10)

        self.ocultar_historial()

        self.root.mainloop()


if __name__ == "__main__":
    search = Search()
