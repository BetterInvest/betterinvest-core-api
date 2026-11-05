# Contribuer

## Branches longues

- `main` : production
- `develop` : intégration

## Branches de travail

Partir de `develop` avec les préfixes :

- `feat/` — nouvelle fonctionnalité
- `fix/` — correctif (les tâches de type *chore* utilisent aussi `feat/` ou `fix/` selon le contexte ; le type de commit `chore:` reste autorisé)

Hotfixes : `hotfix/*` partant de `main`.

Il n'y a **pas** de préfixe `chore/`.

## Flux de fusion

| Flux | Méthode |
| --- | --- |
| `feat/*` ou `fix/*` → `develop` | **squash merge** |
| Release `develop` → `main` | **merge commit** (jamais squash ni rebase), puis tag `vX.Y.Z` sur `main` |
| `hotfix/*` → `main` | **merge commit** + tag, puis immédiatement une PR de back-merge `main` → `develop` en merge commit |

Les tags `v*` sont réservés à Enzo et Yanis.

## Pull requests

- 1 approbation minimum
- CI verte (`lint`, `typecheck`, `test`, `branch-source-check` pour les PR vers `main`)
- Conversations résolues
- Branche à jour avec la base

## Push

- `git push --force-with-lease` autorisé **uniquement** sur votre branche de travail
- Jamais de force-push sur `main` ni `develop`

## Commits

Conventional Commits, en anglais (ex. `feat: add health endpoint`, `chore: bump dependencies`).
