frecuencia = float(input("Ingrese la frecuencia (hz): "))
if frecuencia <= 30*10**3 :
  print("Muy Baja Frecuencia")
elif frecuencia > 30*10**3 and frecuencia <= 650*10**3:
  print("Onda Larga - Radio")
elif frecuencia > 650*10**3 and frecuencia <= 1.7*10**6:
  print("Onda media - Radio")
elif frecuencia >1.7*10**6  and frecuencia <=30*10**6:
  print("Onda Corta - Radio")
elif frecuencia > 30*10**6  and frecuencia <= 300*10**6:
  print("Muy Alta Frecuencia-Radio")
elif frecuencia >300*10**6  and frecuencia <= 3*10**8:
  print("Ultra Alta Frecuencia-Radio")
elif frecuencia >3*10**8  and frecuencia <= 300*10**9 :
  print("Microondas")
elif frecuencia > 300*10**9 and frecuencia <= 6.00*10**12:
  print("Infrarrojo lejano/submilimétrico")
elif frecuencia > 6.00*10**12 and frecuencia <= 120*10**12:
  print("Infrarrojo medio")
elif frecuencia >  120*10**12 and frecuencia <= 384*10**12:
  print("Infrarrojo cercano")
elif frecuencia >  384*10**12 and frecuencia <= 7.89*10**14 :
  print("Espectro Visible")
elif frecuencia >  7.89*10**14 and frecuencia <= 1.5*10**15:
  print("Ultravioleta cercano")
elif frecuencia > 1.5*10**15  and frecuencia <= 30.0*10**15 :
  print("Ultravioleta extremo")
elif frecuencia >   30.0*10**15  and frecuencia <= 30.0*10**18 :
  print("Rayos X")
else:
  print("Rayos gamma")