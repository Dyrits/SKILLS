# ORD-88 : Stocker les totaux de commande en centimes entiers

Les factures de la boutique Hollis Mill affichent des totaux faux d'un centime sur certaines commandes (par exemple 0,1 + 0,2 donne 0,30000000000000004 dans l'export). La cause est la colonne `total`, qui stocke un nombre flottant.

Objectif : stocker le total de commande en nombre entier de centimes, convertir les lignes existantes une seule fois, et cesser d'utiliser la colonne flottante.

Hors périmètre : conversion de devise, mise en page de la facture.
