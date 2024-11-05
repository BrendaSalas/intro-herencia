from ClassPezPayaso import PezPayaso


miPez = PezPayaso("Nemo", "Naranja-Blanco", "Pequeño","Agua Salada", True)
miPez.descripcion()
miPez.nadar()
print(f"Mi pez se llama {miPez.getNombre()}")
miPez.setNombre("Dori")
print(f"Mi pez se llama {miPez.getNombre()}")
print(f"Mi pez tiene el color {miPez.getColor()}")