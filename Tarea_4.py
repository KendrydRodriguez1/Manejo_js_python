#No logre hacer_todo el ejercicio, le pido mil disculpas y soy consiente de mi mala calificacion.

import json

archivo = open("publicacion.json")
contenido = json.load(archivo)
profesores = []

Lista_profesores = []
datos = contenido
ca_cedula=[]
for pe in contenido:
    if pe['cedula'] != ca_cedula:
        ca_cedula[pe]=pe['cedula']
        me = me +1

print(me)
def Cantidad_pro():
 for i in datos:
    cedulas = []
    for x in Lista_profesores:
        cedulas = x['cedula']
        if not i['cedula'] in cedulas:
            Lista_profesores.append({'cedula': i['cedula'], 'apellido': i['apellidos']})

 cant_publicacion = []
 for publica in Lista_profesores:
    data = publica
    cedula_publica = publica['cedula']
    contar_publicacion = 0
    for dato in datos:
        if dato['cedula'] == cedula_publica:
            contar_publicacion += 1
        data['contar_publicacion'] == contar_publicacion
        cant_publicacion.append(data)
 publicaciones_totales=[]
 for dato in datos:
    articulos = [x ['articulos'] for x in Lista_profesores]
    if not dato['articulos'] in articulos:
        publicaciones_totales.append(dato)
 print('La canridad de publicaciones existentes es de: '+ str(len(publicaciones_totales)))

def construir():
    for docente in contenido:
        cedula = docente['cedula']
        apellidos = docente['apellidos']
        datos = {
            'cedula': cedula,
            'apellidos': apellidos,
            'publicaciones': 0,
            'tipos': {'CIENTIFICAS':0,'REGIONALES':0},
            'areas': []
        }
        if datos not in profesores:
            profesores.append(datos)
    publicaciones()
    areas()
    tipo_de_publicaciones()
    imprimir()
def publicaciones():
    for docente in profesores:
        cedula = docente['cedula']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                docente['publicaciones'] += 1
def tipo_de_publicaciones():
    for docente in profesores:
        cedula = docente['cedula']
        tipos = docente['tipos']
        for profesor in contenido:
            if profesor['cedula'] == cedula:
                tipo = profesor['tipobases']
                if tipo == "CIENTIFICAS":
                   tipos['CIENTIFICAS'] += 1
                else:
                    tipos['REGIONALES'] += 1
def areas():
    for docente in profesores:
          cedula = docente['cedula']
          areas_trabajadas = docente['areas']
          for profesor in contenido:
            if profesor['cedula'] == cedula:
                area = profesor['area']
                if not area in areas_trabajadas:
                   areas_trabajadas.append(area);

def imprimir():
    for docente in profesores:
        print(" ")
        print("==========================")
        print(f"Nombre: {docente['apellidos']}")
        print(f"Cedula: {docente['cedula']}")
        print(f"Publicaciones: {docente['publicaciones']}")
        print(" ")
        tipos = docente['tipos']
        print(f"Tipo de articulos publicados:")
        print(f"Cientificos: {tipos['CIENTIFICAS']}")
        print(f"Regionales: {tipos['REGIONALES']}")
        print(" ")
        areas = docente['areas'];
        print('Areas:')
        for key in areas:
            print(key)
        print("==========================")
        print(" ")
print(" ")
print("==================")
Cantidad_pro()
print("================")
if __name__ == "__main__":
    construir();