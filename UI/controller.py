import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.retailer_code = None
        self.retailer = None
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


    def handleb1(self, e):
        self._view.lvTxtOut.controls.clear()

        anno = self._view.dd1.value
      #  if anno is None:
      #      self._view.create_alert("Attenzione, selezionare un anno!")
      #      self._view.update_page()

        if anno == "Nessun filtro":
            anno = None
        else:
            anno = int(anno)

        brand = self._view.dd2.value
    #    if brand is None:
    #        self._view.create_alert("Attenzione, selezionare un brand!")
    #        self._view.update_page()
        if brand == "Nessun filtro":
            brand = None

    #    if self.retailer is None:
    #        self._view.create_alert("Attenzione, selezionare un retailer!")
    #        self._view.update_page()
        if self._view.dd3.value == "Nessun filtro":
            retailer_code = None
        else:
            retailer_code = int(self.retailer.retailer_code)

        vendite = self._model.getVendite(anno, brand, retailer_code)
        if not vendite:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun elemento trovato"))
            self._view.update_page()
        else:
            for v in vendite:
                self._view.lvTxtOut.controls.append(ft.Text(v))
            self._view.update_page()

    def handleb2(self, e):
        self._view.lvTxtOut.controls.clear()

        anno = self._view.dd1.value
        if anno is None:
            self._view.create_alert("Attenzione, selezionare un anno!")
            self._view.update_page()

        if anno == "Nessun filtro":
            anno = None
        else:
            anno = int(anno)

        brand = self._view.dd2.value
        if brand is None:
            self._view.create_alert("Attenzione, selezionare un brand!")
            self._view.update_page()
        if brand == "Nessun filtro":
            brand = None

        if self.retailer is None:
            self._view.create_alert("Attenzione, selezionare un retailer!")
            self._view.update_page()
        if self._view.dd3.value == "Nessun filtro":
            retailer_code = None
        else:
            retailer_code = int(self.retailer.retailer_code)

        statistiche = self._model.getStatistiche(anno, brand, retailer_code)
        if not statistiche:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun elemento trovato"))
            self._view.update_page()
        else:
            self._view.lvTxtOut.controls.append(ft.Text("Statistiche vendite:"))
            self._view.lvTxtOut.controls.append(ft.Text(statistiche))
            self._view.update_page()

