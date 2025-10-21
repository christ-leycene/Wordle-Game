

##  WORDLE GAME
Présentation

Wordle Game est une version en console du célèbre jeu de lettres Wordle, développée en Python.
Le but est simple : deviner un mot mystère en un nombre limité d’essais, avec des indices visuels à chaque tentative.
Ce projet m’a permis de renforcer mes bases en programmation structurée, modularité du code et gestion de fichiers.

## 📁 Structure du projet
```text
Wordle/
│
├── README.md             # Documentation du projet 
├── display.py                # Gère l'affichage du jeu (console, couleurs, etc.)
├── main.py                   #  Point d'entrée du programme 
├── validate_guess.py      # Vérifie la validité des propositions de mots
├── word.txt               # Fichier contenant la liste de mots possibles
├── word_choice.py         # Sélectionne un mot aléatoire dans la liste
└── wordle.py              # Logique principale du jeu Wordle

 ``` 


## Fonctionnement du jeu

Le joueur doit deviner un mot mystère de 5 lettres en un maximum de 6 essais.
Après chaque proposition, le programme affiche :

Les lettres bien placées
Les lettres mal placées
Les lettres absentes

Exemple :

Mot à deviner : _ _ _ _ _
Essai 1 : TABLE
Résultat : T🟨 A🟩 B⬜ L⬜ E⬜
Essai 2 : TRACE
Résultat : T🟩 R🟩 A🟩 C⬜ E🟩
Bravo, mot trouvé en 2 essais.


## Points techniques

-Utilisation de modules Python séparés pour chaque fonctionnalité (validation, affichage, sélection du mot).
-Lecture des mots à partir d’un fichier externe (words.txt).
-Gestion des erreurs de saisie utilisateur (taille du mot, caractères invalides).
-Couleurs et symboles pour améliorer la lisibilité dans le terminal.


## Compétences développées

-Programmation modulaire en Python
-Utilisation de fichiers externes
-Manipulation de chaînes de caractères
-Logique de comparaison et conditions
-Organisation d’un projet en plusieurs modules

