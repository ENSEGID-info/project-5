
import geopandas as gpd
import matplotlib.pyplot as plt



#a= "E:\Info projet 5\inventory_sgi1973\SGI_1973.shp"
#EXTRACTION SURFACES

def creation_nom_fichier (annee) :
    a = "H:\Info projet 5\\inventory_sgi"+str(annee)+"\\SGI_"+ str(annee) + ".shp"
    return (a)
'''n constitue le nom du fichier à partir des dossiers contenant nos données'''
#str : initialment les années sont des int (entiers, chiffres) donc pour pouvoir les ajouter au nom du fichier on les convertie en str (string = chaine de caractère)
#ce qui permettra d'ouvrir les différents fichiers en modifiant juste l'année pour pouvoir récupérer les données des différentes années facilement

def surface_glaciers(nom_du_fichier):

# 1) Charger le shapefile
    path = nom_du_fichier
    gdf = gpd.read_file(path)

#print("Shapefile chargé !")
    print("Nombre d’objets :", len(gdf))
#print("Type de géométrie :", gdf.geometry.geom_type.unique())
#print("Projection d’origine :", gdf.crs)

# 2) Reprojection si nécessaire
    if gdf.crs is None:
        raise ValueError("Le shapefile n’a pas de système de coordonnées (.prj manquant)")

    if gdf.crs.is_geographic:
    #print("Projection en degrés détectée → reprojection en EPSG:3857")
        gdf = gdf.to_crs(epsg=3857)

# 3) Calculer les surfaces
    gdf["surface_m2"] = gdf.geometry.area
    gdf["surface_km2"] = gdf["surface_m2"] / 1e6

# 4) Calculer la somme totale en km²
    surface_totale_km2 = gdf["surface_km2"].sum()

# 5) Afficher le résultat
    print("Surface glaciaire totale :", surface_totale_km2, "km²")

# 6) Export éventuel
    gdf.to_file("SGI_1973_with_area.shp")
#print("Fichier sauvegardé : SGI_1973_with_area.shp")

    return (surface_totale_km2)



#graphique masses

#EXTRACTION

def extraire_S_par_glacier(fichier_csv, glacier_recherche):
    """
    Lit un fichier CSV contenant : glacier, année, S
    et renvoie une liste (année, S) pour le glacier souhaité.
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






