 
#==2 ejercicio  
while True:
    print("Ingrese nota 1")
    n1 = int(input("> "))
    if n1 < 1 or n1 > 7:
        continue
    while True:
        print("Ingrese nota 2")
        n2 = int(input("> "))
        if n2 < 1 or n2 > 7:
            continue
        while True:
            print("Ingrese nota 3")
            n3 = int(input("> "))
            if n3 < 1 or n3 > 7:
                continue
            while True:
                print("Ingrese nota 4")
                n4 = int(input("> "))
                if n4 < 1 or n4 > 7:
                    continue
            else:
                suma = n1 + n2 + n3 + n4
                promedio = suma / 3
                print(f"Su promedio es de: {promedio}")
                break      



