x= float(input("escriba una distacia en km"))
y= float(299792.458)
a= float(1235)
b= float(508)
c= float(44.72)

luz= (x/y)/60
sonido= (x/a)
auto=(x/b)
bolt=(x/c)

print("La luz llegara en" ,str(luz)+  " minutos \n" + "El sonido a una temperatura de 20 grados tardara " + str(sonido)+  " horas \n"+ "El SSC Tautuara tardara " + str(auto)+  " horas en recorrer la distancia \n" + "Bolt tardaria " + str(bolt)+  " horas en recorrer la distacia \n")