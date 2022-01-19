import requests, bs4, time

def szukanie_w_empiku(i):
    
    # Defining variables to use. Each list will hold results for appropriate output.
    base_url = "https://www.empik.com/bestsellery/ksiazki/fantastyka-horror?resultsPP=45"
    titles_list = []
    prices_list = []
    authors_list = []

    req = requests.get(base_url)
    soup = bs4.BeautifulSoup(req.text, "lxml")

    # Assign each variable for further iteration through elements 
    titles = soup.select('.product-title')
    authors = soup.select('.smartAuthorWrapper')
    prices = soup.select('.product-details-wrapper-header')

    #Instead of creating 3 separate loops, zip together created lists and iterate through it.
    # After processing append each element into appropriate list.
    for title, author, price in zip(titles, authors, prices):
        titles_list.append(title.getText().split('\n')[3])
        authors_list.append(author.getText().replace("\n",""))
        prices_list.append(price.getText().replace("\n","").split()[0])
    
    # Zip together all lists, so I can use enumerate function and iterate through each element with index number.
    # The open new txt file named "i" and iterate through zipped lists.
    zipped = zip(titles_list, prices_list, authors_list)
    
    with open(f"pliki\\{i}.txt", mode="w", encoding="utf-8") as f:
    
        for index, item in enumerate(zipped):
            f.write(f"{index + 1}.  {item}\n")
        f.close()

if __name__ == "__main__":

    i = 1
    time_wait = 10
    while True:
        szukanie_w_empiku(i)
        time.sleep(time_wait)
        i += 1