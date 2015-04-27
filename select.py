from wiki import getRandom
import webbrowser

def menu():
	base = "http://www.wikipedia.com/wiki/"
	titles = getRandom()
	for i in range(len(titles)):
		print str(i+1) + " " + titles[i]
	choice = input("Enter a number to open the page: ")
	url = base + str(titles[choice-1].replace(" ", "_"))
	webbrowser.open_new_tab(url)