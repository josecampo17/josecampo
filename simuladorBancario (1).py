__author__="Jose Manuel Campo Erazo"
__licence__="GPL"
__version__="1.0.0"
__email__="Jose.campoe@campusucc.edu.co"

#-------------------------------------------------------------------------------------------------------------
#importaciones
#-------------------------------------------------------------------------------------------------------------
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    # Aqui inicia la declaracion de la clase  

    """# ------------------------------------------------------------------------------------------------------
    # Atributo
    -------------------------------------------------------------------------------------------------------#"""

    __cedula = " "
    __nombre = " "
    __mesActual = 0

    """#-------------------------------------------------------------------------------------------------------
    #Asociaciones
    -------------------------------------------------------------------------------------------------------#"""

    __cuentaAhorros=CuentAhorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()

    """# ------------------------------------------------------------------------------------------------------
    # Metodos
    -------------------------------------------------------------------------------------------------------#"""

    __Saldo = 0
    
    """#-------------------------------------------------------------------------------------------------------
    # Metodos 
    -------------------------------------------------------------------------------------------------------#"""
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        self.__cuentaCorriente.ConsignarSaldo(monto)
      
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total de odas las cuentas"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        #total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.Darsaldo()
        return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()


    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "ninguno"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        #Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.Darsaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)

    __method__ = "Ahorrar"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __Description__ = "Pasa la cuenta corriente a la cuenta de ahorros"

    def Ahorrar(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.RetirarSaldo(monto)
        self._-CuentaCorriente.ConsignarSaldo(monto)

    __method__ = "RetirarAhorro"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __Description__ = "retira un valor dado en la cuenta de ahorros"

    def.RetirarAhorro(self, monto):
        self.__cuentaAhorros.RetirarValor(monto)
    
    __method__ = "RetirarTodo"
    __parameter__ = "Monto"
    __returns__ = "ninguno"
    __Description__ = "retira todo el dinero que hay en la cuenta de ahorros y corriente" 

    def RetirarTodo(self):
        self.__cuentaAhorros.RetirarSaldo(self.__cuentaAhorros.Darsaldo())
        self.__cuentaCorriente.RetirarSaldo(self.__cuentaAhorros.DarSaldo())

    __method__ = "DuplicarAhorro"
    __parameter__ = ""
    __returns__ = ""
    __Description__ = "Permite duplicar el ahorro" 

    def DuplicarAhorro(self):
        self.__cuentaAhorros.consignarvalor(self.__cuentaAhorros.DarSaldo())






