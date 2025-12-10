




def interface():
     """
     Returns
     -------
     None.
    

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
     
     return fig



interface()

