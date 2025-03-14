import requests
import math
#from openpyxl import Workbook
from bs4 import BeautifulSoup as bs
import regex as re
from selenium import webdriver
from selenium.webdriver.chrome.options import (Options)
from database import db,Hackathons

#wb = Workbook()
#ws = wb.active
#wb = Workbook()
#ws = wb.active
headers = ["Name", "URL", "Location", "Image", "Time Left","Submission Date", "Prize Amount", "Description" , "Mode"]
#ws.append(headers)

# DevPost

def devpost():

    response = requests.get("https://devpost.com/api/hackathons?page=1&status[]=open")
    data = response.json()
    total_page_count = math.ceil(data["meta"]["total_count"] / data["meta"]["per_page"])

    for i in range(total_page_count):
        response = requests.get(f"https://devpost.com/api/hackathons?page={i + 1}&status[]=open")
        data = response.json()
        hackathons = data["hackathons"]

        for hackathon in hackathons:
            if hackathon["invite_only"] == False:
                row = [
                    hackathon["title"],
                    hackathon["url"],
                    hackathon["displayed_location"]["location"],
                    hackathon["thumbnail_url"],
                    hackathon["time_left_to_submission"],
                    hackathon["submission_period_dates"],
                    hackathon["prize_amount"].replace("<span data-currency-value>", "").replace("</span>", ""),
                'Empty',
                "Empty"
                ]
                new_competition = Hackathons(
    name=hackathon["title"],
    url=hackathon["url"],
    location=hackathon["displayed_location"]["location"],
    image=hackathon["thumbnail_url"],
    time_left=hackathon["time_left_to_submission"],
    submissions=hackathon["submission_period_dates"],
    prize_amount=hackathon["prize_amount"].replace("<span data-currency-value>", "").replace("</span>", ""),
                
    description='Empty',
    mode='Empty'
)
                db.session.add(new_competition)
                db.session.commit()
        print("Succesfully Saved")

def h2skill():

    response = requests.get("https://hack2skill.com/#ongoin-initiatives")
    data = response.text
    soup = bs(data, "html.parser")

    infos = soup.find_all("a", class_="text-link")

    for i in infos[0:2]:
        if not i:
            continue
        r1 = i.find("h6").text.strip()
        r2 = i["href"]
        r3 = i.find("p", class_="hack-description").text.strip()
        r4 = i.find("p", class_="last-date").text.strip()
        r4 = re.sub(r'\s+', ' ', r4).strip()
        r5 = i.find("p", class_="hack-type").text.strip()
        r5 = re.sub(r'\s+', ' ', r5).strip()
        rows = [r1, r2,"Empty","Empty", "Empty",r4, "Empty",r3, r5]

        #ws.append(rows)
        new_competition = Hackathons(
    name=r1,
    url=r2,
    location="Empty",
    image="Empty",
    time_left="Empty",
    submissions=r4,
    prize_amount="Empty",      
    description=r3,
    mode=r5
)
        db.session.add(new_competition)
        db.session.commit()

    print("Succesfully Saved")

def hackerEarth():
    response = requests.get("https://www.hackerearth.com/challenges/hackathon/")
    data = response.text
    soup = bs(data, "html.parser")

    a = soup.find_all("div", class_="challenge-card-modern")  # Inganethe Kure sadanam undavum
    for i in a:  # pakshe athile ella sadanathilum thazhe kodutha saanam undavanam enilla
        link = i.find("a", class_="challenge-card-wrapper challenge-card-link")
        if link:
            apply = link["href"]
            image = link.find("div", class_="event-image")
            if image:
                name = image["alt"]
                png_link = image["style"]
                png_link = re.findall(r"url\('([^']+)'\)", png_link)[0]
                #ws.append([name,apply,"Empty",png_link,"Empty","Empty","Empty","Empty","Empty"])
                new_competition = Hackathons(
    name=name,
    url=apply,
    location="Empty",
    image=png_link,
    time_left="Empty",
    submissions="Empty",
    prize_amount="Empty",         
    description='Empty',
    mode='Empty'
)
                db.session.add(new_competition)
                db.session.commit()


    print("Succesfully Saved")

def dynamic():

    options = Options()
    options.add_argument(f"--window-size=1366,768")
    options.add_argument(
        f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        f'Chrome/88.0.4324.182 Safari/537.36')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless=new")
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://mlh.io/seasons/2025/events")
    html = driver.page_source
    data = bs(html, "html.parser")
    upcoming = data.find("h3", class_="text-center mb-3")
    print(upcoming.text)
    events = upcoming.find_next_siblings("div")

    for i in events:
        if i.find("div", class_="event-hybrid-notes").text.strip() == "Digital Only":
            name = i.find("h3", class_="event-name").text.strip()
            link = i.find("a")
            link = link["href"]
            date = i.find("p", class_="event-date")
            if date:
                date = date.text.strip()
            image = i.find("img")["src"]
            type = i.find("div", class_="event-hybrid-notes").text.strip()
            #ws.append([name, link, "Empty",  image, "Empty", date,"Empty", "Empty", type])
            new_competition = Hackathons(
    name=name,
    url=link,
    location="Empty",
    image=image,
    time_left="Empty",
    submissions=date,
    prize_amount="Empty",         
    description='Empty',
    mode=type
)
            db.session.add(new_competition)
            db.session.commit()


    print("Done Scrapping All The Opportunities.xlsx")

def proElevate():


    options = Options()
    options.add_argument(f"--window-size=1366,768")
    options.add_argument(
        f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        f'Chrome/88.0.4324.182 Safari/537.36')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless=new")
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.proelevate.in/events?status=upcoming")
    html = driver.page_source
    data = bs(html, "html.parser")

    a = data.find_all("a", class_="w-full")

    for i in a:
        link = "https://www.proelevate.in/" + i["href"]
        name = i.find("h3", class_="text-2xl font-semibold leading-none tracking-tight").text.strip()
        desc = i.find("p", class_="text-muted-foreground text-wrap text-sm break-all").text.strip()
        last = i.find("div",
                      class_="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent m-1 text-rose-700 bg-rose-100").text.strip()
        type = i.find("div",
                      class_="inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 border-transparent capitalize text-purple-700 bg-purple-100 m-1").text.strip()

        #ws.append([name, link, "Empty", "Empty", "Empty", last, "Empty",  desc, type])
        new_competition = Hackathons(
    name=name,
    url=link,
    location="Empty",
    image='Empty',
    time_left="Empty",
    submissions=last,
    prize_amount="Empty",         
    description=desc,
    mode=type
)
        db.session.add(new_competition)
        db.session.commit()

    print("Succsfully ")

#h2skill()
#hackerEarth()
#dynamic()
#proElevate()
#devpost()


#wb.save("Newest.xlsx")