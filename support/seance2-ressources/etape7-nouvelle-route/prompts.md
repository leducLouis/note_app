# Étape 7 : nouvelle route « modifier une note », pas à pas

Un prompt à la fois. Lire la réponse et le diff avant de passer au suivant.

```
Explique-moi comment fonctionne l'ajout d'une note, de la route jusqu'à la base. Ne modifie rien.
```

```
Écris un test qui échoue dans tests/test_edit_note.py : l'auteur peut modifier sa note ;
un utilisateur non connecté reçoit 401 ; un autre utilisateur ne peut pas modifier la note.
Lance-le pour montrer qu'il échoue.
```

```
Ajoute dans database.py une fonction de mise à jour d'une note, avec une requête paramétrée.
```

```
Ajoute la route /edit_note/<note_id> : GET affiche un formulaire prérempli, POST enregistre.
Vérifie que la note appartient à l'utilisateur connecté.
```

```
Ajoute un lien « Modifier » à côté de chaque note sur la page Private.
```

Puis : lancer les tests, relire le diff, commiter.
