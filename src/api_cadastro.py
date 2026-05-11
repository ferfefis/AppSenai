import asyncio

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, Card, Row, TextField, ElevatedButton

from api_endpoint_cadastro import get_enderecos
from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Cadastro"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def cadastro():
        cep = input_cep.value
        numero = input_numero.value

        tem_erro = False
        if cep:
            input_cep.error = None
        else:
            input_cep.error = "Campo obrigatório"

        if numero:
            input_numero.error = None
        else:
            input_numero.error = "Campo obrigatório"

        if not tem_erro:
            endereco = get_enderecos(cep)
            text_cidade.value = endereco["localidade"]
            text_uf.value = endereco["uf"]
            text_logradouro.value = endereco["logradouro"]
            text_bairro.value = endereco["bairro"]

        # TODO: Montar a lista de personagens do seu jeito, capricha ein

    # Gerenciar as telas(routes)
    def route_change():

        # Carrega a primeira lista

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Cadastro", weight=FontWeight.BOLD),
                        bgcolor=Colors.PURPLE_500
                    ),
                    input_cep,
                    input_numero,
                    text_cidade,
                    text_uf,
                    text_logradouro,
                    text_bairro,
                    bnt_salvar
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    text_cidade = TextField(label="Cidade:", disabled=True, color=Colors.BLACK_87)
    text_uf = TextField(label="Uf:", disabled=True, color=Colors.BLACK_87)
    text_logradouro = TextField(label="Rua:", disabled=True, color=Colors.BLACK_87)
    text_bairro = TextField(label="Bairro:", disabled=True, color=Colors.BLACK_87)

    input_cep = TextField(label="Digite seu Cep")
    input_numero = TextField(label="Digite o numero da Casa")

    bnt_salvar = ElevatedButton("Salvar", color=Colors.PURPLE_800, on_click=lambda: cadastro())

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)