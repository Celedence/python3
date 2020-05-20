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
    
</body>
</html>
"""


soup = BeautifulSoup(html, "html.parser")
print(soup)
print(type(soup))
# type returns the <class 'bs4.BeautifulSoup'>