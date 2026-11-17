# Level #11
# IS 303 - Hilton
# Rylek Staker

#import the panda and read the dsv
import pandas as pd

csv = pd.read_csv("video_games_raw.csv")

#Print the intro message and the input for the users row
print("VIDEO GAME CATALOG MANAGER")

row = int(input("\nEnter a row number to inspect: "))

#use iloc to grab the selected row
game = csv.iloc[row]

#print the selected game and information
print("\nSelected Game:")
print(f"Title: {game["Title"]}")
print(f"Platform: {game["Platform"]}")
print(f"Genre: {game["Genre"]}")
print(f"Rating: {game["Rating"]}")
print(f"Current Status: {game["Status"]}")

#Get the new status for the game from the user and update the csv
new_status = input("\nEnter a new status: ")
csv.at[row, "Status"] = new_status

#add the Recommended column and set the games $40 or less and rating 8 or more as "Yes"
csv["Recommended"] = "No"
csv.loc[(csv["Rating"] >= 8) & (csv["Price"] <= 40), "Recommended"] = "Yes"

recommended = csv.query("Recommended == 'Yes'")

print("\nRecommended Games:")
print(recommended[["Title", "Platform", "Price", "Rating"]])

#save the updated data to a new csv file
csv.to_csv("video_games_cleaned.csv", index=False)

print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv.")
