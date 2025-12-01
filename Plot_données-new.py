import geopandas as gpd
import matplotlib.pyplot as plt



#a= "E:\Info projet 5\inventory_sgi1973\SGI_1973.shp"

def renvoie_ttes_sufaces_pour_annees_en_tableau ():
    a = [1931,1973,2010,2016]
    Y = []
    for i in range (len(a)):
        Y=Y+[fonction_totale(a[i])]
        print (Y)
    return (a,Y)



def fonction_totale (annee):
    x = creation_nom_fichier(annee)
    print (x)
    return(surface_glaciers(x))





def creation_nom_fichier (annee) :
    a = "H:\Info projet 5\\inventory_sgi"+str(annee)+"\\SGI_"+ str(annee) + ".shp"
    return (a)




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




def cerveau_de_l_operation2 ():
    a,liste_surface = renvoie_ttes_sufaces_pour_annees_en_tableau ()
    surface_annee_voulue = surface_pour_une_annee(a, liste_surface)
    print (surface_annee_voulue)
    plt.plot(a,liste_surface)
    plt.show()
   
   
def surface_pour_une_annee (liste_annees,liste_surface):
    a= input ('année:')
    for i in range (len(liste_annees)):
        if liste_annees[i]==int(a):
            return (liste_surface[i])
