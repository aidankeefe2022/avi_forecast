
import pandas as pd
import matplotlib.pyplot as plt


path = 'c:/Users/bnhke/.vscode/python/avi forecast/'

#creates a bar chart based on date and temp
#returns a list of the last 10 temps in the dataframe
def tempReport(input):
    plt.bar(input['Date'], height=input['Temp'])
    return input['temp'].tail(10).tolist()
#recentSnow returns the last 5 daily snow totals in a list
def recentSnow(input):
    print(input['New Snow'].tail().sum()) #prints the total snowfall over the last 5 days

    return input['New Snow'].tail().tolist()
#this retruns the avi danger rating for the day from the most recent entry in dataframe
def risk(input):
    return input['Danger'].tail(1).tolist()[0]

#gives the most recent wind direction and the most common wind direction
def windDirection(input):
    to_return =[]
    most_common_dir = input['Direction'].tail(3).tolist().most_common()
    most_recent_dir = input['Direction'].tail(1).tolist()[0]
    to_return.append(most_recent_dir)
    to_return.append(most_common_dir)
    return to_return

#is wind speed in the in recent days at speed that would result in wind slab
def windSpeed(input):
    wind_speed = input['Wind H'].tail(3).tolist()
    WSW = False #wind slab wind
    for speed in wind_speed:
        if speed > 10 and speed < 30:
            WSW = True
    return WSW


avi_bridger = pd.read_csv('bridger.csv')
avi_lionhead = pd.read_csv('lionhead.csv')
avi_northern_gallatin = pd.read_csv('northern-gallatin.csv')
avi_northern_madison = pd.read_csv('northern-madison.csv')
avi_southern_gallatin = pd.read_csv('southern-gallatin.csv')
avi_southern_madison = pd.read_csv('southern-madison.csv')
avi_centennials = pd.read_csv('centennials.csv')
avi_cooke_city = pd.read_csv('cooke-city.csv')
user_input = int
while user_input != 000:
    numToAvi = {1: avi_bridger, 2: avi_lionhead, 3: avi_centennials, 4: avi_cooke_city,
            5: avi_southern_madison, 6: avi_northern_madison, 7: avi_northern_gallatin, 8: avi_southern_gallatin }
    user_input = input("1:avi_bridger \n2:avi_lionhead \n3:avi_centennials\n4:avi_cooke_city\n5:avi_southern_madison\n6:avi_northern_madison\n7:avi_northern_gallatin\n8:avi_southern_gallatin")
    try:
        dataframe = numToAvi[int(user_input)]
        print("REPORT \n")

    except:
        print("re-enter")



#%%

#%%
