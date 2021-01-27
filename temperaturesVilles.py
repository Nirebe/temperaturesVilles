# coding: UTF-8

"""
Script: pythonProject1/temperaturesVilles
Création: admin, le 15/01/2021
"""


# Imports
import mysql.connector
import requests
# Fonctions
def get_temperature(ville):
    url ="http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])

def set_bdd(temperatures, ville):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1',
    database='bdd_temperaturesvilles')
    cursor = cnx.cursor()
    update_val = ("UPDATE table_name SET temperatures = (%s) WHERE ville = (%s)")
    data = (temperatures, ville)
    cursor.execute(update_val, data)
    cnx.commit()
    cursor.close()
    cnx.close()
# Programme principal
def main():
    print(get_temperature('paris'))
    #set_bdd((get_temperature("paris")),"Paris")

if __name__ == '__main__':
    main()
# Fin
