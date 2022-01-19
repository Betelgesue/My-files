import bs4, requests

def autorzy_empik():

    # Defining variables to use. Each list will hold results for appropriate output.
    base_url = "https://www.empik.com/bestsellery/ksiazki/fantastyka-horror?searchCategory=317101&hideUnavailable=true&qtype=facetForm&resultsPP=60"
    author_titles = []
    author_counter = 0
    all_authors = set()

    req = requests.get(base_url)
    soup = bs4.BeautifulSoup(req.text, "lxml")

    # Assign each variable for further iteration through elements
    items = soup.select('.search-list-item-hover')
    authors = soup.select('.smartAuthorWrapper')

    # Append each string into authors_set, so there won`t be any duplicates. Print each author, so user can see available options.
    for author in authors:
        all_authors.add(author.text.replace("\n","").rstrip())

    for author in all_authors:
        print(author)
    print('\n' *2)

    # Simple while loop to get user`s input. Only values from authors_set are acceptable
    while True:
        auth = input("Enter author name:\n")
        
        if auth == 'q':
            break
        elif auth not in all_authors:
            print("Well it seems like there are no books for this author. Ensure that you write author`s name correctly. Try again or press 'q' to break")
        else:
            break

    # Iterate through items and gather titles for each position assigned to chosen author.
    for item in items:
        if auth in str(item.find_all('button')):
            author_counter += 1
            author_titles.append(item.find_all('a')[0]['title'])
            
    print(f'This author has {author_counter} titles\n')

    for author in author_titles:
        print(author)

if __name__ == "__main__":
    autorzy_empik()