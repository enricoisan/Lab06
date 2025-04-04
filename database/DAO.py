from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT YEAR(Date) as Year
                    FROM go_daily_sales"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["Year"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrands():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT DISTINCT Product_brand
                    FROM go_products"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["Product_brand"])

        cursor.close()
        cnx.close()
        return res

    def getRetailers():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT * 
                    FROM go_retailers gr """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(row["Retailer_code"], row["Retailer_name"],
                                row["Type"], row["Country"]))

        cursor.close()
        cnx.close()
        return res