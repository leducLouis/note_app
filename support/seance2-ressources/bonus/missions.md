# Bonus, s'il reste du temps

Même méthode pour chacune : plan mode, plan annoté, hook actif, un commit par étape, relecteur à la fin.

## Refonte de la base
Supprimer toutes les injections SQL de database.py, puis fusionner les 3 bases en une seule
avec clés étrangères, et écrire un script de migration qui conserve les données existantes.

## Algo
Recherche dans ses notes, classée par pertinence (score de type TF-IDF, insensible à la casse
et aux accents), avec des tests de propriétés : une note qui contient tous les mots cherchés
arrive avant une note qui n'en contient qu'un.

## Système
Configuration par variables d'environnement (SECRET_KEY, mode debug), journal des connexions
réussies et échouées, workflow GitHub Actions qui lance les tests à chaque push.
