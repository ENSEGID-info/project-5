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
        
#graphique masses



# ANALYSE DES DONNEES

   
def tracer_graphique(data,g):
    """
    data doit être une liste de tuples (année, S)
    Exemple : [(1900, 3.0), (1901, 4.0), (1905, 88.0)]
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

   
def cerveau_number3 (fichier_csv):
    g= input('nom du glacier voulu : ')
    tupple = extraire_S_par_glacier(fichier_csv, g)
    print (tupple)
    tracer_graphique(tupple,g)
    surface_pour_une_anne (tupple)
   
   
def surface_pour_une_anne (tupple):
    a,m=0,0
    av = input ('année:')
    for i in range (len(tupple)):
        a,m= tupple[i]
        if a==int(av):
            print (m)
            return (m)    
   
   
   
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

