import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://codegurus.com.br
floripacodegurus.com.br
"""


padrao = re.compile(r'(https?://)?(www.)?\w+\.(com|gov)(.br)?')

matches = padrao.finditer(urls)
for match in matches:
    print(match)