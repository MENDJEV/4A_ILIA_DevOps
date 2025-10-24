import pytest
from datetime import datetime


from calendrier import deuxieme_evenement




def test_deuxieme_evenement():
    evenements = [
        (2, datetime(2025, 10, 24, 9, 0), "Petit déjeuner"),
        (3, datetime(2025, 10, 24, 12, 0), "Déjeuner"),
        (1, datetime(2025, 10, 24, 15, 0), "Réunion")
    ]

    # Appel de la fonction
    nom = deuxieme_evenement(evenements)

    # Vérifier que c'est une chaîne
    assert isinstance(nom, str), "Le nom du deuxieme événement doit être une chaîne"

    # Vérifier que c'est bien le nom du premier élément
    assert nom == "Déjeuner", "Le nom du premier événement est incorrect"

    # Cas liste vide
    assert deuxieme_evenement([]) is None, "Si la liste est vide, la fonction doit retourner None"
