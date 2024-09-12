__author__="Jose Manuel Campo Erazo"
__licence__="GPL"
__version__="1.0.0"
__email__="Jose.campoe@campusucc.edu.co"

class CuentaCorriente:
 # Aqui inicia la declaracion de la clase  

    """# ------------------------------------------------------------------------------------------------------
    # Atributo
    -------------------------------------------------------------------------------------------------------#"""

    __Saldo = 0
    
    """#-------------------------------------------------------------------------------------------------------
    # Metodos 
    -------------------------------------------------------------------------------------------------------#"""
        __method__ = " DarSaldo"
        __parameter__ = "Ninguno"
        __returns__ = "Saldo de la cuenta"
        __Description__ = "Metodo que retorna el saldo de la cuenta del cliente"
    def DarSaldo(self): 
        # Aqui inicia mi codigo
        return self.__Saldo

        __method__ = "ConsignarSaldo"
        __parameter__ = "Monto"
        __returns__ = "Ninguno"
        __Description__ = "metodo que permite consignar un monto a la cuenta del cliente"
    def ConsignarSaldo(self, monto):
        # Aqui inicia mi codigo
        self.__Saldo = self.__Saldo+Monto

        __method__ = "RetirarSaldo"
        __parameter__ = "Monto"
        __returns__ = "Ninguno"
        __Description__ = "Metodo que permite retirrar un monto de la cuenta del cliente"
    def RetirarSaldo(self, monto):
        # Aqui inicia mi codigo
        self.Saldo = self.__Saldo-Monto

 