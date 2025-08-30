#Ejercicio Nro 4

class vuelto :

    def cambio(self, monto):

       billetes200=0
       billetes100=0
       billetes50=0
       billetes20=0
       billetes10=0
       billetes5=0
       billetes2=0
       billetes1=0
       monedas050=0
       monedas025=0
       monedas010=0
       monedas005=0

       
       while monto>=0.05:
           if monto>=200:
            billetes200=monto//200
            monto=round(monto%200,2)
           elif monto>=100:
            billetes100=monto//100
            monto=round(monto%100,2)
           elif monto>=50:
            billetes50=monto//50
            monto=round(monto%50,2)
           elif monto>=20:
            billetes20=monto//20
            monto=round(monto%20,2)
           elif monto>=10:
            billetes10=monto//10
            monto=round(monto%10,2)
           elif monto>=5:
            billetes5=monto//5
            monto=round(monto%5,2)
           elif monto>=2:
            billetes2=monto//2
            monto=round(monto%2,2)
           elif monto>=1:
            billetes1=monto//1
            monto=round(monto%1,2)
           elif monto>=0.50:
            monedas050=monto//0.50
            monto=round(monto%0.50,2)
           elif monto>=0.25:
            monedas025=monto//0.25
            monto=round(monto%0.25,2)
           elif monto>=0.10:
            monedas010=monto//0.10
            monto=round(monto%0.10,2)
           elif monto>=0.05:
            monedas005=monto//0.05
            monto=round(monto%0.05,2)

       print(f"""Usted necesita {billetes200} billetes de 200
             {billetes100} billetes de 100
             {billetes50} billetes de 50
             {billetes20} billetes de 20
             {billetes10} billetes de 10
             {billetes5} billetes de 5
             {billetes2} billetes de 2
             {billetes1} billetes de 1
             {monedas050} monedas de 0.5
             {monedas025} monedas de 0.25
             {monedas010} monedas de 0.10
             {monedas005} moendas de 0.05""")
       
vuelto1=vuelto()
pago=float(input("Ingrese el monto del pago: "))
vuelto1.cambio(pago)
        
        
