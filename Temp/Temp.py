#Ejercicio Nro 10

dia=int(input("Ingresa el dia: "))
mes=input("Ingresa el mes: ").lower()
emisferio=input("Ingresa el Emisferio, N o S: ").upper()

if emisferio=="N" :
   if mes=="diciembre" :
      if dia>=21 and dia<=31 :
         print("Invierno")
   elif mes=="enero" :
      if dia>=1 and dia <=31 :
         print("Invierno")
   elif mes=="febrero" :
      if dia>=1 and dia <=28 :
         print("Invierno")
   elif mes=="marzo" :
      if dia>=1 and dia <=20 :
         print("Invierno")
      elif dia>=21 and dia<=31 :
         print("Primavera")
   elif mes=="abril" :
      if dia>=1 and dia<=30 :
         print("Primavera")
   elif mes=="mayo" :
      if dia>=1 and dia<=31 :
         print("Primavera")
   elif mes=="junio" :
      if dia>=1 and dia<=20 :
         print("Primavera")
      elif dia>=21 and dia<=30 :
         print("Verano")
   elif mes=="julio" :
      if dia>=1 and dia<=31 :
         print("Verano")
   elif mes=="agosto" :
      if dia>=1 and dia<=31 :
         print("Verano")
   elif mes=="septiembre" :
      if dia>=1 and dia<=20 :
         print("Verano")
      elif dia>=21 and dia<=30 :
         print("Otoño")
   elif mes=="octubre" :
      if dia>=1 and dia<=31 :
         print("Otoño")
   elif mes=="noviembre" :
      if dia>=1 and dia<=30 :
         print("Otoño")
   elif mes=="diciembre" :
      if dia>=1 and dia<=20 :
         print("Otoño")
elif emisferio=="S" :
   if mes=="diciembre" :
      if dia>=21 and dia<=31 :
         print("Verano")
   elif mes=="enero" :
      if dia>=1 and dia <=31 :
         print("Verano")
   elif mes=="febrero" :
      if dia>=1 and dia <=28 :
         print("Verano")
   elif mes=="marzo" :
      if dia>=1 and dia <=20 :
         print("Verano")
      elif dia>=21 and dia<=31 :
         print("Otoño")
   elif mes=="abril" :
      if dia>=1 and dia<=30 :
         print("Otoño")
   elif mes=="mayo" :
      if dia>=1 and dia<=31 :
         print("Otoño")
   elif mes=="junio" :
      if dia>=1 and dia<=20 :
         print("Otoño")
      elif dia>=21 and dia<=30 :
         print("Invierno")
   elif mes=="julio" :
      if dia>=1 and dia<=31 :
         print("Invierno")
   elif mes=="agosto" :
      if dia>=1 and dia<=31 :
         print("Invierno")
   elif mes=="septiembre" :
      if dia>=1 and dia<=20 :
         print("Invierno")
      elif dia>=21 and dia<=30 :
         print("Primavera")
   elif mes=="octubre" :
      if dia>=1 and dia<=31 :
         print("Primavera")
   elif mes=="noviembre" :
      if dia>=1 and dia<=30 :
         print("Primavera")
   elif mes=="diciembre" :
      if dia>=1 and dia<=20 :
         print("Primavera")
else :
   print("Fecha incorrecta")
      
