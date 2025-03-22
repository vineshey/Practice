import requests
from bs4 import BeautifulSoup
import json

def fetch_course_data():
    url = "https://trainings.internshala.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch data"}

    soup = BeautifulSoup(response.text, "html.parser")

    courses = []
    course_cards = soup.select("#course-card")  # Adjust selector if necessary

    for card in course_cards:
        title = card.select_one("div.course-content > div > h4")
        rating = card.select_one("div.course-content > div > div.feedback > div.star")
        price = card.select_one("div.course-price > div")
        link = card.select_one("a")

        courses.append({
            "title": title.text.strip() if title else "N/A",
            "rating": rating.text.strip() if rating else "No rating",
            "price": price.text.strip() if price else "Free",
            "link": "https://trainings.internshala.com" + link["href"] if link else "#"
        })

    return json.dumps(courses, indent=2)
