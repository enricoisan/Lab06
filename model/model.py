from database import DAO
from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getAnni(self):
        return DAO.getAnni()

    def getBrands(self):
        return DAO.getBrands()

    def getRetailers(self):
        return DAO.getRetailers()

    def getVendite(self, anno, brand, retailer_code):
        return DAO.getVendite(anno, brand, retailer_code)

    def getStatistiche(self, anno, brand, retailer_code):
        return DAO.getStatistiche(anno, brand, retailer_code)