import flet as ft

def main(pagina):
    txt = ft.Text("Chat Online")

    def abrir_chat(evento):
        pass
    title_popup = ft.Text("Olá, vamos começar?!")
    name_user = ft.TextField(label="Qual seu nome?")
    btn_iniciar_chat = ft.ElevatedButton("Entrar", on_click=abrir_chat)

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=title_popup, 
        content=name_user, 
        actions=[btn_iniciar_chat]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    btn_iniciar = ft.ElevatedButton("Inicar Chat", on_click=abrir_popup)
    
    pagina.add(txt)
    pagina.add(btn_iniciar)

ft.app(target=main)
    