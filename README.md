**Version 1.0**  *(quelques petites mise à jour seront à prévoir, comme des commentaires en plus etc... la suppression de code qui ne sert à rien ou qui comprend des fonctions béta sera supprimé)*

# 👉  Projet n°3 MacGyver Robin_Mahou

## :one: Présentation du projet

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


## :two: Structuration du projet

Le projet se décompose de la façon suivante :

![Structure du projet](http://image.noelshack.com/fichiers/2018/45/3/1541582209-projet3ocr.png)

1. Le programme **Main.py** qui est le programme principale appellant les programmes secondaires. 
2. Le programme **Display.py** qui contient toutes les fonctions *d'affichage/rafraichissement des images* du jeu ainsi que les mouvements du joueur.
3. Le programme **Datas.py** qui conserve les liens vers les images et les sons du jeu.
4. Les programmes **Maze_Generator_1** & **Maze_Generator_2** qui eux sont utilisés dans la génération d'un labyrinthe aléatoire.

### - ![#efc403](https://placehold.it/15/efc403/000000?text=+) Main.py sa structuration détaillée
*(cette structuration s'appuie sur l'exemple donné durant le cours "pygame" du site OpenClassRooms)*

Le programme main est composé de la façon suivante : 

![Structure du projet](http://image.noelshack.com/fichiers/2018/45/3/1541584075-projet3ocr2.png)

- ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `Variables diverses` appelle le programme **Datas.py**
- ![#42a440](https://placehold.it/15/42a440/000000?text=+) `Generation aléatoire du labyrinthe` appelle les programmes **Maze_Generator_1 & 2**
- ![#3d6fc1](https://placehold.it/15/3d6fc1/000000?text=+) `Mouvements_joueur` appelle le programme **Display.py**
- ![#3d6fc1](https://placehold.it/15/3d6fc1/000000?text=+) `Affichage` appelle le programme **Display.py**


            
# 👉 Lancez-vous !

Lancez le programme **Main.py** !
*Vous arriverez sur l'écran d'accueil du jeu*

Appuyez sur la touche **F1** !
*La partie se lance*

Utilisez les touches multidirectionnelles pour vous déplacer !
*Votre personnage se déplace*

Attention ! Vous avez 30 secondes pour ramasser les 3 items et vous rendre sur le boss pour lui casser la figure !

*Bonne chance*

##Requierements :
Numpy 1.15
Matplotlib 3.0
Pygame 1.9.4


**R.M**


