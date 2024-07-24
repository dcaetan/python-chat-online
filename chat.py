import flet as ft

def main(pagina):
    txt_title_pg = ft.Text("Chat Online")

    chat = ft.Column()

    def enviar_msg_tunel(mensagem):
        print(mensagem)
        # add msg no chat
        txt_enviar_msg_field_chat = ft.Text(mensagem)
        chat.controls.append(txt_enviar_msg_field_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviar_msg(evento):
        print("Btn ENVIAR ok!")
        pagina.pubsub.send_all(f"{user_name.value}: {msg_field_chat.value}")
        
        # limpar campo de msg do chat
        msg_field_chat.value = ""
        pagina.update()


    msg_field_chat = ft.TextField(label="Digite sua mensagem...", on_submit=enviar_msg)
    btn_send_msg_field_chat = ft.ElevatedButton("Enviar", on_click=enviar_msg)

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
        pagina.pubsub.send_all(f"{user_name.value} entrou...")
        # add campo para escrever msg
        pagina.add(msg_field_chat)
        # add btn enviar msg
        pagina.add(btn_send_msg_field_chat)
        # atualizar para os elementeos aparecerem na pagina
        pagina.update()

    title_popup = ft.Text("Olá, vamos começar?!")
    user_name = ft.TextField(label="Qual seu nome?", on_submit=abrir_chat)
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

ft.app(target=main, view=ft.WEB_BROWSER)
    