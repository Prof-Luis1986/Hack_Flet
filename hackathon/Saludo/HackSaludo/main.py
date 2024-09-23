import flet as ft

def mostrar_nombre(text_field, page):
    
    nombre = text_field.value
    dialog = ft.AlertDialog(
        title=ft.Text("Mostrar Nombre"),
        content=ft.Text(f"Tu nombre es: {nombre}" + " Bienvenido a Flet"),
        actions=[
            ft.TextButton("Da click para salir", on_click=lambda e: close_dialog(page))
        ],
    )
    
    page.dialog = dialog
    page.dialog.open = True
    

def close_dialog(page):
    page.dialog.open = False

def main(page: ft.Page):
    page.title=("Mostrar Nombre")
    
    page.bgcolor = "Blue"
    
    text_field = ft.TextField()
    
    button = ft.ElevatedButton(
        text="Di mi nombre", 
        on_click=mostrar_nombre(text_field, page)
    )
    
    page.add(
        ft.Row(controls=[
            text_field,
            button
        ])
    )

ft.app(target=main)
