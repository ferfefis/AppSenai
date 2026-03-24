import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
from flet.controls import page


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_nome():
        text.value = f"Bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    # Componentes
    text = Text("")
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    # Construção da tela
    page.add(
        Column(
            [
                input_nome,
                input_sobrenome,
                btn_salvar,
                text
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )
    # Funções
    def verificar():
        try:
            n1 = int(input_numero.value)
            result = n1 % 2
            if result == 0:
                text.value = f'{n1} , Seu número é par!'
            else:
                text.value = f'{n1} , Seu número é impar!'
        except ValueError:
            text.value = f'Apenas numeros!'

    # Componentes
    text_verificar = Text()
    input_numero = TextField(label="Digite o primeiro numero")
    btn_verificar = OutlinedButton("Verificar", on_click=verificar)

    # Construção da tela
    page.add(
        Column(
            [
                input_numero,
                btn_verificar,
                text_verificar
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    def nascimento():
        idade = int(input_nascimento.value)
        resultado_idade = 2026 - idade
        if resultado_idade >= 18:
            text.value = f"Ele tem {resultado_idade} anos. Ele é maior de idade, "
            page.update()
        else:
            text.value = f"Ele tem {resultado_idade} anos. Ele é menor de idade, "
            page.update()

    # componentes
    input_nascimento = TextField(label="Digite o ano de nascimento")
    btn_verificar2 = OutlinedButton("Verificar", on_click=nascimento)
    text_verificar = Text()

    # Contrução da tela
    page.add(
        Column(
            [
                input_nascimento,
                btn_verificar2,
                text_verificar
            ],
            width=400,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

flet.app(main)
