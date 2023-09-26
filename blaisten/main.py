from playwright.sync_api import sync_playwright
import time


def scroll_me():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.blaisten.com.ar/ferrum")
        time.sleep(2)
        page.wait_for_load_state('networkidle')
        for x in range(1, 3):
            page.keyboard.press('End')
            print('scrolling key press', x)
            page.get_by_text('Ver más productos').click()
            time.sleep(1)

        browser.close()


def main():
    scroll_me()


if __name__ == "__main__":
    main()
