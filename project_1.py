'''Web scrapping using Beautifulsoup and requsets'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Send a GET request to the website
url = "https://www.thesun.co.uk/sport/football/"
response = requests.get(url)

#get current date and time\
current_date = datetime.now().date()

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the headlines on the page
    headlines = soup.find_all("a", class_="text-anchor-wrap")  #find_all gets all the elements with the specified information

    # create lists for titles, subtitlesm and links
    titles = []
    subtitles = []
    links = []
    
    #for each headline in headlines, extract the title, subtitle and link and add to the lists prviously created
    for headline in headlines:
        title = headline.find("span").text
        subtitle = headline.find("h3").text
        link = headline.get("href")
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
    
    # Create a dict and then a DataFrame using pandas
    my_dict = {"title": titles, "subtitle": subtitles, "link": links}
    df = pd.DataFrame(my_dict)

    # Save the DataFrame to a CSV file
    df.to_csv(f"headlines_{current_date}.csv", index=False)

    print("Data has been scraped and saved to 'headlines.csv'.")
else:
    print("Failed to retrieve the webpage.")
