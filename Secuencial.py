import math

pesos= int(input ("Digite el valor en pesos:"))
dolares= pesos * 0.00027
print ("El valor en dolares es:",dolares)

numero= float(input("Digite el numero a conseguirle el valor absoluto:"))
vabsoluto= math.fabs(numero)
print ("El valor absoluto del numero es: ",vabsoluto)



presion = float(input("Digite la presion:"))
volumen = float(input("Digite la volumen:"))
temperatura= float(input("Digite la temperatura:"))
masa= (presion * volumen) * (0.37* (temperatura + 460))
print ("La masa del aire es: ",masa)




edad = int(input("Digite la edad:"))
npulsaciones= (220 - edad)/10
print ("Tu numero de pulsaciones por cada 10 segundos debe ser de: ",npulsaciones)




salario = float(input("Digite el salario: "))
incremento = salario * 0.25
nsalario= incremento + salario
print ("El nuevo salario con el incremento es: ",nsalario)


presupuesto = float(input("Digite el presupuesto del hospital: "))
Pediatria= presupuesto * 0.30
Ginecologia= presupuesto * 0.40
Traumatologia= presupuesto * 0.30
print("El porcentaje del presupuesto para Pediatria es de: ",Pediatria)
print("El porcentaje del presupuesto para Ginecologia es de: ",Ginecologia)
print("El porcentaje del presupuesto para Traumatologia es de: ",Traumatologia)


precioc = float(input("Digite el precio de compra: "))
por30 = precioc*0.30
preciov = por30 + precioc
print("El precio de venta del articulo para ganarle el 30% es ",preciov)}

tlunes = int(input("Digite el tiempo recorrido el dia Lunes de esta semana  cantidad de minutos"))
tmiercoles = int(input("Digite el tiempo recorrido el dia Miercoles de esta semana en cantidad de minutos"))
tviernes = int(input("Digite el tiempo recorrido el dia Viernesde esta semana en  cantidad de minutos"))
promediot= (tlunes + tmiercoles + tviernes)/3
print ("El promedio de tiempo en la ruta esta semana fue de ",promediot, " minutos")


cantt = float(input("Digite la cantidad total invertida en pesos es: "))
cantp1= float(input("Digite la cantidad invertida por la primera persona: "))
cantp2= float(input("Digite la cantidad invertida por la segunda persona: "))
cantp3= float(input("Digite la cantidad invertida por la tercera persona: "))
por1 = (cantp1 * 100) /cantt
por2 = (cantp2 * 100) /cantt
por3 = (cantp3 * 100) /cantt
print( "El porcentaje del primer inversor es:",por1)
print( "El porcentaje del segundo inversor es:",por2)
print( "El porcentaje del tercer inversor es:",por3)


print("Este es un programa para calcular el promedio de tus tres materias escogidas como las mas dificiles:")
examm = float(input("Digite la nota del examen de matematicas: "))
tarea1m= float(input("Digite la nota de la primera tarea de matematicas: "))
tarea2m= float(input("Digite la nota de la segunda tarea de matematicas: "))
tarea3m= float(input("Digite la nota de la tercera tarea de matematicas: "))
portareasm= ((tarea1m + tarea2m + tarea3m)/3)*0.10
porexamm= examm * 0.90
notamate= porexamm + portareasm
examf = float(input("Digite la nota del examen de fisica: "))
tarea1f = float(input("Digite la nota de la primera tarea de fisica: "))
tarea2f = float(input("Digite la nota de la segunda tarea de fisica: "))
portarea1f= tarea1f * 0.10
portarea2f= tarea2f * 0.10
porexamf= examf * 0.80
notafisica= portarea1f + portarea2f + porexamf
examq = float(input("Digite la nota del examen de quimica: "))
tarea1q = float(input("Digite la nota de la primera tarea de quimica: "))
tarea2q = float(input("Digite la nota de la segunda tarea de quimica: "))
tarea3q = float(input("Digite la nota de la segunda tarea de quimica: "))
portareasq= ((tarea1q + tarea2q + tarea3q)/3)*0.15
porexamq= examq * 0.85
notaquimica= portareasq + porexamq
promtotal= (notamate + notafisica + notaquimica)/3
print( "El promedio de Matermatica es:",notamate)
print( "El promedio de Fisica es:",notafisica)
print( "El promedio de Quimica es:",notaquimica)
print( "El promedio de Total de las 3 materias es:",promtotal)











