import asyncio

import flet

from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Text, Container, Column, Row, Icon, Icons, \
    CrossAxisAlignment, FontWeight
from flet.controls.border_radius import horizontal


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def exibir_informacoes():
        text_nome.value = input_nome.value
        text_marca.value = input_marca.value
        text_cor.value = input_cor.value
        text_categoria.value = input_categoria.value
        text_qnt_itens.value = input_qnt_itens.value

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio!"

        if input_marca.value:
            input_marca.error = None
        else:
            tem_erro = True
            input_marca.error = "Campo obrigatorio!"

        if input_cor.value:
            input_cor.error = None
        else:
            tem_erro = True
            input_cor.error = "Campo obrigatorio!"

        if input_categoria.value:
            input_categoria.error = None
        else:
            tem_erro = True
            input_categoria.error = "Campo obrigatorio!"

        if input_qnt_itens.value:
            input_qnt_itens.error = None
        else:
            tem_erro = True
            input_qnt_itens.error = "Campo obrigatorio!"

        if not tem_erro:
            # Limpando os Inputs
            input_nome.value = ""
            input_marca.value = ""
            input_cor.value = ""
            input_categoria.value = ""
            input_qnt_itens.value = ""
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
                        title="Cadastre sua máquina",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("Digite aqui os dados da máquina:"),
                    input_nome,
                    input_marca,
                    input_cor,
                    input_categoria,
                    input_qnt_itens,
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
                            title="Dados da máquina:",
                            bgcolor=Colors.AMBER_200,
                        ),
                        Container(
                            Column([
                                text_nome,
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_label_marca, text_marca
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_label_cor,text_cor
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_label_categoria,text_categoria
                                ]),
                                Row([
                                    Icon(Icons.ARROW_RIGHT_ROUNDED, size=40),
                                    text_label_qnt_itens,text_qnt_itens
                                ]),
                            ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                        ),

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
    input_marca = TextField(label="Marca")
    input_cor = TextField(label="Cor")
    input_categoria = TextField(label="Categoria")
    input_qnt_itens = TextField(label="Quantidade de Itens")
    text_nome = Text(weight=FontWeight.BOLD, size=24)
    text_marca = Text()
    text_label_marca = Text("Marca: ",weight=FontWeight.BOLD, color=Colors.AMBER_500)
    text_cor = Text()
    text_label_cor = Text("Cor: ",weight=FontWeight.BOLD, color=Colors.AMBER_500)
    text_categoria = Text()
    text_label_categoria = Text("Categoria: ",weight=FontWeight.BOLD, color=Colors.AMBER_500)
    text_qnt_itens = Text()
    text_label_qnt_itens = Text("Quantidade de itens: ",weight=FontWeight.BOLD, color=Colors.AMBER_500)
    btn_salvar = Button("Salvar", on_click=exibir_informacoes)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
