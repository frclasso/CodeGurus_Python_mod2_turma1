import re

emails = """
FabioClasso@gmail.com
fabio.classo@codegurus.edu
fabio-74-classo@my-work.net
"""
padrao = re.compile(r'[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')

matches = padrao.finditer(emails)
for match in matches:
    print(match)