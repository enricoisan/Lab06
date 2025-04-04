import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def filldd1(self):
        self._view.dd1.options.append(ft.dropdown.Option("Nessun filtro"))
        for anno in self._model.getAnni():
            self._view.dd1.options.append(ft.dropdown.Option(anno))

    def filldd2(self):
        self._view.dd2.options.append(ft.dropdown.Option("Nessun filtro"))
        for brand in self._model.getBrands():
            self._view.dd2.options.append(ft.dropdown.Option(brand))

    def filldd3(self):
        self._view.dd3.options.append(ft.dropdown.Option("Nessun filtro"))
        for retailer in self._model.getRetailers():
            self._view.dd3.options.append(ft.dropdown.Option(key = retailer.retailer_code,
                                                             text=retailer.retailer_name,
                                                             data=retailer,
                                                             on_click=self.read_retailer))

    def read_retailer(self, e):
        self.retailer = e.control.data
        # self._view.lvTxtOut.controls.append(ft.Text(f"Hai selezionato {self.retailer}"))
        # self._view.update_page()