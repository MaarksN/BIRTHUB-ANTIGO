from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{os.getcwd()}/benchmark.html")
        result = page.evaluate("window.runBenchmark()")
        print(f"Bad (innerHTML +=): {result['bad']:.2f}ms")
        print(f"Good (insertAdjacentHTML): {result['good']:.2f}ms")
        print(f"Improvement: {result['improvement']:.2f}x faster")
        browser.close()

if __name__ == "__main__":
    run()
