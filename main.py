#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <YII KAH NUM >
#Group Name: <NAME>
#Class: <PN2004L>
#Date: <9/2/2021>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
import numpy as np
#import matplotlib.pyplot as pit
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class Analyse():
  def __init__(self):
    
    df = pd.read_csv('MonthlyVisitors.csv')
    printcountry()

def sortTopCountries(ha):
  df = pd.read_csv('MonthlyVisitors.csv')
  TotalVis()
  
def TotalVis():
  df = pd.read_csv('MonthlyVisitors.csv')
  BN= df[' Brunei Darussalam '][264:396].to_list()
 
  for b in range(0, len(BN)):
    BN[b] = float(BN[b])
  
  Total_BN=sum(BN)
  
  Brunei_Darussalam=int(Total_BN)  

  #Abstracting the coulumn ' Indonesia ' between the year 2000-2010
  IDN= df[' Indonesia '][264:396].to_list()
  #convert the IDN into numeric (decimal / float)
  for b in range(0, len(IDN)):
    IDN[b] = float(IDN[b])
  #finding the total amount of visitors
  Total_IDN=sum(IDN)
  #making the value an integer
  Indonesia=int(Total_IDN)
  
  #Abstracting the coulumn ' Malaysia ' between the year 2000-2010
  MY= df[' Malaysia '][264:396].to_list()
  #convert the MY into numeric (decimal / float)
  for b in range(0, len(MY)):
    MY[b] = float(MY[b])
  #finding the total amount of visitors
  Total_MY=sum(MY)
  #making the value an integer
  Malaysia=int(Total_MY)
  
  #Abstracting the coulumn ' Philippines ' between the year 2000-2010
  PH= df[' Philippines '][264:396].to_list()
  #convert the PH into numeric (decimal / float)
  for b in range(0, len(PH)):
    PH[b] = float(PH[b])
  #finding the total amount of visitors
  Total_PH=sum(PH)
  #making the value an integer
  Philippines=int(Total_PH)
   
  #Abstracting the coulumn ' Thailand ' between the year 2000-2010
  TH= df[' Thailand '][264:396].to_list()
  #convert the TH into numeric (decimal / float)
  for b in range(0, len(TH)):
    TH[b] = float(TH[b])
  #finding the total amount of visitors
  Total_TH=sum(TH)
  #making the value an integer
  Thailand=int(Total_TH)

  #Abstracting the coulumn ' Viet Nam ' between the year 2000-2010
  VN= df[' Viet Nam '][264:396].to_list()
  #convert the VN into numeric (decimal / float)
  for b in range(0, len(VN)):
    VN[b] = float(VN[b])
  #finding the total amount of visitors
  Total_VN=sum(VN)
  #making the value an integer
  Viet_Nam=int(Total_VN)
   

  #Abstracting the coulumn ' Myanmar ' between the year 2000-2010
  MM= df[' Myanmar '][264:396].to_list()
  #convert the MM into numeric (decimal / float)
  for b in range(0, len(MM)):
    MM[b] = float(MM[b])
  #finding the total amount of visitors
  Toatl_MM=sum(MM)
  #making the value an integer
  Myanmar=int(Toatl_MM)
  countries_population={"Brunei Darussalam":Brunei_Darussalam,"Indonesia":Indonesia,"Malaysia":Malaysia,"Philippines":Philippines,"Thailand":Thailand,"Viet Nam":Viet_Nam,"Myanmar":Myanmar}
  #creating a one-dimensional labeled array of the S.E.A region dictionary
  s = pd.Series(countries_population)

  print(s.nlargest(3))


def printcountry():
  
  #df['Total'] = df.iloc[264:396, 2:9].sum(axis=0)
  df = pd.read_csv('MonthlyVisitors.csv')
  
  
  Regions = ['South East Asia Region', 'Asia Pacific Region' , 'South Asia Pacific Region', 'Middle East Region', 'Europe Region' ,'North America Region', 'Australia Region', 'Africa Region']
  for i in range(len(Regions)):

    print("\n", str(i+1),': ',Regions[i])
    
  print("\n")
  ans = input("Press 1 - 8 for region: ")
  try:
    ans = int(ans)
    if ans >8:
      print("Try again!")
      printcountry()

    elif ans <1:
      print("Try again!")
      printcountry

    else:

      print("\nYou have chosen the",str(Regions[ans-1]),)

    if ans == 1:
      print(df.iloc[264:396, 2:9])
     
      sortTopCountries(df.iloc[264:396, 2:9])
      
     # df['Total'] = df.iloc[264:396, 2:9]
    elif ans == 2:
      print(df.iloc[264:396, 9:14])
      sortTopCountries(df.iloc[264:396, 9:14])
     # df['Total'] = df.iloc[264:396, 9:14]

    elif ans == 3:
      print(df.iloc[264:396, 14:17])
      sortTopCountries(df.iloc[264:396, 14:17])
      #df['Total'] = df.iloc[264:396, 14:17]

    elif ans == 4:
      print(df.iloc[264:396, 17:20])
      sortTopCountries(df.iloc[264:396, 17:20])
      #df['Total'] = df.iloc[264:396, 17:20]
    elif ans == 5:
      print(df.iloc[264:396, 20:31])
      sortTopCountries(df.iloc[264:396, 20:31])
      #df['Total'] = df.iloc[264:396, 20:31]

    elif ans == 6:
      print(df.iloc[264:396, 31:33])
      sortTopCountries(df.iloc[264:396, 31:33])
      #df['Total'] = df.iloc[264:396, 31:33]
    
    elif ans == 7:
      print(df.iloc[264:396, 33:35])
      sortTopCountries(df.iloc[264:396, 33:35])
      #df['Total'] = df.iloc[264:396, 33:35]

    elif ans == 8:
      print(df.iloc[264:396, -1])
      sortTopCountries(df.iloc[264:396, -1])
      #df['Total'] = df.iloc[264:396, -1]
  
      

  except ValueError:

    print("Try again!")
    printcountry()
  
Analyse()

import matplotlib.pyplot as pit
print("GENERATING SOUTH EAST ASIA REGION PIE CHART...")
#The list for top 3 countries of the most amount of visitors in S.E.A region between the year 2000-2010
activities = ['Indonesia', 'Malaysia', 'Thailand']

#The list for the amount of visitors in S.E.A region between the year 2000-2010
slices = [18692646, 6976158, 3520036]

#The list for the colours 
colours = ['r', 'g', 'b']

#pie chart
pit.pie(slices,
      labels=activities,
      startangle=90,
      shadow=True,
      explode=(0.2, 0, 0),
      autopct='%1.2f%%')


pit.legend()
pit.show()

