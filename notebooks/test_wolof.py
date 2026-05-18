# notebooks/test_wolof.py
# Exercice 1 : Tester le prompt engineering en wolof

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# System prompt mixte francais-wolof
SYSTEM_PROMPT_WOLOF = """Tu es un assistant medical senegalais.
Tu recois un diagnostic et des donnees patient.
Explique le resultat en francais simple, en y melangeant
quelques mots ou expressions courantes en wolof
(comme nanga def pour bonjour, jamm rekk pour ca va bien,
sibbiru pour paludisme, tangor pour fievre,
feebar pour maladie, lopitaan pour hopital,
moytu pour fais attention, noflaay pour repos).
Garde un ton chaleureux et respectueux.
Maximum 4 phrases.
Termine toujours par une recommandation de consulter."""

# Test 1 : Paludisme
print("=" * 60)
print("TEST 1 : Paludisme (femme, 28 ans, Dakar)")
print("=" * 60)

r1 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT_WOLOF},
        {"role": "user",
         "content": """Patient : Femme, 28 ans, region Dakar
         Symptomes : temperature 39.5, toux, fatigue, maux de tete
         Diagnostic du modele : paludisme (probabilite 72%)
         Explique ce resultat au patient."""}
    ],
    max_tokens=250,
    temperature=0.4
)
print(r1.choices[0].message.content)

# Test 2 : Grippe
print("\n" + "=" * 60)
print("TEST 2 : Grippe (homme, 35 ans, Thies)")
print("=" * 60)

r2 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT_WOLOF},
        {"role": "user",
         "content": """Patient : Homme, 35 ans, region Thies
         Symptomes : temperature 38.2, toux, fatigue
         Diagnostic du modele : grippe (probabilite 65%)
         Explique ce resultat au patient."""}
    ],
    max_tokens=250,
    temperature=0.4
)
print(r2.choices[0].message.content)

# Test 3 : Patient sain
print("\n" + "=" * 60)
print("TEST 3 : Patient sain (femme, 22 ans, Saint-Louis)")
print("=" * 60)

r3 = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT_WOLOF},
        {"role": "user",
         "content": """Patient : Femme, 22 ans, region Saint-Louis
         Symptomes : temperature 37.0, pas de symptomes
         Diagnostic du modele : sain (probabilite 88%)
         Explique ce resultat au patient."""}
    ],
    max_tokens=250,
    temperature=0.4
)
print(r3.choices[0].message.content)