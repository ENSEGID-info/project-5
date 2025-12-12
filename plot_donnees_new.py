import geopandas as gpd
import matplotlib.pyplot as plt



#a= "E:\Info projet 5\inventory_sgi1973\SGI_1973.shp"

def renvoie_ttes_sufaces_pour_annees_en_tableau ():
    """
   desciption fonction : Crée une liste des années et une liste des surfaces correspondantes.
   Comment ?    1) crée la liste des années pour lesquelles on a des données,
                2) crée une liste vide, 
                3) ajoute à la liste pour chaque année la surface correspondante
                en faisant appelle à la fonction_totale

    Returns
    -------
    a : list of int 
        liste des annees 
    Y : list of int
        liste des surfaces des glaciers

    """
    a = [1931,1973,2010,2016]
    Y = []
    for i in range (len(a)):
        Y=Y+[fonction_totale(a[i])]
        print (Y)
    return (a,Y)



def fonction_totale (annee):
    """
   desciption fonction : à partir d'une année, elle renvoie la surface du glacier correspondante
   Comment ?    1) crée un nom de fichier en faisant appelle à la fonction creation_nom_fichier
                2) renvoie la surface correspondante

    Returns
    -------
    surface_glaciers(x) : int surface glacier

    """
    x = creation_nom_fichier(annee)
    print (x)
    return(surface_glaciers(x))





def creation_nom_fichier (annee) :
    """
   desciption fonction : à partir d'une année, elle crée le nom de fichier CAD le chemin d'accès
   Comment ?    1) crée un nom de fichier en faisant une cocaténation de str

    Returns
    -------
    a = chemin d'accès au fichier'

    """
    a = "H:\Info projet 5\\inventory_sgi"+str(annee)+"\\SGI_"+ str(annee) + ".shp"
    return (a)




def cerveau_de_l_operation2 ():
    """
   desciption fonction : execute la totalité des fonctions et crée un plot
   Comment ?    1) récupère la liste des années et des surfaces
                2) récupère la surface pour une année voulue
                3) crée un plot
                4) affiche le plot

    Returns
    -------
    le plot

    """
    
    a,liste_surface = renvoie_ttes_sufaces_pour_annees_en_tableau ()
    surface_annee_voulue = surface_pour_une_annee(a, liste_surface)
    print (surface_annee_voulue)
    plt.plot(a,liste_surface)
    plt.show()
   
   
def surface_pour_une_annee (liste_annees,liste_surface):
    """
   desciption fonction : à partir de la liste des années et de celle des surfaces
   elle renvoie la valeur de la surface correspondante à l'année souhaitée'
   Comment ?    1) demande une année (input)
                2) parcours la liste des années pour recupérer l'indice de l'année demandée
                3) return la surface correspondante

    Returns
    -------
    liste_surface[i] = la surface correspondante à l'année souhaitée

    """
    a= input ('année:')
    for i in range (len(liste_annees)):
        if liste_annees[i]==int(a):
            return (liste_surface[i])
        
#graphique masses



# ANALYSE DES DONNEES

   
def tracer_graphique(data,g):
        
    
    """
    
    """
    """
   desciption fonction : à partir de la liste de tuple des années associées 
   aux surfaces correspondantes (année, S), exemple : [(1900, 3.0), (1901, 4.0), (1905, 88.0)]
   elle crée un plot montrant l'évolution du glacier

   Comment ?    1) crée 2 listes vides
                2) parcours la liste récupère les valeurs du tupple
                3) ajoute ces valeurs aux listes
                4) crée le plot et ses légendes

    Returns
    -------
    le plot

    """

    # Séparer années et valeurs S
    X,Y = [],[]
    for i in range (len(data)):
        annees,m = data[i]
        X=X+[annees]
        Y=Y+[m]

    # Création du graphique
    plt.figure()
    plt.plot(X, Y)
    plt.xlabel("Année")
    plt.ylabel("masse")
    plt.title("Évolution de "+str(g)+"en fonction des années")
    plt.grid(True)
    plt.show()

   
def surface_pour_une_anne (tupple):
    """
   desciption fonction : à partir d'une liste de tuple renvoie la surface correspondante
   à une année souhaité
   Comment ?    1) crée 2 int
                2) demande une année voulue (input)
                3) pacours la liste de tuple renvoie la surface pour l'année souhaitée 
                (tranformée en int)
    Returns
    -------
    la surface pour une année souhaitée

    """
    
    a,m=0,0
    av = input ('année:')
    for i in range (len(tupple)):
        a,m= tupple[i]
        if a==int(av):
            print (m)
            return (m)    
   


def cerveau_number3 (fichier_csv):
    """
   desciption fonction : à partir d'un fichier csv elle lance toute les fonctions pour
   crée un plot et renvoyer la surface pour une année souhaitée
   Comment ?    1) demande le nom du glacier voulu
                2) extrait les données pour le glacier demandé à l'aide de la 
                fonction extraire_S_par_glacier
                3) trace le plot pour le glacier demandé grace à la fonction tracer_graphique
                4) récupère la surface pour l'année souhaitée'
    
    Returns
    -------
    le plot, la surface pour une année souhaitée

    """
    g= input('nom du glacier voulu : ')
    tupple = extraire_S_par_glacier(fichier_csv, g)
    tracer_graphique(tupple,g)
    surface_pour_une_anne (tupple)
   
   

   
   
###
#LISTE DE TS LES GLACIERS POSSIBLES
 
#Silvrettagletscher,
#Glatscher da Plattas / Glatscher da Medel,
#Vorabgletscher,
#Glatschiu dil Segnas,
#Pizolgletscher,
#Limmerngletscher
#Plattalva / Griessfirn
#Claridenfirn
#Schwarzwasserfirn
#St. Annafirn
#Tiefengletscher
#Oberaargletscher
#Glacier de la Plaine Morte
#Glacier du Sex Rouge
#Glacier de Tsanfleuron
#Grosser Aletschgletscher
#Rhonegletscher
#Griesgletscher
#Hohsaasgletscher
#Ofentalgletscher
#Schwarzberggletscher
#Allalingletscher
#Hohlaubgletscher
#Chessjengletscher
#Chessjengletscher NW
#Alphubelgletscher N
#Findelgletscher
#Adlergletscher
#Mont Collon
#Glacier de Tortin
#Vadrec del Forno
#Vadrec da l'Albigna
#Vadret Pers
#Vadret dal Corvatsch

