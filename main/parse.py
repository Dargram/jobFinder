from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

target_url = "https://www.work.ua/jobs-remote-програмування"

print("Завантажуємо сторінку...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    page.goto(target_url, wait_until="networkidle")
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "html.parser")

job_links = soup.select("div.mb-lg h2.my-0 a")

for link in job_links:
    print(link.get_text(strip=True))