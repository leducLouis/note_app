# note_app

Appli Flask de prise de notes : comptes, notes, images, page admin.
Python 3.8+, Flask 3, SQLite sans ORM.

## Commandes
- Installer : python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
- Tests : python -m pytest -q
- Lancer : python app.py (http://localhost:5000, comptes test/123456 et admin/admin)

## Architecture
- app.py : toutes les routes Flask et la gestion de session
- database.py : accès SQLite, une fonction par opération
- database_file/ : les 3 bases (users, notes, images)
- templates/ : pages Jinja ; static/ : CSS, JS et images
- tests/ : pytest ; conftest.py crée des bases temporaires

## Règles
- SQL toujours paramétré (?), jamais de concaténation
- Ne pas modifier tests/test_app.py ; nouveaux tests dans tests/test_<sujet>.py
- Bug : écrire d'abord un test qui échoue
- Pas de nouvelle dépendance sans me demander
- Un commit par étape, message en français

## Pièges
- Les chemins des bases sont relatifs : lancer depuis la racine du projet
- Les tests ne touchent jamais database_file/ : passer par les fixtures client et login de conftest.py
