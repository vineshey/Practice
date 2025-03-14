import requests
from bs4 import BeautifulSoup

# Function to scrape internship data
def fetch_internship_data():
    url = "https://www.internshala.com/internships/engineering-internship/"

    # Send HTTP request
    response = requests.get(url)
    
    # Parse the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Data collection
    data = []
    internships = soup.find_all('div', class_='individual_internship')

    for internship in internships:
        try:
            # Extract Title
            title = internship.find('a', class_='job-title-href').text.strip()

            # Extract Company Name
            company = internship.find('p', class_='company-name').text.strip()

            # Extract Location
            location = internship.find('div', class_='row-1-item locations').text.strip()

            # Extract Duration
            duration = internship.find('div', class_='row-1-item').text.strip()

            # Extract Stipend
            stipend = internship.find('span', class_='stipend').text.strip()

            # Extract Application Link
            link = "https://www.internshala.com" + internship.find('a', class_='job-title-href')['href']

            # Append the collected data
            data.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Duration": duration,
                "Stipend": stipend,
                "Link to Apply": link
            })

        except Exception as e:
            print(f"❗ Error fetching data for one result: {e}")
    
    return data