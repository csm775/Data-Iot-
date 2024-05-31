import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
import random # import du random pour sélectionner aléatoirement un personnage
from machine import Pin, PWM # Import des fonctions pour gérer les broches de sortie et la modulation du signal

# Initialisation du module Wi-Fi en mode client
wlan = network.WLAN(network.STA_IF) 
wlan.active(True) # Active le mode client Wi-Fi

# Informations de connexion au réseau Wi-Fi
ssid = 'iPhone de csm77'
password = 'cellou7775'
wlan.connect(ssid, password) # Connecte la Raspberry Pi au réseau Wi-Fi


url = "https://hp-api.lainocs.fr/characters/"

# Dictionnaire des maisons 
houses = {"Gryffindor": (30000, 1000, 1000),
          "Slytherin": (1000, 30000, 1000),
          "Hufflepuff": (int((227*30000)/255), 20000, 1000),
          "Ravenclaw": (int((30*30000)/255), int((144*30000)/255), 30000)}

# Initialisation des broches PWM pour les LED
rouge = PWM(Pin(17, mode=Pin.OUT))
rouge.freq(1000)
vert = PWM(Pin(18, mode=Pin.OUT))
vert.freq(1000)
bleu = PWM(Pin(19, mode=Pin.OUT))
bleu.freq(1000)

# Mise à zéro des intensités des LED
rouge.duty_u16(0)
vert.duty_u16(0)
bleu.duty_u16(0)

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)

print("GET")
r = urequests.get(url)  # Lancer une requête sur l'URL
slugs = [item["slug"] for item in r.json()]
r.close()  # Fermer la demande

# Sélectionne aléatoirement un "slug" de personnage
try:
    selected_slug = random.choice(slugs)
    character_url = f"{url}{selected_slug}"
    print("GET", character_url)
    r = urequests.get(character_url)  # Lancer une requête sur l'URL du personnage
    character = r.json()
    print("Nom:", character["name"])
    print("Maison:", character["house"])  # Traiter la réponse en JSON

    # Définir l'intensité des LED en fonction de la maison du personnage
    if character["house"] in houses:
        intensity = houses[character["house"]]
        rouge.duty_u16(intensity[0])
        vert.duty_u16(intensity[1])
        bleu.duty_u16(intensity[2])
    else:
        print("Maison non reconnue")

    r.close()  # Fermer la demande
    utime.sleep(1)  # Attendre 1 seconde avant de terminer
except Exception as e:
    print(f"Erreur : {e}")  # Afficher toute exception survenue pendant l'exécution


