from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fetch_movie_details(movie_name):
    driver = webdriver.Chrome()

    url = "https://www.imdb.com"
    driver.get(url)
    
    # Locate the search box and input the movie name
    search_box = driver.find_element(By.ID, "suggestion-search")
    search_box.send_keys(movie_name)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(1)

    # Click on the first result
    first_result = driver.find_element(By.CSS_SELECTOR, "#__next > main > div.ipc-page-content-container.ipc-page-content-container--full.sc-f91e97af-0.jbRgdG > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid__item.ipc-page-grid__item--span-2 > section:nth-child(4) > div.sc-b03627f1-2.gWHDBT > ul > li:nth-child(1) > div.ipc-metadata-list-summary-item__c > div > a")
    first_result.click()
    time.sleep(1)

    # Extract the movie details
    try:
        title = driver.find_element(By.CLASS_NAME, "hero__primary-text").text
        rating = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span/div/div[2]/div[1]/span[1]").text
        year = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[1]/a").text
        duration = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/ul/li[3]").text
        
    except Exception as e:
        print(f"Error while extracting movie details: {e}")
        title, rating, year, duration, description = "N/A", "N/A", "N/A", "N/A", "N/A"

    movie_details = {
            'Title': title,
            'Rating': rating,
            'Year': year,
            'Duration': duration,
            
        }

    driver.quit()  # Close the browser window after scraping
    return movie_details


def chatbot():
    print("Welcome to the IMDb Movie Details Chatbot!")
    while True:
        movie_name = input("Enter the movie name (or type 'exit' to quit): ")
        if movie_name.lower() == 'exit':
            print("Goodbye!")
            break
        
        movie_details = fetch_movie_details(movie_name)
        
        if movie_details:
            print("\nMovie Details:")
            print(f"Title: {movie_details['Title']}")
            print(f"Rating: {movie_details['Rating']}")
            print(f"Year: {movie_details['Year']}")
            print(f"Duration: {movie_details['Duration']}")
          
        else:
            print("Sorry, I couldn't find the movie details. Please try again.\n")

# Start the chatbot
chatbot()
