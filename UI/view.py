import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.dd1 = None
        self.dd2 = None
        self.dd3 = None
        self.btn1 = None
        self.btn2 = None
        self.label1 = None


    def load_interface(self):

        # Titolo
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        # Riga 1
        self.dd1 = ft.Dropdown(label = "Anno")
        self._controller.filldd1()

        self.dd2 = ft.Dropdown(label = "Brand")
        self._controller.filldd2()

        self.dd3 = ft.Dropdown(label = "Retailer")
        self._controller.filldd3()


        row1 = ft.Row([self.dd1, self.dd2, self.dd3], alignment=ft.MainAxisAlignment.CENTER)

        self.btn1 = ft.ElevatedButton(text = "Top vendite")
        self.btn2 = ft.ElevatedButton(text = "Analizza vendite")
        row2 = ft.Row([self.btn1, self.btn2], alignment=ft.MainAxisAlignment.CENTER)

        # List View
        self.lvTxtOut = ft.ListView(expand=True)

        self._page.add(row1, row2, self.lvTxtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
