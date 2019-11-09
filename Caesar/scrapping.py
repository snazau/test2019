from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
	url = "https://ru.wikipedia.org/wiki/%D0%A7%D0%B0%D1%81%D1%82%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C"
	req = requests.get(url)
	page_content = req.content

	page_bs = BeautifulSoup(page_content, "html.parser")
	freq_table = page_bs.find_all("table", {"class" : "standard sortable"})

	letters_probs = []
	letters = []
	tds = freq_table[0].find_all("td")
	for i in range(len(tds)):
		tds[i] = tds[i].text.replace("<td>", "").replace("</td>","").replace("\n", "")
		if (i % 4 == 1):
			letters.append(tds[i])
		if (i % 4 == 3):
			letters_probs.append(float(tds[i].replace("%", "")) / 100)

	print(letters, letters_probs)
