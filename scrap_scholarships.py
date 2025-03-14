import requests
from bs4 import BeautifulSoup as bs
from database import db,Scholarships

# URL of the NSP portal

def fetch_filtered_links():
    url = "https://services.india.gov.in/service/search?kw=engineering+scholarships&ln=en&cat_id_search=&location=district&state_id=&district_name=&pin_code=0"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully fetched the page!")
        
        # Parse the page content
        soup = bs(response.content, 'html.parser')
        
        # Extract all headings with 'h3' tag
        headings = soup.find_all('h3')
        
        filtered_links = []
        for heading in headings:
            link = heading.find('a')
            if link:
                href = link.get('href')
                if href:
                    filtered_links.append({
                        'link': href,
                        'title': link.text.strip()  # Strip to remove extra spaces
                    })
                    
        
        # Return the filtered links
        return filtered_links
    else:
        print(f"Failed to fetch the page, status code: {response.status_code}")
        return []

# Call the function and print the result
#filtered_links = fetch_filtered_links(url)
#print(filtered_links)
