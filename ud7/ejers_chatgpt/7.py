class CuentaBancaria:
    def __init__(self, __saldo: float):
        if __saldo > 0:
            self.__saldo = __saldo
        else:
            print("el deposito debe de ser mayor a 0")

    def depositar(self, deposito: float):
        if deposito > 0:
            self.__saldo += deposito
        else:
            print("El deposito debe ser mayor a 0")

    def retirar(self, retirado: float):
        if retirado > 0 and retirado <= self.__saldo:
            self.__saldo -= retirado
        elif retirado > self.__saldo:
            print("No hay suficiente saldo para realizar el retiro")
        else:
            print("El monto a retirar debe ser mayor a 0")

    def consultar_saldo(self) -> str:
        return f"Tu saldo es de {self.__saldo}"

cuenta = CuentaBancaria(1000)

# Depositar 500
cuenta.depositar(500)

# Intentar retirar 200
cuenta.retirar(200)

# Intentar retirar más de lo que hay en la cuenta
cuenta.retirar(2000)

# Ver el saldo actual
print(cuenta.consultar_saldo())  # "Tu saldo es de 1300"