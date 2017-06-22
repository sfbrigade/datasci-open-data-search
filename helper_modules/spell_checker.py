# https://www.kaggle.com/steubk/home-depot-product-search-relevance/fixing-typos/notebook

import requests
import re
import time
from random import randint
import numpy as np

START_SPELL_CHECK="<span class=\"spell\">Showing results for</span>"
END_SPELL_CHECK="<br><span class=\"spell_orig\">Search instead for"

HTML_Codes = (
		("'", '&#39;'),
		('"', '&quot;'),
		('>', '&gt;'),
		('<', '&lt;'),
		('&', '&amp;'),
)

def spell_check(s):
	q = '+'.join(s.split())
	time.sleep(  randint(0,2) ) #relax and don't let google be angry

	try:
		r = requests.get("https://www.google.com/search?q="+q)
	except ConnectionError:
		try:
			r = requests.get("https://www.google.com/search?q="+q)
		except:
			return "connection error"


	content = r.text
	start=content.find(START_SPELL_CHECK) 
	if ( start > -1 ):
		start = start + len(START_SPELL_CHECK)
		end=content.find(END_SPELL_CHECK)
		search= content[start:end]
		search = re.sub(r'<[^>]+>', '', search)
		for code in HTML_Codes:
			search = search.replace(code[1], code[0])
		search = search[1:]
	else:
		return None


	return search ;


###samples
#searches = [ "metal plate cover gcfi", 'artric air portable", "roll roofing lap cemet", "basemetnt window", 
#            "vynal grip strip", "lawn mower- electic" ]
 
#for search in searches:
	#speel_check_search= spell_check(search)
	#print (search+"->" + speel_check_search)