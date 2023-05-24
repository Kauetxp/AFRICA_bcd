def edita():
    
    import mysql.connector
    x = 0
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
    busca = input("Digite o nome da raça que deseja editar: ")
    sql = "SELECT * FROM tb_animal WHERE raca LIKE %s"
    val = ("%" + busca + "%",)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    
    if result:
        cod = result[0]
        nome_antigo = result[1]
        hab_ant = result[2]
        ext_ant = result[3]
        reg_ant = result[4]
        
        print(result,"\nO que você deseja editar? (Digite o número)")
        print("1 - Raça")
        print("2 - Habitantes")
        print("3 - Extinção")
        print("4 - Região")
        op = int(input(""))
        
        if op == 1:
            print(f"A raça atual é '{nome_antigo}'.")
            novo_nome = input("Digite o novo nome: ")
            sql = "UPDATE tb_animal SET raca = %s WHERE id = %s"
            val = (novo_nome, cod)
            cursor.execute(sql, val)
            con.commit()
        
        
        elif op == 2:
            print(f"O número de animais atual é '{hab_ant}'.")
            novo_hab = input("Digite o novo número: ")
            sql = "UPDATE tb_animal SET quantidade = %s WHERE id = %s"
            val = (novo_hab, cod)
            cursor.execute(sql, val)
            con.commit()
            
        elif op == 3:
            print(f"Extinção '{ext_ant}'.")
            novo_ren = input("Digite o dado: ")
            sql = "UPDATE tb_animal SET risco_extincao = %s WHERE id = %s"
            val = (novo_ren, cod)
            cursor.execute(sql, val)
            con.commit()
            
            
        elif op == 4:
            print(f"A região atual é: '{reg_ant}'.")
            novo_esc = input("Digite a nova região: ")
            sql = "UPDATE tb_animal SET area_encontrada = %s WHERE id = %s"
            val = (novo_esc, cod)
            cursor.execute(sql, val)
            con.commit()
            
            
        else:
            x = 5
            print("ERRO")
            
        
        if x != 5:
            print("Item atualizado com sucesso!")
        else:
            print("Operação cancelada")
            
    else:
        print("Não foi encontrado nenhum registro com o nome informado.")
    
    con.close()
    
#edita()