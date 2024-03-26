from bs4 import BeautifulSoup
import webbrowser
import pyautogui
import pydirectinput
from time import sleep

# Read the HTML file
file_path = "photos.html"
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# Find all <a> tags with photos and extract href attributes into a list
href_list = [link.get("href") for link in soup.find_all("a")]
href_list = filter(lambda h: "photo.php" in h if h is not None else False, href_list)

for href in href_list:
    print(href)

    # TODO: path to chrome executable goes here
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(
        href
    )

    # Move mouse around to "Save Image As"
    # Sleep in between to account for page loading times. 5 seconds is pretty generous.
    pydirectinput.moveTo(600, 400)
    sleep(5)
    pydirectinput.click(button="right")
    pydirectinput.moveTo(630, 460)
    pydirectinput.click()
    sleep(5)
    pydirectinput.keyDown("enter")
    pydirectinput.keyUp("enter")
    sleep(5)
    pydirectinput.keyDown("ctrl")
    pydirectinput.keyDown("w")
    pydirectinput.keyUp("ctrl")
    pydirectinput.keyUp("w")
