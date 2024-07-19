# Calcular en total de compar de artículos
#Nomeplatura con el identificador snake_case
def calcular_costo_total (cuadernos, zapatos,alimentos): #funcionalidad
    total= cuadernos+zapatos+alimentos
    return total

#variables

cuadernos=29 #Dato enteros (int)
zapatos=30.75 #Dato flotante (float)
alimentos=52.08 #Dato flotante

#llamar la funcion

costo_total=calcular_costo_total(cuadernos,zapatos,alimentos)

# Tipos de datos de las variables

print(f'El costo total de los artículos es de : ${costo_total:.2f}')
#.2f indica que numero flotante despues del punto del numero entero van dos cifras
if isinstance(cuadernos, float)and isinstance(zapatos, float)and isinstance(alimentos, float):
    print(costo_total)

else:
    print("DATOS ERRONEOS")
