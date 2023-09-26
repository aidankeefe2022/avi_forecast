import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


path = 'c:/Users/bnhke/.vscode/python/avi forecast/'

def tempReport(input):
    plt.bar(input['Date'], height=input['Temp'])
    return
def recentSnow(input):
    print(input['New Snow'].tail().sum())

    return input['New Snow'].tail().sum()
def risk(input):
    print(input['Danger'].tail(1))
    return 
def windDirection():

    return
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
    numToAvi = {1:avi_bridger, 2:avi_lionhead, 3:avi_centennials, 4:avi_cooke_city,
            5:avi_southern_madison,6:avi_northern_madison,7:avi_northern_gallatin,8:avi_southern_gallatin}
    user_input = input("1: avi_bridger \n2:avi_lionhead \n3:avi_centennials\n4:avi_cooke_city\n5:avi_southern_madison\n6:avi_northern_madison\n7:avi_northern_gallatin\n8:avi_southern_gallatin")

    recentSnow(numToAvi[int(user_input)])
    risk(numToAvi[int(user_input)])
            

#%%

#%%
