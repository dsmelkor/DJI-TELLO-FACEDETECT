"""
esto es un codigo de pruebas
"""
print ('hola mundo')

var1=0

for i in range (5):
    var1+=1
    print (var1)


def mensaje():
    print ('hola funcion')
    print ("esto es una funcion")

mensaje ()

def suma (num1, num2):
    resultado= num1+num2
    return resultado

clResultado=suma(2,3)
print ('resultado =',clResultado)