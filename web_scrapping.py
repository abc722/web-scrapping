from bs4 import BeautifulSoup

# İstediğiniz web sitesini ziyaret edin ve HTML kodunu çekin
import requests
url = "https://www.usom.gov.tr/adres"
r = requests.get(url)
html_content = r.text

# HTML kodunu Beautiful Soup ile işleyin
soup = BeautifulSoup(html_content, "html.parser")

# İstediğiniz verileri seçin ve bir txt dosyasına yazdırın
with open("scrapped_data_2.txt", "w") as f:
    for tag in soup.find_all("tr"):  # <p> etiketleri içinde arama yapın
        text = tag.text  # etiket içindeki metni alın
        f.write(text + "\n")  # metni dosyaya yazın ve satır atlayın
