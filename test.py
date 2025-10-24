import pytest
from datetime import datetime
from calendrier import typeT, evenement,liste_evenements,trier_evenements_chronologiquement,premier_evenement  # ← importer les fonctions

# Test 1 : vérifier que typeT retourne une liste
def Liste_evenement():
    result = typeT()
    assert isinstance(result, list), "typeT() doit retourner une liste"

# Test 2 : vérifier le tuple de evenement
def test_evenement_types():
    T = 5               # entier
    t = datetime.now()  # date/heure
    n = "exemple"       # chaîne de caractères

    result = evenement(T, t, n)
    
    # Vérifier que c'est un tuple
    assert isinstance(result, tuple), "evenement() doit retourner un tuple"
    
    # Vérifier les types des éléments
    assert isinstance(result[0], int), "Le premier élément doit être un entier"
    assert isinstance(result[1], datetime), "Le deuxième élément doit être un datetime"
    assert isinstance(result[2], str), "Le troisième élément doit être une chaîne"

def test_trier_evenements_chronologiquement():
    evenements = [
        (1, datetime(2025, 10, 24, 15, 0), "Réunion"),
        (2, datetime(2025, 10, 24, 9, 0), "Petit déjeuner"),
        (3, datetime(2025, 10, 24, 12, 0), "Déjeuner")
    ]

    # Appel de la fonction
    result = trier_evenements_chronologiquement(evenements)

    # Vérifier que le résultat est une liste
    assert isinstance(result, list), "Le résultat doit être une liste"

    # Vérifier que chaque élément est un tuple de 3 éléments
    for ev in result:
        assert isinstance(ev, tuple)
        assert len(ev) == 3

    # Vérifier que la liste est triée par date croissante
    dates = [ev[1] for ev in result]
    assert dates == sorted(dates), "Les événements doivent être triés par date croissante"


def test_premier_evenement():
    evenements = [
        (2, datetime(2025, 10, 24, 9, 0), "Petit déjeuner"),
        (3, datetime(2025, 10, 24, 12, 0), "Déjeuner"),
        (1, datetime(2025, 10, 24, 15, 0), "Réunion")
    ]

    # Appel de la fonction
    nom = premier_evenement(evenements)

    # Vérifier que c'est une chaîne
    assert isinstance(nom, str), "Le nom du premier événement doit être une chaîne"

    # Vérifier que c'est bien le nom du premier élément
    assert nom == "Petit déjeuner", "Le nom du premier événement est incorrect"

    # Cas liste vide
    assert premier_evenement([]) is None, "Si la liste est vide, la fonction doit retourner None"
