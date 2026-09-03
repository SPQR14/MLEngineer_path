import logging
import logger
from random import randint
from random import random

logger.setup_logger("app1")

log = logging.getLogger("Arithmetic App1")


def sumar(a, b):
    log.info(f"Entra a la función sumar con a={a} y b={b}")
    resultado = a + b
    log.debug(f"Resultado de la suma {a}+{b}={resultado}")
    return resultado


def restar(a, b):
    log.info(f"Entra a la función restar con a={a} y b={b}")
    resultado = a - b
    log.debug(f"Resultado de la resta {a}-{b}={resultado}")
    return resultado


def multiplicar(a, b):
    log.info(f"Entra a la función multiplicar con a={a} y b={b}")
    resultado = a * b
    log.debug(f"Resultado de la multiplicación {a}*{b}={resultado}")
    return resultado


def dividir(a, b):
    log.info(f"Entra a la función dividir con a={a} y b={b}")
    try:
        resultado = a / b
        log.debug(f"Resultado de la división {a}/{b}={resultado}")
        return resultado
    except ZeroDivisionError:
        log.error("División por cero")
        return None
    finally:
        log.info("Sale de la función dividir")
    

def potencia(a, b):
    log.debug(f"Entra a la función potencia con a={a} y b={b}")
    resultado = a ** b
    log.info(f"Resultado de la potencia {a}^{b}={resultado}")
    return resultado


def especial(*args):
    log.info(f"Entra a la función especial con los argumentos {args}")
    try:
        resultado = sum(args)
        log.debug(f"Resultado de la función especial {args}={resultado}")
        return resultado
    except TypeError:
        log.warning("Tipos de dato incompatibles para la suma de la función especial")
        return None
    finally:
        log.debug("Sale de la función especial")


for i in range(100):
    sumar(randint(1, 2000), randint(1, 2000))
    restar(randint(1, 2000), randint(1, 2000))
    multiplicar(randint(1, 2**i), random())
    dividir(randint(1,2000), randint(-10,10))
    potencia(2, randint(1, 100))
    especial(random(), random(), random(), random())
    especial(1, 2, 3, 4, str(randint(1, 100)))
