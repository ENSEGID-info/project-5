
import geopandas as gpd
import matplotlib.pyplot as plt


#EXTRACTION DONNEES SURFACES

# a = "E:\Info projet 5\inventory_sgi1973\SGI_1973.shp

def creation_nom_fichier (annee) :
    """
    
    On crée une fonction qui nous donne le chemin d'accées au fichier pour 
    l'année désirée.
   
    Parameters
    ----------
    annee : int
        on converti les années en str pour pouvoir les ajouter nom du fichier.

    Returns
    -------
    a : str
        a est le nom du fichier à partir des dossiers contenant nos données.

    """
    a = "H:\Info projet 5\\inventory_sgi" + str(annee)+"\\SGI_"+ str(annee) + ".shp"
    return (a)


def surface_glaciers(nom_du_fichier):
    """
    On crée une fonction qui récupère les données (shapfile) pour l'année voulu 
    et on calcule la somme des surfaces totales des glaciers pour l'année en 
    question.

    Parameters
    ----------
    nom_du_fichier : str
        

    Returns
    -------
    surface_totale_km2 : int
        Surface totale des glaciers en km2

    """

#1) Charger le shapefile
    path = nom_du_fichier
    gdf = gpd.read_file(path)

    print("Nombre d’objets :", len(gdf))

#2) Reprojection si nécessaire
    if gdf.crs is None:
        raise ValueError("Le shapefile n’a pas de système de coordonnées (.prj manquant)")

    if gdf.crs.is_geographic:
    #print("Projection en degrés détectée → reprojection en EPSG:3857")
        gdf = gdf.to_crs(epsg=3857)

#3) Calculer les surfaces
    gdf["surface_m2"] = gdf.geometry.area
    gdf["surface_km2"] = gdf["surface_m2"] / 1e6

#4) Calculer la somme totale en km²
    surface_totale_km2 = gdf["surface_km2"].sum()

#5) Afficher le résultat
    print("Surface glaciaire totale :", surface_totale_km2, "km²")

# 6) Export éventuel
    gdf.to_file("SGI_1973_with_area.shp")
#print("Fichier sauvegardé : SGI_1973_with_area.shp")

    return (surface_totale_km2)




#EXTRACTION DES DONNEES DE MASSE

def extraire_S_par_glacier(fichier_csv, glacier_recherche):
   """
    Lit un fichier CSV contenant : glacier, année, S
    et renvoie une liste (année, S) pour le glacier souhaité.

    Parameters
    ----------
    fichier_csv : str
        Chemin d'accès au fichier csv
        
    glacier_recherche : str
        Glacier choisi

    Returns
    -------
    resultats : liste de uplets en int
        Renvoie l'année associée à la masse du glacier recherche

    """
    
    resultats = []

    with open(fichier_csv, newline='', encoding='utf-8') as f:
        lecteur = csv.reader(f)
        #liste_annee=[]
        #liste_surface=[]
        for ligne in lecteur:
            if len(ligne) < 8:
                continue  # ignorer lignes incomplètes

            glacier,date_start, winter_mass_balance = ligne[0], ligne[2], ligne[5]
            annee = date_start.split("-")[0]
            #liste_annee=liste_annee+[annee]
            if glacier == glacier_recherche:
                try:
                    resultats.append((int(annee), int(winter_mass_balance)))
                    #liste_surface.append(float(annual_mass_balance))
                except ValueError:
                    # ignorer les lignes mal formatées
                    continue
    # Trier les résultats par année
    resultats.sort(key=lambda x: x[0])
    #création evolution glacier
   # plt.plot (liste_annee,liste_surface)
    #plt.show()
    return (resultats)






