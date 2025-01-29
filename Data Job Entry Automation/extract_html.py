from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

print(soup.prettify())

with open('html.html', 'w') as file:
    file.write(soup.prettify())

listings = soup.find_all(name="li",
                         class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

for listing in listings:
    # Adresse
    address = listing.find("address", {"data-test": "property-card-addr"})
    address_text = address.text.strip() if address else "Non disponible"

    # Lien vers l'offre
    link = listing.find("a", {"data-test": "property-card-link"})
    link_href = link["href"] if link else "Non disponible"

    # Prix
    price = listing.find("span", {"data-test": "property-card-price"})
    price_text = price.text.strip() if price else "Non disponible"

    # Détails (chambres, salles de bain, surface)
    details = listing.find("ul", class_="StyledPropertyCardHomeDetailsList")
    if details:
        details_items = [item.text.strip() for item in details.find_all("li")]
    else:
        details_items = ["Non disponible"]

    # Afficher les informations extraites
    print(f"Adresse: {address_text}")
    print(f"Lien: {link_href}")
    print(f"Prix: {price_text}")
    print(f"Détails: {', '.join(details_items)}")
    print("-" * 40)
