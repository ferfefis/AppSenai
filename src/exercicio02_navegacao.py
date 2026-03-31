import asyncio

import flet

from flet import ThemeMode, View, AppBar, Colors, Button, TextField, Text


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções

    def exibir_informacoes():
        text_nome.value = f"Nome:{input_nome.value}"
        text_cpf.value = f"CPF:{input_cpf.value}"
        text_email.value = f"E-mail:{input_email.value}"
        text_salario.value = f"Salario: R${input_salario.value}"


        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Campo obrigatorio!"


        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Campo obrigatorio!"


        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Campo obrigatorio!"

        if input_salario.value:
            input_salario.error= None
        else:
            tem_erro = True
            input_salario.error = "Campo obrigatorio!"

        if not tem_erro:
            # Limpando os Inputs
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
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
                        title="Cadastro do Funcionário",
                        bgcolor=Colors.AMBER_200,
                    ),
                    Text("Digite seus dados para se cadastrar"),
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
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
                            title="Seus dados:",
                            bgcolor=Colors.AMBER_200,
                        ),
                        text_nome,
                        text_cpf,
                        text_email,
                        text_salario
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
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="E-mail")
    input_salario = TextField(label="Salário")
    text_nome = Text()
    text_cpf = Text()
    text_email = Text()
    text_salario = Text()
    btn_salvar = Button("Salvar", on_click= exibir_informacoes)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)