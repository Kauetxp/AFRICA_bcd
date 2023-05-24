def exclui():
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
    
    busca = input("Digite o nome da raca que deseja excluir: ")
    sql = "SELECT * FROM tb_animal WHERE raca LIKE %s"
    val = ("%" + busca + "%",)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result:
        cod = result[0]
        nome = result[1]
        confirmacao = input(f"Tem certeza que deseja deletar a tribo '{nome}'? (s/n) ")

        if confirmacao.lower() == "s":
            sql = "DELETE FROM tb_animal WHERE id = %s"
            val = (cod,)
            cursor.execute(sql, val)
            con.commit()
            print("Item deletado com sucesso!")
        else:
            print("Operação cancelada pelo usuário")

    else:
        print("Erro, verifique os dados")
    con.close()
    
#exclui()
    