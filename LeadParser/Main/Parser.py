from bs4 import BeautifulSoup
import json
import re
import os
import codecs


#Scans the HTML document and retrieves the Lead Name
def get_name(soup):
	#Find all fonts and loop through
	for font_tags in soup.find_all('font'):
		for font_tags_text in font_tags.contents:
			if 'Name' in font_tags_text:
				#Sibling tag of Name contains our lead name
				return font_tags_text.find_next_sibling().contents[0]

#Scans the HTML document and retrieves the Lead e-mail
def get_email(soup):
	#loop through all tags containing an email
	for tags in soup.find_all(href=re.compile('mailto:')):
		for tags_contents in tags.contents:
			#Our lead e-mail is without @email.realtor.com
			if 'realtor.com' not in tags_contents:
				return tags_contents

#Scans the HTML document and retrieves the Lead Phone
def get_phone(soup):
	#Retrieve tag with regex 'tel:+' in href attribute
	contact_tag = soup.find(href=re.compile('tel:'))
	return contact_tag.contents[0]

#Scans the HTML document and retrieves the no of Beds
def get_beds(soup):
	#Loop though all font tags
	for font_tags in soup.find_all('font'):
		for font_tags_text in font_tags.contents:
			#Sibling of the one containing 'Beds' will give us no of Beds
			if 'Beds' in font_tags_text:
				return font_tags_text.find_next_sibling().contents[0]

#Scans the document and retrieves the no of baths
def get_baths(soup):
	#Loop through all font tags
	for font_tags in soup.find_all('font'):
		for font_tags_text in font_tags.contents:
			#Sibling of the one containing 'Baths' will give us no of baths
			if 'Baths' in font_tags_text:
				return font_tags_text.find_next_sibling().contents[0]

#Scans the HTML document and retrieves Lead address
def get_address(soup):
	#Loop through the font tags
	for font_tags in soup.find_all('font'):
		for font_tags_text in font_tags.contents:
			#After reaching 'Beds' we will traverse back to the first tag content 
			#containing 'email.realtor.com' in href attribute, its contents will
			#give us the Lead address
			if 'Beds' in font_tags_text:
				return font_tags_text.find_all_previous(href=re.compile('//email.realtor.com'))[0].contents[0]

#Checks the sub head returns true if Lead type is Seller
def is_seller(soup):
      sub_head = []
	for font_tags in soup.find_all('font'):
		for font_tags_text in font_tags.contents:
			if 'interested' in font_tags_text:
				sub_head = font_tags_text
                              break
                               

	
	#List to store all comparison checks of keywords in sub-head
	sell_check = []
	#Keywords that may indicate if the person wants to sell
	key_words = ['sell', 'selling', 'Sell', 'Selling']

	for keys in key_words:
		sell_check.append(keys in sub_head)

	return(any(sell_check))

#This is the path to our HTML data
data_path = (os.path.dirname(os.getcwd()) + '/Data')

#this will contain all leads data
data = {}
data['leads'] = []

#Loop through all HTML files in the Data folder and retreive data
for html_file in os.listdir(data_path):

		html_doc = codecs.open(data_path+"/"+html_file)
		#soup will get a BeautifulSoup object with our HTML file data
		soup = BeautifulSoup(html_doc, 'html.parser')

		name = get_name(soup)
		
		email = get_email(soup)
		
		phone = get_phone(soup)
		
		beds = get_beds(soup)
		
		baths = get_baths(soup)
		
		address = get_address(soup)
		
		#lead_type will be given a string based on return val of is_seller()
		lead_type = 'Seller' if is_seller(soup) else 'Buyer'

		#All the retrieved data is populated in data dictionary
		data['leads'].append({
			'name' : name,
			'email': email,
			'phone': phone,
			'beds': beds,
			'baths': baths,
			'address': address,
			'type': lead_type
			})

#Path containing our output.json file
output_path = os.path.dirname(os.getcwd()) + '/Output' + '/'

#Dump all data into json file
with open(output_path +'output.json', 'w') as outfile:
	json.dump(data, outfile, indent=2)
