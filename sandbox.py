from bs4 import BeautifulSoup

html = """
<head>
    <p>hey</p>
    <a href="/fresh">link</a>
</head>
<body>
    <p>Hello, world!</p>
    <script>
</body>
"""

doc = BeautifulSoup(html, "html.parser")
head = doc.find("head")
head.insert(0, BeautifulSoup("<base href=http://localhost/proxy/>", "html.parser"))

print(doc.prettify())
