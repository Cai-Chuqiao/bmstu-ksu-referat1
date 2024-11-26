from bs4 import BeautifulSoup
import json
from shadowspider import get_content1, get_content2, get_content3
import os


url = "https://solutionportfolio.net.sap/bcm/industry/HEALTH"

#get all title and href for single page
def get_title_href1():
    try:
        with open('temp.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

            soup = BeautifulSoup(html_content, 'html.parser')

            result = {}
            current_key = None

            for element in soup.find_all(['div', 'a']):
                if element.name == 'div' and 'sl-content-name' in element.get('class', []):
                    current_key = element.get_text(strip=True)
                    result[current_key] = {}  # Initialize as an empty dictionary
                elif element.name == 'a' and 'sl-sub-element' in element.get('class', []):
                    if current_key is not None:
                        sub_name = element.get_text(strip=True)
                        href = element['href']
                        result[current_key][sub_name] = {'href': href}  # Add sub-name and href
            return result

    except Exception as e:
        print(e)

def get_title_href2():
    try:
        with open('temp.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

            soup = BeautifulSoup(html_content, 'html.parser')

            result = {}

            for element in soup.find_all('solution-library-web-child-object'):
                for e in element.find_all(['div','a']):
                    if e.name == 'div' and 'sl-content-name' in e.get('class', []):
                        title = e.get_text(strip=True)
                        result[title] = {}
                        result[title]['content'] = {}
                    elif e.name == 'div' and 'sl-content-description' in e.get('class', []):
                        description = e.get_text(strip=True)
                        result[title]['description'] = description
                    elif e.name == 'a' and 'sl-sub-element' in e.get('class', []):
                        subtitle = e.get_text(strip=True)
                        href = e['href']
                        result[title]['content'][subtitle] = {'href': href}
            return result

    except Exception as e:
        print(e)


            
if __name__ == '__main__':
    if not os.path.exists('all_content.json'):
        get_content1(url)
        result = get_title_href1()
        with open("all_content.json", 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)     
    with open("all_content.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    for k0, v0 in data.items():
        for k1, v1 in v0.items():
            if 'content' not in data[k0][k1]:
                get_content2(v1['href'])
                data[k0][k1]['content'] = get_title_href2()
            for k2, v2 in data[k0][k1]['content'].items():
                for k3, v3 in v2['content'].items():
                    if 'content' not in data[k0][k1]['content'][k2]['content'][k3]:
                        data[k0][k1]['content'][k2]['content'][k3]['content'] = get_content3(v3['href'])
                        with open("all_content.json", 'w', encoding='utf-8') as f:
                            json.dump(data, f, ensure_ascii=False, indent=4) 


            