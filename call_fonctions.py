# ===============================
# Projet Informatique
# Structure du programme principal
# ===============================

# Import des modules écrits par les sous-groupes
import plot_donnees_new
import code_interface_graphique


def main():
    print("=== Début du programme ===")
    
    # Étape 1 – Préparation ou lecture de données et Étape 2 – Traitement ou analyse
    print("\n--- Étape 1 : Données et analyse ")
    data = plot_donnees_new.main()
    
    
    
    
    # Étape 3 – Résultats ou affichage final
    print("\n--- Étape 3 : Résultats ou sortie ---")
    code_interface_graphique.main(result)
    
    print("\n=== Fin du programme ===")

if __name__ == "__main__":
    main()


