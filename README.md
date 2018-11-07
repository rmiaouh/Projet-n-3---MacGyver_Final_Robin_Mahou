# Projet n°3 MacGyver_Final_Robin_Mahou

## Présentation du projet

L'objectif de ce projet était de réaliser un labyrinthe avec les fonctionnalités suivantes :

- [x] Il n'y a qu'un seul niveau. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
- [x] MacGyver sera contrôlé par les touches directionnelles du clavier.
- [x] Les objets seront répartis aléatoirement dans le labyrinthe et changeront d’emplacement si l'utilisateur ferme le jeu et le relance.
- [x] La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
- [x] MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
- [x] Il récupèrera un objet simplement en se déplaçant dessus.
- [x] Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
- [x] Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.

__________________________________


## Structuration du projet

Le projet se décompose de la façon suivante :

![Structure du projet](http://image.noelshack.com/fichiers/2018/45/3/1541582209-projet3ocr.png)

1. Le programme **Main.py** qui est le programme principale appellant les programmes secondaires. 
2. Le programme **Display.py** qui contient toutes les fonctions *d'affichage/rafraichissement des images* du jeu ainsi que les mouvements du joueur.
3. Le programme **Datas.py** qui conserve les liens vers les images et les sons du jeu.
4. Les programmes **Maze_Generator_1** & **Maze_Generator_2** qui eux sont utilisés dans la génération d'un labyrinthe aléatoire.

### - ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Main.py sa structuration détaillée
*(cette structuration s'appuie sur l'exemple donné durant le cours "pygame" du site OpenClassRooms)*

Le programme main est composé de la façon suivante : 
 
  Création de la fenêtre du jeu
  Initialisation des variables et appel du programme **Datas.py** qui conserve les configurations/images/sons. 
    Boucle while de la fenêtre(si on quitte cette boucle, le jeu s'éteint):
      Boucle while accueil(cette boucle gère le menu accueil):
        On attend que le joueur choisissent un niveau/start le jeu
        Quand le joueur décide, on génère aléatoirement un labyrinthe en faisant appel aux programmes **Maze_Generator_1 & 2**
        On sort de la boucle while accueil
      Si le choix du niveau == 1 (if):
        Boucle while du jeu(si on quitte cette boucle, le jeu se termine mais ne s'éteint pas):
          On met en place le Timer qui compte les secondes
          On active les mouvements du joueur en utilisant le programme **Display.py**
          à chaque mouvement du joueur on fait un rafraichissement de l'affiche toujours avec le programme **Display.py**
          
          Si (if) le joueur a les 3 items et que le joueur est sur la case du boss:
            Le joueur gagne + sons "you win"
            On reset ensuite les variables et on retourne dans la boucle accueil
          Si (if) le Timer == 0 secondes:
            Le joueur perd + sons "you loose"
            On reset ensuite les variables et on retourne dans la boucle accueil
            



