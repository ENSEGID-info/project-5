<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 18:40:19 2025

@author: PIETREQUIN
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



#a= "E:\Info projet 5\inventory_sgi1973\SGI_1973.shp"

def renvoie_ttes_sufaces_pour_annees_en_tablea ():
    """
   desciption fonction : Collecte et retourne l’ensemble des surfaces glaciaires
   calculées pour une liste d’années prédéfinies.
   Comment ? 1) parcourt les années disponibles, 
    2) calcule la surface totale pour chacune, 3) renvoie un tableau des années
    et un tableau des surfaces associées. 

    Returns
    -------
    a : list of int 
        liste des annees 
    Y : list 
        liste des surfaces des glaciers.

    """
     a = [1931,1973,2010,2016]
     Y = []
     for i in range (len(a)):
         Y=Y+[fonction_totale(a[i])]
         print (Y)
     return (a,Y)



def fonction_totale (annee):
    """
    description fonction : Point d’entrée du calcul de surface pour une année donnée.
   Comment ? 1) génère le chemin du shapefile correspondant, 2) lance le calcul
    de surface totale, 3) renvoie la valeur obtenue en km².

    Parameters
    ----------
    annee : nb 
     le nombre rentré par l utilisateur    

    Returns
    -------
list des surfaces des glaciers  

    """
     x = creation_nom_fichier(annee)
     print (x)
     return(surface_glaciers(x))



def creation_nom_fichier (annee) :
    """
    Construit dynamiquement le chemin complet vers le fichier SGI correspondant à l’année fournie.

    Parameters
    ----------
    annee : nb
       le nombre rentré par l utilisateur 

    Returns
    -------
    a : list
        liste des annees

    """
     "programme\\inventory_sgi"+str(annee)+"\\SGI_"+ str(annee) + ".shp"
     return (a)



def surface_glaciers(nom_du_fichier):
    """
    Calcule la surface totale des glaciers à partir d’un shapefile en vérifiant
    la projection, en calculant l’aire de chaque polygone, puis en enregistrant
    un shapefile avec les surfaces.
    Comment ? 1) charge le shaperfile, 2) vérifie si le CRS est géographique, 
    3) calcule les surfaces et surface totale, 4) enregistre dans un nouveau 
    shaperfile, 5) retourne la surface totale

    Parameters
    ----------
    nom_du_fichier : str
        nom du fichier shapefile du glacier 

    Returns
    -------
    surface_totale_km2 : float 
        surface totale des glaviers en km 

    """
     path = nom_du_fichier
     gdf = gpd.read_file(path)

#print("Shapefile chargé !")
     print("Nombre d’objets :", len(gdf))

     if gdf.crs is None:
         raise ValueError("Le shapefile n’a pas de système de coordonnées (.prj manquant)")

     if gdf.crs.is_geographic:
         gdf = gdf.to_crs(epsg=3857)

     gdf["surface_m2"] = gdf.geometry.area
     gdf["surface_km2"] = gdf["surface_m2"] / 1e6

     surface_totale_km2 = gdf["surface_km2"].sum()

     print("Surface glaciaire totale :", surface_totale_km2, "km²")
     gdf.to_file("SGI_1973_with_area.shp")
#print("Fichier sauvegardé : SGI_1973_with_area.shp")

     return (surface_totale_km2)




def cerveau_de_l_operation2 ():
    """
    cription fonction : Fonction principale qui coordonne l’ensemble du processus
    Comment ? 1) collecte des surfaces pour toutes les années, 2) génération
    du graphique d’évolution, 3) lancement des visualisations supplémentaires

    Returns
    -------

    """

     a,liste_surface = renvoie_ttes_sufaces_pour_annees_en_tableau ()
     # surface_annee_voulue = surface_pour_une_annee(a, liste_surface)
     # print (surface_annee_voulue)
     plt.plot(a,liste_surface)
     plt.show()

     plot_glacier_surfaces(a, liste_surface)





def surface_pour_une_annee (liste_annees,liste_surface):
    """
   description fonction : Permet à l’utilisateur d’obtenir la surface d’une
   année précise.
   Comment ? Après saisie d’une année, la fonction recherche dans la liste et 
   retourne la surface correspondante

    Parameters
    ----------
    liste_annees : list 
        liste des annees 
    liste_surface : list 
        liste des surfaces des glaciers

    Returns
    -------
    list 
        DESCRIPTION.

    """
     a= input ('année:')
     for i in range (len(liste_annees)):
         if liste_annees[i]==int(a):
             return (liste_surface[i])
"
>>>>>>> origin/plot





<<<<<<< HEAD
def interface():
     """
     Returns
     -------
     None.
    
=======
def plot_glacier_surfaces(years, surfaces):
    """
