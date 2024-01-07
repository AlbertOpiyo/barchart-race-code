import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.animation import FuncAnimation, PillowWriter

# import the data
df=pd.read_csv("https://raw.githubusercontent.com/datagy/mediumdata/master/populations.csv")

df["Age Group"]=df["Age Group"].fillna(method='ffill')

df["Males"]=df["Males"].str.replace(",","").astype("int")
df["Females"]=df["Females"].str.replace(",","").astype("int")
df["Females"]=df["Females"] *-1



fig,ax=plt.subplots(figsize=(10,6))

def animate(year):
  ax.clear()
  filtered_df=df[df['Year']==year]

  males= plt.barh(y=filtered_df["Age Group"], width=filtered_df["Males"])
  females=plt.barh(y=filtered_df["Age Group"], width=filtered_df["Females"])


  ax.set_xlim(-2000000,2000000)
  ax.bar_label(males, padding=3, labels=[f'{round(value,-3):,}' for value in filtered_df["Males"]])
  ax.bar_label(females, padding=3, labels=[f'{-1 * round(value,-3):,}' for value in filtered_df["Females"]])

  for edge in ["top","right","bottom","left"]:
    ax.spines[edge].set_visible(False)

  ax.tick_params(left=False)
  ax.get_xaxis().set_visible(False)

  # Create legend handles
  male_patch = mpatches.Patch(color='blue', label='Males')
  female_patch = mpatches.Patch(color='orange', label='Females')

  ax.legend(handles=[male_patch, female_patch])
  # ax.legend(['males','females'], ['Males','Females'])

  ax.set_title(f'Population of Canada in {year}',size=18, weight='bold')

  
  
animation=FuncAnimation(fig,animate,frames=range(df['Year'].min(),df['Year'].max()+1))

plt.show()