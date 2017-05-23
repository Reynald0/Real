from django.template import Library

register = Library()

def get_comprobante_domicilio(dic, key):
    return dic.get(key)[0]

def get_credencial_estudiante(dic, key):
    return dic.get(key)[1]

def get_kardex(dic, key):
    return dic.get(key)[2]

register.filter("get_comprobante_domicilio", get_comprobante_domicilio)
register.filter("get_credencial_estudiante", get_credencial_estudiante)
register.filter("get_kardex", get_kardex)