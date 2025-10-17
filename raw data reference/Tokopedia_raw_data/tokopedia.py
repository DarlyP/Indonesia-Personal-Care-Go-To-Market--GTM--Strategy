from playwright.sync_api import sync_playwright
import csv

def scrape_tokopedia(query, max_items=20):
    """
    Scrapes Tokopedia search results for a given query.

    Args:
        query (str): Search keyword.
        max_items (int): Maximum number of items to scrape.

    Returns:
        list of dict: Scraped product data (title, price, link).
    """
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  
        )
        url = f"https://www.tokopedia.com/search?st=product&q={query}"
        page.goto(url)
        # Tunggu hingga item muncul
        page.wait_for_selector('div.css-1g20a2m')
        items = page.query_selector_all('div.css-1g20a2m')
        for item in items[:max_items]:
            title_el = item.query_selector('div.css-1bjwylw')
            price_el = item.query_selector('div.css-rhd610')
            link_el = item.query_selector('a')
            if not (title_el and price_el and link_el):
                continue
            title = title_el.inner_text().strip()
            price = price_el.inner_text().strip()
            link = link_el.get_attribute('href')
            results.append({
                'title': title,
                'price': price,
                'link': link
            })
        browser.close()
    return results

if __name__ == "__main__":
    keyword = input("Skincare")
    products = scrape_tokopedia(keyword, max_items=50)
    # Simpan hasil ke CSV
    with open('tokopedia_results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'price', 'link'])
        writer.writeheader()
        for prod in products:
            writer.writerow(prod)
    print(f"Selesai! {len(products)} produk disimpan di tokopedia_results.csv")
