#Comando de inserção

def insere():
    import mysql.connector
    import random
    config = {
      'user': 'usuarioremoto',
      'password': 'grunge1994',
      'host': '172.31.84.191',
      'database': 'africa'
    }
    
    try:
        con = mysql.connector.connect(**config)
        print("Conexão com banco executada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err} ")
        
    cursor = con.cursor()
    
    cod = (random.randint(0,1000000) - random.randint(0,100))
    n_tribo = input("Raça: ")
    n_habita = input("População: ")
    renda = input("Risco de extinção: (sim/nao): ")
    renda = renda.lower()
    escol = input("Região em que vivem: ")
    val = (cod,n_tribo,n_habita,renda,escol)
    
    
    comando = "INSERT INTO tb_animal VALUES (%s,%s, %s,%s, %s)"
    cursor.execute(comando, val)
    
    con.commit()
    
    print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")
    
    con.close()
    
#insere()