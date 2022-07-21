import os
import csv

cvspath = os.path.join('..', 'Resources', 'netflix_ratings.csv')
video_search = input("What video are you looking for? ")
with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) 
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        if video_search == row[0]:
            print(f"{row[0]} is rated {row[1]} and has a current user rating of {row[5]}")
        else :
            print("Your searched video could not be found.")
            break