from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from selenium import webdriver
from time import sleep

class CadastroProduto(App):
    def build(self):
        # LAYOUT
        layout1 = GridLayout(cols=1, spacing=10, size_hint_y=None, height=600)
        layout1.bind(minimum_height=layout1.setter('height'))

        layout1.add_widget(Label(text='Hora de cadastrar os produtos!'))
        layout1.add_widget(Label(text='Nome'))
        self.nome = TextInput(multiline=False)
        layout1.add_widget(self.nome)

        layout1.add_widget(Label(text='GTIN'))
        self.gtin = TextInput(multiline=False)
        layout1.add_widget(self.gtin)

        layout1.add_widget(Label(text='Peso'))
        self.peso = TextInput(multiline=False)
        layout1.add_widget(self.peso)

        layout1.add_widget(Label(text='Preço'))
        self.preco = TextInput(multiline=False)
        layout1.add_widget(self.preco)

        layout1.add_widget(Label(text='Link/Url'))
        self.url = TextInput(multiline=False)
        layout1.add_widget(self.url)

        self.buscar = Button(text='Buscar', size_hint_x=None, width=100)
        self.buscar.bind(on_press=self.buscar_descricao)
        layout1.add_widget(self.buscar)

        layout1.add_widget(Label(text='Janela de Saída - Editar Descrição'))

        self.descricao = TextInput(multiline=True)
        layout1.add_widget(ScrollView(size_hint=(1, None), height=200, pos_hint={'center_x':.5}))
        layout1.children[8].add_widget(self.descricao)

        boxlayout1 = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        self.cadastrar = Button(text='Cadastrar Produto')
        self.cadastrar.bind(on_press=self.cadastrar_produto)
        boxlayout1.add_widget(self.cadastrar)

        self.novo_produto = Button(text='Novo Produto')
        self.novo_produto.bind(on_press=self.limpar_campos)
        boxlayout1.add_widget(self.novo_produto)

        self.finalizar = Button(text='Finalizar Programa')
        self.finalizar.bind(on_press=self.stop)
        boxlayout1.add_widget(self.finalizar)

        layout1.add_widget(boxlayout1)

        # JANELA
        self.janela1 = layout1

        return self.janela1

    def buscar_descricao(self, *args):
        url = self.url.text
        if 'https://' not in url:
            self.popup = App.get_running_app().root
            self.popup.popup = Popup(title='ERRO!!!', content=Label(text='Insira um Link para iniciar uma busca.'), size_hint=(None, None), size=(400, 200))
            self.popup.popup.open()
        else:
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            sleep(5)
            descricao = self.driver.find_element_by_xpath('//h1').text
            self.descricao.text = descricao

    def cadastrar_produto(self, *args):
        nome = self.nome.text
        gtin = self.gtin.text
        peso = self.peso.text
        preco = self.preco.text
