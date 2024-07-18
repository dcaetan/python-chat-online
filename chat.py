import flet as ft

def main(pagina):
    txt_title_pg = ft.Text("Chat Online")

    chat = ft.Column()

    def enviar_msg(evento):
        print("Btn ENVIAR ok!")
        # add msg no chat
        txt_enviar_msg_chat = ft.Text(msg_chat.value)
        chat.controls.append(txt_enviar_msg_chat)
        # limpar campo de msg do chat
        msg_chat.value = ""
        pagina.update()

    msg_chat = ft.TextField(label="Digite sua mensagem...")
    btn_send_msg_chat = ft.ElevatedButton("Enviar", on_click=enviar_msg)

    def abrir_chat(evento):
        print("Btn ENTRAR ok!")
        # depois que clicar no btn iniciar chat, fazer limpeza...
        # fechar popup
        popup.open = False
        # tirar btn iniciar chat
        pagina.remove(btn_iniciar)
        # tirar titulo da pagina
        pagina.remove(txt_title_pg)        
        # depois de limpar a pagina, criar de fato o chat...
        # criar o chat
        pagina.add(chat)
        txt_user_name = ft.Text(f"{user_name.value} entrou...")
        chat.controls.append(txt_user_name)
        # add campo para escrever msg
        pagina.add(msg_chat)
        # add btn enviar msg
        pagina.add(btn_send_msg_chat)
        # atualizar para os elementeos aparecerem na pagina
        pagina.update()

    title_popup = ft.Text("Olá, vamos começar?!")
    user_name = ft.TextField(label="Qual seu nome?")
    btn_iniciar_chat = ft.ElevatedButton("Entrar", on_click=abrir_chat)

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=title_popup, 
        content=user_name, 
        actions=[btn_iniciar_chat]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    btn_iniciar = ft.ElevatedButton("Inicar Chat", on_click=abrir_popup)
    
    pagina.add(txt_title_pg)
    pagina.add(btn_iniciar)

ft.app(target=main)
    