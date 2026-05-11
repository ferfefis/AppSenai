import asyncio

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, Card, Row

from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def verificar_gender(item):
        if item["gender"] == "Male":
            cor = Colors.RED_500
            return cor
        elif item["gender"] == "Female":
            cor = Colors.GREEN_500
            return cor
        elif item["gender"] == "Unknown":
            cor = Colors.YELLOW_500
            return cor
        elif item["gender"] == "Other":
            cor = Colors.PURPLE_500
            return cor

    def montar_lista_personagens():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_personagens()

        # item é um apelido para o objeto que esta vindo da api
        for item in lista_dados ["items"]:
            list_view.controls.append(
                Card(
                    height=300,
                    content=Row([
                        Image(src=item["image"], width=100),
                        Column([
                        Text(item["name"], weight=FontWeight.BOLD, color=Colors.ORANGE_500),
                        Text("Ki", weight=FontWeight.BOLD, color=Colors.ORANGE_200),
                        Text(item["ki"], max_lines=2),
                        Text("Race", weight=FontWeight.BOLD, color=Colors.ORANGE_200),
                        Text(item["race"], max_lines=2),
                        Text("Gender", weight=FontWeight.BOLD, color=Colors.ORANGE_200),
                        Text(item["gender"], max_lines=2, color = verificar_gender(item)),
                        ])

                    ],
                        margin=8
                    ),

                )
            )
        # TODO: Montar a lista de personagens do seu jeito, capricha ein

    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for item in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=item["image"], width=60),
                    title=Text(item["name"], weight=FontWeight.BOLD, color=Colors.ORANGE_300),
                    subtitle=Text(item["description"], max_lines=2),
                )
            )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar as telas(routes)
    def route_change():

        # Carrega a primeira lista
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    Column([
                        pagelet,
                    ])
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

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.MAN, label="Personagens"),
                NavigationBarDestination(icon=Icons.BLUR_ON, label="Planetas"),
            ],
            on_change=define_lista,
        ),
        content=Column([
                    list_view,
                ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600,
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)