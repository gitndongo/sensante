---
title: SenSante
emoji: 🏥
colorFrom: green
colorTo: blue
sdk: docker
app_port: 8000
---

# SenSante
Assistant de pre-diagnostic medical pour le Senegal.

## Demo en ligne

https://sokhnaaichaka-sensante.hf.space


## Description
SenSante utilise le Machine Learning pour aider au
pre-diagnostic des maladies courantes (paludisme,
grippe, typhoide) a partir des symptomes du patient.

## Structure du projet
- `data/` : Donnees patients (CSV)
- `models/` : Modele ML serialise
- `api/` : API FastAPI
- `frontend/` : Interface web
- `notebooks/` : Scripts d'exploration

## Stack

- scikit-learn (modele ML)
- FastAPI (API REST)
- Tailwind CSS (frontend responsive)
- Groq / Llama 3 (explication LLM)
- Docker (conteneurisation)

## Auteur
Sokhna Aicha KA - L2 GLSI - ESP/UCAD

## Cours
Integration de Modeles IA - Dr. El Hadji Bassirou TOURE
