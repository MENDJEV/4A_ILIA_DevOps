from datetime import datetime,timedelta
import pytest 

def typeT():
    T = []
    return T

def evenement(T, t, n):
    return (T, t, n)




# Exemple de fonction qui génère une liste d'événements
def liste_evenements():
    calendrier1= []

    # Créons 3 événements pour l'exemple
    for i in range(3):
        T = i                  # entier
        t = datetime.now() + timedelta(hours=i)  # date/heure
        n = f"Événement {i}"   # chaîne de caractères

        calendrier1.append((T, t, n))

    return calendrier1

def test_liste_evenements():
    result = liste_evenements()

    # Vérifier que le résultat est une liste
    assert isinstance(result, list), "liste_evenements() doit retourner une liste"

    # Vérifier que chaque élément de la liste est un tuple
    for ev in result:
        assert isinstance(ev, tuple), "Chaque élément doit être un tuple"
        assert len(ev) == 3, "Chaque tuple doit contenir exactement 3 éléments"
        
        T, t, n = ev
        
        # Vérifier les types de chaque élément
        assert isinstance(T, int), "Le premier élément doit être un entier"
        assert isinstance(t, datetime), "Le deuxième élément doit être un datetime"
        assert isinstance(n, str), "Le troisième élément doit être une chaîne de caractères"



def trier_evenements_chronologiquement(evenements):
    """
    Trie une liste d'événements par date/heure croissante.
    
    Paramètres :
        evenements (list of tuples): liste de tuples (T, t, n)
    
    Retourne :
        list of tuples: liste triée par t (datetime)
    """
    # Utilisation de sorted avec key pour trier par le deuxième élément du tuple
    return sorted(evenements, key=lambda ev: ev[1])


def premier_evenement(evenements):
    """
    Retourne le nom du premier événement dans la liste.
    
    Paramètres :
        evenements (list of tuples): liste de tuples (T, t, n)
    
    Retourne :
        str: nom du premier événement
    """
    if not evenements:
        return None  # retourne None si la liste est vide
    return evenements[0][2]  # le nom du premier événement


def deuxieme_evenement(evenements):
    """
    Retourne le nom du premier événement dans la liste.
    
    Paramètres :
        evenements (list of tuples): liste de tuples (T, t, n)
    
    Retourne :
        str: nom du premier événement
    """
    if not evenements or len(evenements)<=1:
        return None  # retourne None si la liste est vide
    return evenements[1][2]  # le nom du premier événement

