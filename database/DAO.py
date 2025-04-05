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

    @staticmethod
    def getVendite(anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT YEAR(ds.Date) AS Year, 
                        ds.Unit_sale_price * ds.Quantity AS Revenue, 
                        ds.Retailer_code, 
                        ds.Product_number
                    FROM go_daily_sales AS ds
                    JOIN go_products AS p ON ds.Product_number = p.Product_number
                    WHERE YEAR(ds.Date) = COALESCE(%s, YEAR(ds.Date))
                    AND p.Product_brand = COALESCE(%s, p.Product_brand)
                    AND ds.Retailer_code = COALESCE(%s, ds.Retailer_code)
                    ORDER BY Revenue DESC
                    LIMIT 5;
"""

        cursor.execute(query, (anno, brand, retailer_code,))

        res = []
        for row in cursor:
            res.append(
                f"Year: {row['Year']}, Revenue: {row['Revenue']}, Retailer_code: {row['Retailer_code']}, Product_number: {row['Product_number']}")

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStatistiche(anno, brand, retailer_code):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT SUM(Unit_sale_price * Quantity) as TotalVolume,
		                COUNT(*) as SalesNum,
		                COUNT(DISTINCT(ds.Product_number)) as ProdNum,
		                COUNT(DISTINCT(ds.Retailer_code)) as RetNum
                    FROM go_daily_sales AS ds
                    JOIN go_products AS p ON ds.Product_number = p.Product_number
                    WHERE YEAR(ds.Date) = COALESCE(%s, YEAR(ds.Date))
                    AND p.Product_brand = COALESCE(%s, p.Product_brand)
                    AND ds.Retailer_code = COALESCE(%s, ds.Retailer_code)
    """

        cursor.execute(query, (anno, brand, retailer_code,))
        row = cursor.fetchone()
        res = f"Giro d'affari: {row["TotalVolume"]}\nNumero vendite: {row["SalesNum"]}\nNumero retailers: {row["RetNum"]}\nNumero prodotti: {row["ProdNum"]}"
        cursor.close()
        cnx.close()
        return res


