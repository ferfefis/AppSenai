import asyncio

import flet

from flet import ThemeMode, View, AppBar, Colors, Button, FloatingActionButton, Icons, TextField, ListView, Text, Card, \
    Column, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, DropdownOption, Switch


class Maquina_de_venda():
    def __init__(self, marca, cor, categoria, cofre, quantidade_itens):
        self.marca = marca
        self.cor = cor
        self.categoria = categoria
        self.cofre = cofre
        self.quantidade_itens = quantidade_itens



def main(page: flet.Page):
    # Configurações
    page.title = "Máquina de Vendas"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # Funções
    # Função de navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )



    def montar_lista_padrao():
        list_view.controls.clear()

        # Item é uma pessoa com nome, profissão e sexo
        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.LIGHTBULB_CIRCLE_OUTLINED),
                    title=item.marca,
                    subtitle=(f"A máquina contém: {item.categoria}"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("Ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, maquina=item: ver_detalhes(maquina)),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda:excluir(item)),
                        ]
                    ),
                )
            )

    def ver_detalhes(maquina):
        text_marca.value = maquina.marca
        text_cor.value = maquina.cor
        text_categoria.value = maquina.categoria
        text_cofre.value = "Possui Cofre" if maquina.cofre else "Não possui cofre"
        text_quantidade_itens.value = maquina.quantidade_itens

        navegar("/detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        marca = input_marca.value.strip()
        categoria = input_categoria.value.strip()
        cor = input_cor.value.strip()
        cofre = input_cofre.value
        quantidade_itens = input_quantidade_itens.value.strip()
        print(cofre)

        tem_erro = False
        if marca:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatório"

        if cor:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatório"

        if categoria:
            input_categoria.error = None
        else:
            tem_erro = True
            input_categoria.error = "Campo obrigatório"

        if quantidade_itens:
            input_quantidade_itens.error = None
        else:
            tem_erro = True
            input_quantidade_itens.error= "Campo obrigatório"



        if not tem_erro:
            # Montar o objeto
            maquina = Maquina_de_venda(
                marca = marca,
                cor = cor,
                categoria = categoria,
                cofre = cofre,
                quantidade_itens = quantidade_itens,
            )

            # add objeto na lista
            lista_dados.append(maquina)

            # limpando campos
            input_marca.value = ""
            input_cor.value = ""
            input_categoria.value = ""
            input_cofre.value = True
            input_quantidade_itens.value = ""


        montar_lista_padrao()

    # Função de gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Máquina de Vendas",
                        bgcolor=Colors.RED_200
                    ),
                    list_view,
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                        ),
                        input_marca,
                        input_cor,
                        input_categoria,
                        input_cofre,
                        input_quantidade_itens,
                        btn_salvar,
                    ]
                )
            )

        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                        ),
                        Text(f"Marca: {text_marca.value}"),
                        Text(f"Cor: {text_cor.value}"),
                        Text(f"Categoria: {text_categoria.value}"),
                        text_cofre,
                        Text(f"Quantidade de itens: {text_quantidade_itens.value}"),
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
    input_marca = TextField(label="Marca", hint_text="Digite a marca da sua máquina")
    input_cor = TextField(label="Cor", hint_text="Digite a cor da sua máquina")
    input_categoria = TextField(label="Categoria", hint_text="Digite a categoria da sua máquina")
    input_cofre = Switch(label="Cofre")
    input_quantidade_itens = TextField(label="Quantidade de itens", hint_text="Ex: 10")

    text_marca = Text()
    text_cor = Text()
    text_categoria = Text()
    text_cofre = Text()
    text_quantidade_itens = Text()

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()

flet.run(main)