# ===============================
# Projet Informatique
# Structure du programme principal
# ===============================

# Import des modules écrits par les sous-groupes
import plot_donnees_new
import interface_graphique


def main():
    print("=== Début du programme ===")
    
    # Étape 1 – Préparation ou lecture de données et Étape 2 – Traitement ou analyse
    print("\n--- Étape 1 : Données et analyse ")
    data= plot_donnees_new.renvoie_ttes_sufaces_pour_annees_en_tableau ()
    data= plot_donnees_new.fonction_totale ()
    data=plot_donnees_new.creation_nom_fichier ()
    data= plot_donnees_new.surface_glaciers()
    data=plot_donnees_new.cerveau_de_l_operation2 ()
    data=plot_donnees_new.surface_pour_une_annee ()
    data=plot_donnees_new.extraire_S_par_glacier()
    data=plot_donnees_new.tracer_graphique()
    data=plot_donnees_new.cerveau_number3 ()
    data=plot_donnees_new.surface_pour_une_anne ()
    
    
    
    # Étape 3 – Résultats ou affichage final
    print("\n--- Étape 3 : Résultats ou sortie ---")
    code_interface_graphique.main(result)
    
    print("\n=== Fin du programme ===")

if __name__ == "__main__":
    main()


