from bs4 import BeautifulSoup
html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="first">
        <h3 data-example="yes">Hi</h3>
        <p> more text</p>
    </div>
    <ol>
        <li class="special">list one</li>
        <li class="special">list two</li>
        <li>list three</li>
    </ol>
    <div>bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_="special").parent
data = soup.find(id="first").find_next_sibling()
print(data)
# print(soup)
# print(type(soup))
# # type returns the <class 'bs4.BeautifulSoup'>
# d = soup.body.ol
# print(d)

# f = soup.select("#first")
# print(f)
# # p = soup.find_all("div")[1]
# # using a for loop to loop through the divs
# for p in soup.select("div"):
#     print(p.get_text())