def arrancar(self):
    if not self.encendido:
        self.encendido = True
        print(f"El {self.modelo} ha arrancado.")
    else:
        print(f"El {self.modelo} ya está encendido.")


# Uso
mi_coche = Coche("Toyota", "Corolla", 2020)
mi_coche.arrancar()