# Padel blog site de démonstration, test technique

## Fonctionnalités principales

- **Gestion des articles** : Créez et publiez des articles avec une interface moderne.
- **Gestion des événements** : Gérez et affichez des événements avec des dates et des images.
- **Formulaire de contact** : Permet aux utilisateurs d'envoyer des messages via un formulaire simple.

## Prérequis

- **Python 3.12+**
- **Poetry** : Utilisé pour gérer les dépendances du projet.

## Installation

```git clone https://github.com/lecramc/padelBlog/```

1. **Installer `pipx`** si nécessaire :

    ```bash
    python -m pip install --user pipx
    python -m pipx ensurepath
    ```

2. **Installer `Poetry`** via `pipx` :

    ```bash
    pipx install poetry
    ```

3. **Entrer dans l'environnement virtuel Poetry** :

    ```bash
    poetry shell
    ```

4. **Lancer l'application** avec le script de développement :

    ```bash
    ./entrypoint-dev.sh
    ```
5. **Utilisation**

   Une fois l'application lancée, vous pouvez vous connecter ou vous inscrire à l'adresse suivante : `http://localhost:8000`.
   
   Se connecter avec les identifiants de test :
   
      - Nom d'utilisateur : `admin`
      - Mot de passe : `test`


## Accès à la documentation API

La documentation de l'API est disponible à l'adresse : `http://localhost:8000/api/docs/`

## Accès à Django Admin

Pour ajouter des articles ou des événements, connectez-vous à l'interface **Django Admin**.

1. Ouvrez le navigateur à l'adresse : `http://localhost:8000/admin/`
2. Connectez-vous avec vos identifiants d'administrateur.
3. Ajoutez un nouvel article ou un événement dans les sections correspondantes.

PS : Le fichier .env a été laissé a des fins de demonstration. Il est recommandé de créer un fichier .env personnalisé pour votre environnement.