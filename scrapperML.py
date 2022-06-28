"""
Con este script, utilizamos BeautifulSoup 4 para hacer un request html y recorrer el dom, con el fin de listar todos los articulos en venta que cumplan con el criterio de búsueda.
Los artículos listados, devuelven nombre, precio, y link de la publicacion. 
"""

import requests #py -m pip install requests beautifulsoup4
#py -m pip install html5lib
from bs4 import BeautifulSoup
import re
#from bs4.diagnose import diagnose


url = "https://instrumentos.mercadolibre.com.ar/instrumentos-cuerdas-guitarras-criollas/usado/_OrderId_PRICE_PriceRange_1000-0_NoIndex_True#applied_filter_id%3Dprice%26applied_filter_name%3DPrecio%26applied_filter_order%3D3%26applied_value_id%3D1000-*%26applied_value_name%3Dnull1000-null*%26applied_value_order%3D4%26applied_value_results%3DUNKNOWN_RESULTS%26is_custom%3Dtrue"
if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
  
    results = soup.find_all( class_=re.compile("ui-search-result__content ui-search-link")) 
    
    
    print(len(results))
    for anuncio in results:
        try:
            title = anuncio.find("h2").get_text()
            anunciolink = anuncio.get("href")
            price = anuncio.find(class_=re.compile("price-tag-fraction")).get_text()
            print("------------")
            print(title)
            print(price)
            print(anunciolink)
        except Exception as e:
            print ("Exception: {}".format(e))
            pass
