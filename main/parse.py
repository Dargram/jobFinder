from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


class BaseJobParser(ABC):
    def fetch_page(self, target_url: str) -> str:
        with sync_playwright() as p:

            browser = p.chromium.launch(headless=True)
            page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

            try:
                page.goto(target_url, wait_until="domcontentloaded")
                html = page.content()
            
            finally:
                browser.close()

            return html

    @abstractmethod
    def parse(self, query: str):
        pass


class WorkUaParser(BaseJobParser):
    def parse(self, query):

        formatted_query = query.strip().lower().replace(" ", "-")
        base_url = f"https://www.work.ua/jobs-{formatted_query}"

        current_page = 1
        number = 1

        while True:
            target_url = f"{base_url}?page={current_page}"
            print(target_url)

            html = self.fetch_page(target_url)

            soup = BeautifulSoup(html, "html.parser")
            job_links = soup.select("h2 > a[href *='/jobs/']")

            if not job_links:
                print(f"Not vacancies on page {current_page}")
                break


            for link in job_links:

                href = link.get("href")
                title = link.get_text(strip=True)

                print(f"{number}. {href, title} \n")
                number += 1                
            
            current_page += 1
        print(f"Vacancies: {number - 1}")
parser = WorkUaParser()
parser.parse("дизайнер")