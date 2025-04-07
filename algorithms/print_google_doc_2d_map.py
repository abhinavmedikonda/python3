import requests
import re

def get_document_html(document_url):
    response = requests.get(document_url)
    if response.status_code != 200:
        print(f"Failed to retrieve document. Status code: {response.status_code}")
        return
    html_content = response.text
    return html_content

def translate_to_python(html_content):
    tables = re.findall(r'<table.*?>(.*?)</table>', html_content, re.DOTALL)
    if len(tables) == 0:
        print("No tables found in the document.")
        return
    rows = re.findall(r'<tr.*?>(.*?)</tr>', tables[0], re.DOTALL)
    if len(rows) == 0:
        print("No rows found in the table.")
        return
    keys = []
    values = []
    for i, row in enumerate(rows):
        cells = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
        list = []
        for cell in cells:
            if i == 0:
                keys.append(re.sub(r'<.*?>', '', cell))
            else:
                # Clean up the text by removing HTML tags and extra spaces
                list.append(re.sub(r'<.*?>', '', cell))
        if i != 0:
            values.append(list)
    return [dict(zip(keys, row)) for row in values]

def clean_data(data):
    for item in data:
        item['x-coordinate'] = int(item['x-coordinate'])
        item['y-coordinate'] = int(item['y-coordinate'])
    data.sort(key=lambda x: (-x['y-coordinate'], x['x-coordinate']))
    return data

def print_document(data):
    next_x = 0
    next_y = data[0]['y-coordinate']
    string = ""
    for item in data:
        if next_y != item['y-coordinate']:
            print(string, end="")
            while next_y != item['y-coordinate']:
                print()
                next_y -= 1
            string = ""
            next_x = 0
        if next_x != item['x-coordinate']:
            string += (" " * (item['x-coordinate'] - next_x))
        string += item['Character']
        next_x += item['x-coordinate'] - next_x + 1
    print(string)

def print_public_google_doc_2d_data(document_url):
    try:
        html_content = get_document_html(document_url)
        data = translate_to_python(html_content)
        data = clean_data(data)
        print_document(data)
    except Exception as e:
        print("An error occurred while processing the document.")
        print(e)

if __name__ == "__main__":
    # document_url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    document_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    print_public_google_doc_2d_data(document_url)
