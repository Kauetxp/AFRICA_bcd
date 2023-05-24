#Essa é a função de exibir

def exibe():
    import mysql.connector

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
        
    comando = "Select * from tb_animal"
    cursor = con.cursor()
    cursor.execute(comando)
    result = cursor.fetchall()
    for linhas in result:
        print(linhas)
        
    con.close()

#exibe()