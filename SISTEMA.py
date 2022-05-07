import sqlite3
import PySimpleGUI as sg

def Sistema():
    sg.theme("DarkBlue2")

    layout=[
        [sg.Text("ID:"),sg.Input('',size=(10,1)),sg.Text("CATEGORIA:"),sg.Input("",size=(20,1))],
        [sg.Text("INFORMACAO:")],
        [sg.Multiline('',size=(56,5))],
        [sg.Text(key='info')],
        [sg.Button("Pesquisar"),sg.Button("Inserir"),sg.Button("Atualizar")]
    ]

    janela=sg.Window("SISTEMA",layout)

    while True:
        eventos,valor=janela.read()
        try:
            serial= valor[0]
        except:
            print("")
        try:
            equip = valor[1]
        except:
            print("")
        try:
            info = valor[2]
        except:
            print("")

        banco = sqlite3.connect('acap.db')
        cursor = banco.cursor()

        if eventos == 'Inserir':
                     #Esse comando server para criar a tabela no arquivo ***.DB
                # cursor.execute("CREATE TABLE stock ( equip text,n_serie interger,info text)")
                    #Para criar a tabela comente essa linha de baixo.
                insert = cursor.execute(f"INSERT INTO stock VALUES('{equip}','{serial}','{info}')")
                cursor.execute("SELECT * FROM stock")
                banco.commit()
                tabela1=cursor.fetchmany()
                for c in tabela1:
                    output = "INSERIDO COM SUCESSO"
                    janela['info'].update(output)


        if eventos == 'Pesquisar':
            cursor.execute(f"SELECT equip, n_serie ,info FROM stock WHERE equip ='{equip}' OR n_serie = '{serial}' ORDER BY equip ASC")
            banco.commit()
            tabela1 = cursor.fetchall()
            for c in tabela1:
                output = f"ID:{c[1]}\n"f"CATEGORIA:{c[0]}\n"f"INFORMACOES:{c[2]}"
                janela['info'].update(output)


        if eventos == 'Atualizar':
            update = cursor.execute(f"UPDATE stock SET info = '{info}' WHERE n_serie = '{serial}'")
            banco.commit()
            cursor.execute(f"SELECT equip, n_serie ,info FROM stock WHERE equip ='{equip}' OR n_serie = '{serial}' ORDER BY equip ASC")
            banco.commit()
            tabela1=cursor.fetchall()
            for c in tabela1:
                output = f"ID:{c[1]}\n"f"CATEGORIA:{c[0]}\n"f"INFORMACOES:{c[2]}"
                janela['info'].update(output)
        if eventos == sg.WINDOW_CLOSED:
            break

Sistema()