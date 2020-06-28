# LeadParser
LeadParser parses through HTML files of emails containing real estate leads that agents receive. The extracted information contains name, email, phone, beds, baths, address and whether it's a buyer or a seller. 

PACKAGES (import) required:
1. bs4
2. codecs
3. json
4. re
5. os

How To Run:
1. Download LeadParser directory containing 'Data', 'Main', 'Output' directories.
2. Add all the HTML files you want to the 'Data' folder.
3. open cmd and change directory to 'Main'
4. Run the python script named 'Parser.py'
5. Open 'Output' folder and check 'output.json'  for lead data.

CITATIONS:
1. https://www.crummy.com/software/BeautifulSoup/bs4/doc/

NOTE: DO NOT DELETE 'output.json' file. It get's overwritten based on contents of the data folder everytime the parser is run.

 
