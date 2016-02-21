import bottlenose
import xml.etree.ElementTree as ET
from io import StringIO

def main():

	accessKey= "AKIAJWACTA74DBVKYH5A"
	secretKey="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"
	associateTag="snakcs"
	chipsData= []

	#10 items per page can change page through ItemPage attribute
	amazon = bottlenose.Amazon(accessKey, secretKey, associateTag, MaxQPS=0.8)
	response = amazon.ItemSearch(Keywords="Chips", SearchIndex="All", ItemPage=10).decode(encoding='UTF-8')
	
	#gets the root tag from the xml response <ItemSearchResponse>


	#removes namespaces of xml files to find matching element for find()
	it= ET.iterparse(StringIO(response))
	for _, el in it:
		if '}' in el.tag:
			el.tag = el.tag.split('}', 1)[1]
	root= it.root

	
	for items in root[1].findall('Item'):
		data={}
		asin=""
		parentAsin="None"
		detailsUrl=""
		reviewsUrl=""
		manufacturer=""
		productGroup=""
		title=""

		itemAttributes= items.find("ItemAttributes")
		itemLink= items.find("ItemLinks")
		

		asin= items.find("ASIN").text
		parentAsin= items.find("ParentASIN")
		detailsUrl= items.find("DetailPageURL").text
		reviewsUrl= itemLink[5].find("URL").text
		
		manufacturer= itemAttributes.find("Manufacturer")
		productGroup= itemAttributes.find("ProductGroup").text
		title= itemAttributes.find("Title").text

		if parentAsin is not None:
			parentAsin= parentAsin.text

		if manufacturer is not None:
			manufacturer= manufacturer.text

		data["title"]= title
		data["asin"]= asin;
		data["parentAsin"]= parentAsin
		data["detailsUrl"]= detailsUrl
		data["manufacturer"]=manufacturer
		data["reviewsUrl"]=reviewsUrl
		data["productGroup"]= productGroup
		chipsData.append(data)
		

	
	output= open("responseData.txt", "a")
	output.write(str(chipsData))
	
	
	
	



main()