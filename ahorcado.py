import random

def jugar():

    print('================================')
    print('Bienvenido al Juego del Ahorcado')
    print('================================')
       
    archivo=open('palabras.txt','r')
    palabras=[]
    for linea in archivo:
        linea=linea.strip()
        palabras.append(linea)
        
        
    archivo.close()
    numero=random.randrange(0,len(palabras))
    
    palabra_secreta = palabras[numero].lower()
    letras_acertadas =['_' for elemento in palabra_secreta]
    
    ahorcado = False
    acerto = False
    
    print(letras_acertadas)
    while ( not ahorcado and not acerto ):
        entrada=input ("ingrese una letra...")
        entrada=entrada.strip()
        entrada=entrada.lower()
        indice = 0
        for letra in palabra_secreta:
                if(entrada==letra):
                    letras_acertadas[indice] = letra
                
                indice = indice + 1     
        print(letras_acertadas)
        print('jugando...')
    print('fin del juego')
     
    
if(__name__ == "__main__"):

    jugar()