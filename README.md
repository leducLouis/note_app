# notes-app

Petite application web Flask : connexion, prise de notes, dépôt d'images et page d'administration des comptes. Données stockées dans trois bases SQLite (`database_file/`).

## Lancer l'application

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
python app.py                    # http://localhost:5000
```

## Lancer les tests

```bash
python -m pytest
```

Les tests utilisent des bases temporaires : ils ne modifient pas les données de `database_file/`.

## Comptes de test

| Identifiant | Mot de passe |
|---|---|
| admin | admin |
| test | 123456 |

## Pages

- **Public** : accessible à tous.
- **Private** : notes et images de l'utilisateur connecté.
- **Admin** : réservée au compte admin, liste, ajout et suppression de comptes.

## Origine

Adapté de l'exercice `flask-api` du dépôt [kousen/claude-code-training](https://github.com/kousen/claude-code-training) (licence MIT, voir `LICENSE`), lui-même basé sur [XD-DENG/flask-example](https://github.com/XD-DENG/flask-example).

Images : private.jpg, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:(315-365)_Locked_(6149414678).jpg) ; public.jpg, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Drown%3F!_(131380682).jpg).
