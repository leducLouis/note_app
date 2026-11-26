# Étape 4 : hook

```
mkdir -p .claude/hooks
cp <ressources>/etape4-hook/tests.sh .claude/hooks/
chmod +x .claude/hooks/tests.sh
cp <ressources>/etape4-hook/settings.json .claude/settings.json
```

Relancer `claude`, puis :

```
/hooks
```

```
Renomme la route /write_note en /notes/new.
```

Windows : dans tests.sh, remplacer .venv/bin/python par .venv/Scripts/python.exe
(le hook s'exécute avec Git Bash).
