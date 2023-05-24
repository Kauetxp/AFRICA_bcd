def consulta():
    
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
        
    cursor = con.cursor()
    busca = input("Digite o nome da raça que deseja cunsultar: ")
    sql = "SELECT * FROM tb_animal WHERE raca LIKE %s"
    val = ("%" + busca + "%",)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    print(result)
    
    con.close()
