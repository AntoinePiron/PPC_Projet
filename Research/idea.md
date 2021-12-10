# Notre choix d'implémentation

## Conception générale 
Pour la réalisation de ce projet nous avons décidé de partir sur un système implémentant un programme __serveur__ et un programme __client__.  <br/>
Le serveur va correspondre au processus principal et se chargera de déclencher une partie en lançant un processus __jeu__.  <br/>
Le client va lui correspondre au processus joueur qui va interragir avec le serveur.  <br/>

## Déroulement d'une interraction client-serveur 
Au début de nultiples clients se connectent à notre serveur. Ces derniers se voit proposés différents ID de parties et choisissent de se connecter à l'une d'entre-elle. Côté serveur, chaque client sera identifié par un unique ID également afind e pouvoir interragir facilement avec lui.  <br/>
Une fois connecté le client est en attente du début de partie qui peut-être déclenché de 2 manières différentes : 
 - Un client demande un début de partie, tous les joueurs reçoivent une demande de confirmation pour lancer celle- ci et si tous le monde confirme la partie démarre.
 - Au bout d'un certains *time out* et d'un nombre minimal de joueur (3)