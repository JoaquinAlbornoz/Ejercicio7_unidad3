from manpersonal import lista
from personal import docente
from personal import apoyo
from personal import investigador
from personal import docenteinvestigador
def test(): 
    a = lista()
    a.instanciar()
    x = int(input('ingrese el numero de opcion: '))
    while x>0 and x<9:
        match x:
            case 1:
                indice = int(input('ingrese posicion para insertar elemento: '))
                print('ingrese los siguientes datos: ')
                tipo = input('tipo de personal: ')
                cuil = input('cuil: ')
                ape = input('apellido: ')
                nom = input('nombre: ')
                sueldobasico = int(input('sueldo basico: '))
                anti = int(input('antigÜedad: '))
                if tipo == 'docente':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    personal = docente(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra)
                elif tipo == 'apoyo':
                    categoria = input('categoria: ')
                    personal = apoyo(cuil, ape, nom, sueldobasico, anti, categoria)
                elif tipo == 'investigador':
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    personal = investigador(cuil, ape, nom, sueldobasico, anti, areainv, tipoinv)
                elif tipo == 'docenteinvestigador':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    catprog = input('categoría en el programa de incentivos de investigación: ')
                    impextra = int(input('importe extra por docencia e investigación: '))
                    investigacion = input('investigacion: ')
                    personal = docenteinvestigador(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra, areainv, tipoinv, catprog, impextra, investigacion)
                a.InsertarElemento(indice,personal)
            case 2:
                print('ingrese los siguientes datos: ')
                tipo = input('tipo de personal: ')
                cuil = input('cuil: ')
                ape = input('apellido: ')
                nom = input('nombre: ')
                sueldobasico = int(input('sueldo basico: '))
                anti = int(input('antigÜedad: '))
                if tipo == 'docente':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    personal = docente(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra)
                elif tipo == 'apoyo':
                    categoria = input('categoria: ')
                    personal = apoyo(cuil, ape, nom, sueldobasico, anti, categoria)
                elif tipo == 'investigador':
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    personal = investigador(cuil, ape, nom, sueldobasico, anti, areainv, tipoinv)
                elif tipo == 'docenteinvestigador':
                    carre = input('carrera: ')
                    cargo = input('cargo: ')
                    catedra = input('catedra: ')
                    areainv = input('area de investigacion: ')
                    tipoinv = input('tipo de investigacion: ')
                    catprog = input('categoría en el programa de incentivos de investigación: ')
                    impextra = int(input('importe extra por docencia e investigación: '))
                    investigacion = input('investigacion: ')
                    personal = docenteinvestigador(cuil, ape, nom, sueldobasico, anti, carre, cargo, catedra, areainv, tipoinv, catprog, impextra, investigacion)
                a.AgregarElemento(personal)
            case 3:
                indice = int(input('ingrese posicion para mostrar elemento: '))
                a.mostrarElemento(indice)
            case 4:
                a.docinv()
            case 5:
                a.cont()
            case 6:
                a.most()
            case 7:
                a.catte()
            case 8:
                a.guarda()
        x = int(input('ingrese el numero de opcion: '))

if __name__=='__main__':
    test()