description fonction : Permet de créer une interface graphique Tkinter.
Comment ? 1) définit la fonction qui affiche la surface selon l'année 
    sélectionnée, 2) crée un graphique Matplotlib (année vs surface), 
    3) intègre le graphique dans une interface Tkinter, 4) crée un menu 
    déroulant pour sélectionner une année, 5) affiche la surface correspondante
    lorsque l’utilisateur choisit une année   

    Parameters
    ----------
    years : nb 
      les années 
    surfaces : nb 
        les surfaces en km2

    Returns
    -------

    """
>>>>>>> origin/plot

     when called:
     creates a window with the plot of the surfaces over time and  you can select

     """
    

          
     # --- Create main Tkinter window ---
     root = tk.Tk()
     root.title("Masse annuelle des glacier en fonction du temps")
     
     # list of the glaciers is created here
     glaciers = ["Silvrettagletscher"
     ,"Glatscher da Plattas / Glatscher da Medel"
     ,"Vorabgletscher"
     ,"Glatschiu dil Segnas"
     ,"Pizolgletscher"
     ,"Limmerngletscher"
     ,"Plattalva / Griessfirn"
     ,"Claridenfirn"
     ,"Schwarzwasserfirn"
     ,"St. Annafirn"
     ,"Tiefengletscher"
     ,"Oberaargletscher"
     ,"Glacier de la Plaine Morte"
     ,"Glacier du Sex Rouge"
     ,"Glacier de Tsanfleuron"
     ,"Grosser Aletschgletscher"
     ,"Rhonegletscher"
     ,"Griesgletscher"
     ,"Hohsaasgletscher"
     ,"Ofentalgletscher"
     ,"Schwarzberggletscher"
     ,"Allalingletscher"
     ,"Hohlaubgletscher"
     ,"Chessjengletscher"
     ,"Chessjengletscher NW"
     ,"Alphubelgletscher N"
     ,"Findelgletscher"
     ,"Adlergletscher"
     ,"Mont Collon"
     ,"Glacier de Tortin"
     ,"Vadrec del Forno"
     ,"Vadrec da l'Albigna"
     ,"Vadret Pers,Vadret dal Corvatsch"]
   
     

     # --- Function to handle the selection of the glaciers ---
     def select_glacier(event=None):
         # gets the name of the glacier by selection in the interface
         selected_glacier = glacier_select.get()
         
         # gets the needed data for the selected glacier 
         data = extraire_S_par_glacier("H:\massbalance_observation.csv", selected_glacier)
         years,surface = creation_liste(data,selected_glacier)
         
         # Convert years to strings (for the dropdown)
         year_strings = [str(y) for y in years]
         

         
         def show_surface(event=None):
             selected_year = int(year_select.get())
             index = years.index(selected_year)
             masse_value = surface[index]
             result_label.config(text=f"Masse annuelle du glacier voulu : {masse_value}")


         fig = plot_glacier_masse(years, surface)
       
         # --- Embed matplotlib figure into Tkinter ---
         canvas = FigureCanvasTkAgg(fig, master=root)
         canvas.draw()
         canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

         # --- Frame for selection controls ---
         control_frame = ttk.Frame(root)
         control_frame.pack(pady=10)

         # Dropdown for year selection
         ttk.Label(control_frame, text="Select a year:").grid(row=0, column=0, padx=5)

         year_select = ttk.Combobox(control_frame, values=year_strings, state="readonly")
         year_select.grid(row=0, column=1, padx=5)
         year_select.bind("<<ComboboxSelected>>", show_surface)

         # Label to show result
         result_label = ttk.Label(control_frame, text="Mass: -")
         result_label.grid(row=1, column=0, columnspan=2, pady=5)

         
         
         

     # --- Frame for selection controls ---
     control_frame_G = ttk.Frame(root)
     control_frame_G.pack(pady=10)
   

     # Dropdown for year selection
     ttk.Label(control_frame_G, text="Select a Glacier:").grid(row=0, column=0, padx=5)

     glacier_select = ttk.Combobox(control_frame_G, values=glaciers, state="readonly")
     glacier_select .grid(row=0, column=1, padx=5)
     glacier_select .bind("<<ComboboxSelected>>", select_glacier)
     
     
     
     # recup année et masse du glacier choisi
     
     
     
     
     
  
    # --- Start the GUI event loop ---
     root.mainloop()    

   
   
       
       
def plot_glacier_masse(years, surfaces):

   

     # --- Create Matplotlib Figure ---
     fig, ax = plt.subplots(figsize=(6, 4))
     ax.plot(years, surfaces, marker='o', linestyle='-', color='blue')
     ax.set_title("Glacier Mass Change")
     ax.set_xlabel("Year")
     ax.set_ylabel("Mass")
     ax.grid(True)
     
<<<<<<< HEAD
     return fig



interface()
=======
    
cerveau_de_l_operation2()
>>>>>>> origin/plot
''

