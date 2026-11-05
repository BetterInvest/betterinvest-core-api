# betterinvest-core-api

API backend de **BetterInvest**, application mobile éducative (style Duolingo) pour apprendre l'investissement de long terme.

Stack : **Python 3.12**, **FastAPI**, gestion des dépendances avec **uv**. Architecture en oignon (`domain` → `application` → `infrastructure` / `presentation`).

## Prérequis

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Docker (optionnel, pour l'image)

## Installation

```bash
uv sync
cp .env.example .env   # renseigner les clés si besoin
```

## Lancer l'API

```bash
uv run uvicorn betterinvest_api.main:app --reload --host 0.0.0.0 --port 8000
```

Endpoint disponible : `GET /health` → `{"status":"ok"}`.

## Commandes

| Commande | Description |
| --- | --- |
| `uv run ruff check .` | Lint |
| `uv run ruff format --check .` | Vérification du formatage |
| `uv run mypy` | Contrôle de types (strict) |
| `uv run pytest` | Tests |
| `docker build -t betterinvest-core-api .` | Build de l'image |

## Structure

```
src/betterinvest_api/
  domain/           # règles métier (aucune dépendance sortante)
  application/      # cas d'usage (dépend du domain)
  infrastructure/   # adaptateurs techniques
  presentation/     # routeurs FastAPI
infra/              # déploiement VPS (à venir : Docker Compose + Caddy)
```

Chaque couche contient un README décrivant son rôle et sa règle de dépendance. Le domaine métier n'est pas encore spécifié : seul le squelette est en place.

## Workflow Git (résumé)

- Branches longues : `main` (prod), `develop` (intégration)
- Travail : `feat/*` ou `fix/*` depuis `develop` ; hotfixes `hotfix/*` depuis `main`
- `feat`/`fix` → `develop` : squash ; release `develop` → `main` : merge commit + tag `vX.Y.Z`
- Détails : voir [CONTRIBUTING.md](CONTRIBUTING.md)

## Sécurité

Voir [SECURITY.md](SECURITY.md). Ne jamais committer de secrets (`.env`, clés, keystores).
