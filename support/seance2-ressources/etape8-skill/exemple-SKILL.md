---
name: nouvelle-route
description: Démarche pour ajouter une route Flask à note_app. À utiliser dès qu'on ajoute une page, un formulaire ou une action.
---

# Ajouter une route à note_app

1. Lire la route la plus proche dans app.py et la fonction associée dans database.py. Résumer le fonctionnement avant de coder.
2. Écrire un test qui échoue dans tests/test_<sujet>.py avec les fixtures client et login :
   - le cas nominal ;
   - utilisateur non connecté : 401 ;
   - données d'un autre utilisateur : refusé.
   Le lancer et montrer l'échec.
3. Base : une fonction dans database.py, requête paramétrée (?) uniquement.
4. Route dans app.py : vérifier la session, vérifier que la ressource appartient à l'utilisateur.
5. Template : formulaire en POST pour toute modification ; lien depuis la page concernée.
6. Lancer python -m pytest -q, relire le diff, commiter avec un message en français.
