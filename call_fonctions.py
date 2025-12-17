# ===============================
# Projet Informatique
# Structure du programme principal
# ===============================

# Import des modules écrits par les sous-groupes
import lecture_des_données
import plot_donnees_new
import interface_graphique



def main():
    print("=== Début du programme ===")
   
    # Étape 1 – Préparation ou lecture de données
    print("\n---Etape1: Lecture des donées---")
    data=lecture_des_données.creation_nom_fichier()
    data=lecture_des_données.surface_glaciers()
    data=lecture_des_données.extraire_S_par_glacier()
   
   
    #Étape 2 – Traitement ou analyse
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
    data=interface_graphique.renvoie_ttes_sufaces_pour_annees_en_tablea()
    data=interface_graphique.fonction_totale()
    data=interface_graphique.creation_nom_fichier()
    data=interface_graphique.surface_glaciers()
    data=interface_graphique.cerveau_de_l_operation2()
    data=interface_graphique.surface_pour_une_annee()
    data=interface_graphique.interface()
    data=interface_graphique.select_glacier()
    data=interface_graphique.show_surface()
    data=interface_graphique.plot_glacier_masse()
    data=interface_graphique.show_surface()

   
   
   
    print("\n=== Fin du programme ===")

if __name__ == "__main__":
    main()




