import pandas as pd
import matplotlib.pyplot as plt

#Reading of Excel File
df = pd.read_excel(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\proccesed\revenue_per_city_editted.xlsx") #reads excel file "revenue_per_city"
df = df.sort_values("total_value", ascending = False) #sorts total_revenue

#Plt Edits
plt.figure() #creates an empty chart
plt.bar(df["city"], df["total_value"]) #creates a bar chart with X -> "city" and y -> "total_revenue"
plt.title("Revenue per City")
plt.xlabel("City") #gives a title to X
plt.ylabel("Total Revenue (€)") #gives a title to Y
plt.xticks(rotation=45) #rotates names of cities so that they do not stick to each other
plt.tight_layout() #fixes blank spaces

#Creating of chart
plt.savefig("revenue_per_city_chart.png")
plt.close()

#Inserting chart in excel
from openpyxl import load_workbook #lets us edit excel files
from openpyxl.drawing.image import Image #lets us insert images in excel
wb = load_workbook(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\proccesed\revenue_per_city_editted.xlsx") #opens excel file

#Editting
ws = wb.active #picks the first sheet
img = Image("revenue_per_city_chart.png") #loads image of chart
ws.add_image(img, "E2") #puts image in cell "E2"
wb.save(r"C:\Users\dimit\Downloads\iknowhow-data-pipeline\data\proccesed\revenue_per_city_editted.xlsx")


