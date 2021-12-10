# Règles du jeu 
Le Cambiecolo est un jeu de cartes.  <br/>
Le but est de se constituer une main de 5 cartes affichant le même moyen de transport.
Les différents moyens de transports sont : <br/>
 - avion
 - voiture
 - train
 - vélo
 - pied  <br/>

Au début de la partie on distribue 5 * nombre_de_joueurs cartes avec autant de moyen de transport que de joueur. (3 joueurs = 15 cartes avec 3 moyens de transports)
On place une cloche au milieu des joueurs.
Les joueurs peuvent alors échanger de 1 à 3 cartes identiques en annonçant le nombre de cartes souhaités. Le joueur échange alors ses cartes avec le premier adversaire qui accepte et le jeu continue jusqu'à ce qu'un joueur réunisse 5 cartes identiques et sonne la cloche. Il gagne alors de nombre de points asociés au moyen de transport réuni.

## Contraintes techniques
Le jeu doit contenir 3 types de processus :  <br/>
 - Le processus principal
 - Le processus "jeu" &rarr; traque la session de jeu, les offres et la cloche.
 - Le processus "joueur" &rarr; processus intéragissant avec l'utilisateurs, traque ses cartes et les offres. Les interations avec le processus "jeu" sont traités dans un thread séparé. <br/>

Au niveau de la communication inter-processus les offres doivent être stockés dans de la __mémoire partagée__ alors que la communication entre les joueurs doit s'effectueur par un __message queue__