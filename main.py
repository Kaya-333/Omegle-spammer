from playwright.sync_api import sync_playwright
import os

def clear():
    clear = lambda: os.system('cls')
    clear()

with open("message.txt", "r", encoding="utf-8") as f:
    content = f.read()

def run():
    page.goto("https://www.omegle.com/")
    page.locator("input[type=\"text\"]").fill(interest)
    page.locator("img[alt=\"Text chat\"]").click()
    page.locator("text=OUR AGE RESTRICTIONS HAVE CHANGED. YOU MUST BE 18 OR OLDER TO USE OMEGLE. Person >> input[type=\"checkbox\"]").check()
    page.locator("text=By checking the box you acknowledge that you have reviewed and agree to be bound >> input[type=\"checkbox\"]").check()
    page.locator("text=Confirm & continue").click()

def spam():
    page.locator("textarea").fill(content)
    page.locator("text=SendEnter").click()
    page.locator("text=StopEsc").click()
    page.locator("text=Really?Esc").click()
    page.locator("text=NewEsc").click()
    print(f"[{cont}] Messages sent")

clear()
interest = input("Interest: ")
clear()

with sync_playwright() as p:
    cont = 1
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    run()
    while True:
        spam()
        cont = cont + 1


