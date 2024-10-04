# Padel blog

## Fonctionnalités principales

- **Gestion des articles** : Créez et publiez des articles avec une interface moderne.
- **Gestion des événements** : Gérez et affichez des événements avec des dates et des images.
- **Formulaire de contact** : Permet aux utilisateurs d'envoyer des messages via un formulaire simple.

## Prérequis

- **Python 3.12+**
- **Poetry** : Utilisé pour gérer les dépendances du projet.

## Installation

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

## Accès à la documentation API

La documentation de l'API est disponible à l'adresse : `http://localhost:8000/api/docs/`

## Accès à Django Admin

Pour ajouter des articles ou des événements, connectez-vous à l'interface **Django Admin**.

1. Ouvrez le navigateur à l'adresse : `http://localhost:8000/admin/`
2. Connectez-vous avec vos identifiants d'administrateur.
3. Ajoutez un nouvel article ou un événement dans les sections correspondantes.

## Utilisation

Une fois l'application lancée, vous pouvez vous connecter ou vous inscrire à l'adresse suivante : `http://localhost:8000`.

