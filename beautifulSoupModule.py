import requests, bs4
res = requests.get('http://nostarch.com')
print(res.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml')
print(type(noStarchSoup))
with open('example.html', 'r') as example_file:

    example_soup = bs4.BeautifulSoup(example_file.read(), 'lxml')
    elems = example_soup.select('#author')
    p_elems = example_soup.select('p')
    print(type(example_soup))
    print(elems)
    print(elems[0].getText())
    print(p_elems[2].getText())
#getting data from an elements attributes
with open('example.html', 'r') as soup:
    index = 0
    soup = bs4.BeautifulSoup(soup.read(), 'lxml')
    span_elems = soup.select('span')[index]
    print(f' Here is the span element at index {index} {span_elems}')
    print(span_elems.get('id'))
    print(span_elems.attrs)