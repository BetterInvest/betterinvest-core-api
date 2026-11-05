# Presentation

Couche HTTP : routeurs FastAPI, schémas de requête/réponse, injection de dépendances.

**Règle de dépendance :** peut dépendre de `application` et du `domain`. Ne doit pas dépendre directement de `infrastructure` (passer par les ports / l'injection).
