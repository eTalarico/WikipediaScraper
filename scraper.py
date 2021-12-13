
from WikipediaPage import WikipediaPage, GetRandomPage
##
##https://en.wikipedia.org/wiki/Special:Random

#page = WikipediaPage("https://en.wikipedia.org/wiki/CASIC_HW-X100_series_UAV")
page = WikipediaPage("https://en.wikipedia.org/wiki/Category:Plymouth_Argyle_F.C._players")
#page = GetRandomPage()
print(page._links)
print()



