# Checkpoint A — Lagouze

- Étudiant : Grégoire
- Identifiant GitHub : `Lagouze`
- Équipe : G03 — T01
- Dépôt partagé : [oranedlrch/esilv-marketpulse-g03-t01](https://github.com/oranedlrch/esilv-marketpulse-g03-t01)
- Périmètre du checkpoint : TD01 à TD04

## Travail réalisé au TD04

J’ai développé l’affichage des premières et dernières dates d’observation pour AAPL et SP500 dans la fonction réutilisable `display_market_summary()`.

Le travail a été réalisé sur la branche `feature/display-observation-dates`, puis enregistré dans le commit `f1410cc` (`feat: display first and last observation dates`). Après comparaison avec `main`, j’ai intégré la fonctionnalité dans mon `main` local par une fusion fast-forward. Le programme a été exécuté après la fusion pour vérifier son fonctionnement.

La fonctionnalité et les preuves ont ensuite été publiées dans le dépôt partagé de l’équipe.

## Exécution

Depuis la racine du dépôt :

```bash
python src/main.py
```

Résultat vérifié pour les deux séries : 21 observations, première date `2026-09-01` et dernière date `2026-09-30`.

## Preuves individuelles

| Fichier | Objet |
| --- | --- |
| [01_terminal_python.png](01_terminal_python.png) | Exécution de MarketPulse dans mon environnement. |
| [02_git_status_log.png](02_git_status_log.png) | État du dépôt et historique Git. |
| [03_branch_merge.png](03_branch_merge.png) | État des branches et preuve de la fusion locale. |

Les captures complètent l’historique Git, l’exécution du programme et l’explication des manipulations.
