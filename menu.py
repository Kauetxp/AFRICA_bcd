# iniciando
import time
from consulta import consulta
from editar import edita
from excluir import exclui
from exibir import exibe
from inserir import insere

print("BEM VINDO AO BANCO DE DADOS DE ANIMAIS AFRICANOS")
time.sleep(0.5)
#Verificando o que irá rodar
rod = 2
print("SELECIONE UMA OPÇÃO")
print("1 - COLSULTA\n2 - EDITAR\n3 - INSERIR\n4 - EXCLUIR\n5 - EXIBIR TUDO")


while rod > 1:
    c = input()
    if c =="1":
        rod = 0
        consulta()
    elif c =="2":
        rod = 0
        edita()
    elif c =="3":
        rod = 0
        insere()
    elif c =="4":
        rod = 0
        exclui()
    elif c =="5":
        rod = 0
        exibe()
    else: 
        rod = 3

    