# NebulaForge

## Description

NebulaForge est un projet d'apprentissage DevOps permettant de construire progressivement une infrastructure moderne similaire à celles utilisées en entreprise.

## Technologies utilisées

* Python
* PostgreSQL
* Docker
* Docker Compose

## Fonctionnalités

* Afficher les tâches
* Ajouter une tâche
* Modifier une tâche
* Supprimer une tâche

## Lancer le projet

```bash
docker compose up --build
```

## Exemple d'utilisation

Afficher les tâches :

```bash
curl localhost:8000/taches
```

Ajouter une tâche :

```bash
curl -X POST localhost:8000/taches \
-H "Content-Type: application/json" \
-d '{"nom":"Apprendre DevOps"}'
```
