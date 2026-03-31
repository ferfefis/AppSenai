import asyncio

import flet

from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Text


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700
    input_nome = TextField(label="Nome")

    # Funções
    def exibir_mensagem():
        text_mensagem.value = f"Bom dia {input_nome.value}!"
        input_nome.value = ""
        navegar("/tela_mensagem")

    # Função de navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # Função de gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Identificação",
                        bgcolor=Colors.AMBER_200,

                    ),
                    Text("Digite seu nome para receber uma mensagem"),
                    input_nome,
                    btn_salvar,
                ]
            )
        )
        if page.route == "/tela_mensagem":
            page.views.append(
                View(
                    route="/tela_mensagem",
                    controls=[
                        flet.AppBar(
                            title="Mensagem",
                            bgcolor=Colors.AMBER_200,
                        ),
                        text_mensagem,
                    ]
                )
            )

    # Função de voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
            
    # Componentes
    input_nome = TextField(label="Nome")
    text_mensagem = Text()
    btn_salvar = Button("Salvar", on_click= exibir_mensagem)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)