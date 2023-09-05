def jugar():

    print('================================')
    print('Bienvenido al Juego del Ahorcado')
    print('================================')
    
     
    palabra_secreta = 'mandarina'
    letras_acertadas=['_','_','_','_','_','_','_','_','_']
    
    ahorcado = False
    acerto = False
    
    while ( not ahorcado and not acerto ):
        entrada = input ("ingrese una letra...")
        entrada = entrada.strip()
        entrada = entrada.lower()
        indice = 0
        for letra in palabra_secreta:
            if(entrada == letra):
                letras_acertadas[indice]=letra
            
            indice = indice +1
        print(letras_acertadas)

    print("Fin del Juego")
    
if(__name__ == "__main__"):
   jugar()
