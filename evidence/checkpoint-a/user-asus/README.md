# Checkpoint A — user-asus

- Étudiant : Nathan
- Identifiant GitHub : `user-asus`
- Équipe : G03 — T01
- Dépôt partagé : [oranedlrch/esilv-marketpulse-g03-t01](https://github.com/oranedlrch/esilv-marketpulse-g03-t01)
- Périmètre du checkpoint : TD01 à TD04

## Travail réalisé au TD04

J’ai développé l’affichage des premières et dernières dates d’observation pour AAPL et SP500 dans la fonction réutilisable `display_market_summary()`.

Le travail individuel a été enregistré sur la branche `feature/display-observation-dates` dans le commit `a4452f2` (`feat: display first and last observation dates`), puis intégré à mon `main` local.

Lors de la synchronisation de l’équipe, mon historique TD04 a été conservé dans `archive/td04-nathan` et dans la branche de fonctionnalité. Mon `main` a ensuite été aligné sur `origin/main`, la version partagée de l’équipe. Le programme a été exécuté après cette synchronisation pour vérifier son fonctionnement.

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
