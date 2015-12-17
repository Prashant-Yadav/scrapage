import json

data = json.loads(open('../fetch_data_items.json').read())
title = data['title']
headings = data['headings']
links = data['links']
paragraphs = data['paragraphs']

with open('content.txt', 'w') as f:
	
	f.write("Page title: \n")
	for t in title:
		f.write(t+"\n")
	
	f.write("\nPage headings: \n")
	for heading in headings:
		f.write(heading+"\n")
	
	f.write("\nParagraphs: \n")
	for para in paragraphs:
		f.write(para+"\n")
	
	i = 0
	f.write("\nLinks: \n")
	for l in links:
		i+=1
		f.write(str(i)+". "+l+"\n")