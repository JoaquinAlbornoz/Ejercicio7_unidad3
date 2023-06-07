from zope.interface import Interface
class Icoleccion(Interface):
    def InsertarElemento(indice,elemento):
        pass
    def AgregarElemento(elemento):
        pass
    def mostrarElemento(indice):
        pass