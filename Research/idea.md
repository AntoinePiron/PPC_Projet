# Notre choix d'implémentation

## Conception générale 
Pour la réalisation de ce projet nous avons décidé de partir sur un système implémentant un programme *__serveur__* et un programme *__client__*.  <br/>
Le serveur va correspondre au processus principal et se chargera de déclencher une partie en lançant un processus *__jeu__*.  <br/>
Le client va lui correspondre au processus joueur qui va interragir avec le serveur.  <br/>

## Déroulement d'une interraction client-serveur 
Au début de multiples clients se connectent à notre serveur. Ces derniers se voit proposés différents ID de parties et choisissent de se connecter à l'une d'entre-elle. Côté serveur, chaque client sera identifié par un unique ID également afin de pouvoir interragir facilement avec lui.  On pourra imaginer par exemple un dictionnaire avec pour clé les IDs clients (uniques et généré automatiquement lors d'une connection) <br/>
Une fois connecté le client est en attente du début de partie qui peut-être déclenché de 2 manières différentes : 
 - Un client demande un début de partie, tous les joueurs reçoivent une demande de confirmation pour lancer celle- ci et si tous le monde confirme la partie démarre.
 - Au bout d'un certains *time out* et d'un nombre minimal de joueur (3) une proposition automatique de début de partie est envoyée. <br/>

La partie se déroule alors comme prévu dans les règles. Une fois la partie finie on demande à chaque participant s'il veut rejouer. Si oui on le renvoie dans la selection des parties, sinon on ferme sa connection (on pourra éventuellement lui renvoyer ses statistiques : nombres de parties, nombres de victoires).

## Implémentations des différents éléments qui permettent le bon déroulement de la partie
Tout d'abord nous allons profiter de l'aspect POO de python. <br/>
Effectivement nous allons pouvoir créer un classe qui gère la main de chaque joueur avec le type et le nombre de carte. On pourra l'imaginer de la sorte : 
```python
import enum 

class cardType(enum.Enum):
    airplane = 1
    car = 2
    train = 3
    bike = 4
    shoes = 5

class Hand:
    #De base on a une main vide
    myHand = [0,0,0,0,0]
    
    def __init__(self, hand):
        self.myHand = hand
    
    def __str__(self):
        outstr = ""
        for i in range(self.myHand):
            outStr += "Carte %s : %s | "%(i, Animal(self.myHand[i]).name)
        return(outstr)
```
Il s'agit simplement d'un exemple montrant l'enum pour les cartes et comment la main serais affiché dans la console. 