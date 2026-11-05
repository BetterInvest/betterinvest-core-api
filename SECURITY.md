# Sécurité

## Signaler une vulnérabilité

Utilisez le **signalement privé de vulnérabilité** de GitHub (onglet *Security* → *Report a vulnerability*).

Ne créez **pas** d'issue publique pour un problème de sécurité. Décrivez l'impact, les étapes de reproduction et, si possible, une proposition de correctif. L'équipe accusera réception et traitera le signalement de façon confidentielle.

## Secret poussé par erreur

1. **Révoquez / rotatez immédiatement** le secret auprès du fournisseur (Supabase, Mistral, Marketstack, CoinGecko, etc.).
2. Ensuite seulement, nettoyez l'historique Git si nécessaire (et coordonnez-vous avec Enzo ou Yanis).
3. Prévenez l'équipe (Enzo / Yanis) pour vérifier qu'aucun usage abusif n'a eu lieu.

Les fichiers `.env*`, keystores et clés de compte de service ne doivent **jamais** être commités. Voir `.gitignore` et `.env.example`.
