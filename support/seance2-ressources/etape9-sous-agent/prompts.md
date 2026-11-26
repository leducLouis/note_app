# Étape 9 : sous-agents et modèles

```
mkdir -p .claude/agents
cp <ressources>/etape9-sous-agent/relecteur-securite.md .claude/agents/
cp <ressources>/etape9-sous-agent/traducteur.md .claude/agents/
```

Relancer `claude`, puis :

```
/agents
```

```
Utilise le sous-agent relecteur-securite sur les derniers commits.
```

```
Utilise le sous-agent traducteur pour traduire README.md en anglais dans README.en.md.
```

Pour la session principale :

```
/model opusplan
```

(Opus en plan mode, Sonnet pour exécuter.)
