# notebooks/test_temperature.py
# Exercice 2 : Tester l'effet de la temperature

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """Tu es un assistant medical senegalais.
Tu recois un diagnostic et des donnees patient.
Explique le resultat en francais simple,
comme un medecin parlerait a son patient.
Sois rassurant mais recommande toujours
une consultation medicale.
Maximum 3 phrases.
Ne fais JAMAIS de diagnostic toi-meme."""

USER_PROMPT = """Patient : Femme, 28 ans, region Dakar
Symptomes : temperature 39.5, toux, fatigue, maux de tete
Diagnostic du modele : paludisme (probabilite 72%)
Explique ce resultat au patient."""

# Tester 3 temperatures, chacune avec 2 appels
# pour observer la variabilite
temperatures = [0.0, 0.5, 1.0]

for temp in temperatures:
    print("=" * 60)
    print(f"TEMPERATURE = {temp}")
    print("=" * 60)

    for essai in [1, 2]:
        print(f"\n--- Essai {essai} ---")
        r = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT}
            ],
            max_tokens=200,
            temperature=temp
        )
        print(r.choices[0].message.content)
    print()