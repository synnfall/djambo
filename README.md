# DJAMBO

> **Un jeu d'exploration et de survie en 2D développé en Python avec Pygame.**

## Présentation

Dans **Djambo**, vous incarnez un sorcier piégé dans une série de labyrinthe obscures. L'obscurité est totale et oppressante, votre seule chance de survie ? La magie.

Le jeu repose sur une mécanique d'éclairage dynamique : le joueur émet une aura, mais pour voir plus loin et anticiper les murs du labyrinthe, il doit lancer des **boules de feu** qui illuminent les couloirs lors de leur passage.

Votre objectif est très simple : **Trouver la porte de sortie avant que le temps ne soit écoulé.**

## Les commandes du jeu

| Action | Touche (Clavier) |
| :--- | :--- |
| **Haut** | `Z` ou `Flèche HAUT` |
| **Bas** | `S` ou `Flèche BAS` |
| **Gauche** | `Q` ou `Flèche GAUCHE` |
| **Droite** | `D` ou `Flèche DROITE` |
| **Tirer** | `ESPACE` ( ou Clic Souris ) |
| **Quitter** | `ECHAP` ou fermer la fenêtre |

## Installation

> Python entre la version 3.10 à 3.12 est nécessaire.

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/synnfall/djambo.git
    cd djambo
    ```

2. **Créer l'environnement python :**
    ```bash
    python -m venv venv
    ```

3. **Charger l'environnement python**

    sur `Linux` :
    ```bash
    source venv/bin/activate
    ```

    sur `Windows` :
    ```bash
    venv\Scripts\activate
    ```

4.  **Installer la dépendance :**
    ```bash
    pip install pygame
    ```

5.  **Lancement du jeu :**
    ```bash
    python main.py
    ```

## Crédits
- [GUYON Eddy](https://github.com/synnfall)