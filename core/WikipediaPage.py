import bs4
import nltk
import re
import requests
import warnings


nltk.download('punkt')


class WikipediaPage: 
    """
    A simple structure representing a single page of Wikipedia. Automatically calls the url
    and parses the resulting HTML. Extracts the title, body, and links to other Wikipedia 
    articles. 

    """
    _base_url = "https://en.wikipedia.org"

    def __init__(self, url):
        """
        Gets the relevant content, including title, body, and links to 
        other Wikipedia pages from a Wikipedia url. 

        Inputs: 
            url: The Wikipedia url. 
        """
        self.url = url 
        self._char_match = re.compile("^[a-zA-Z]+$")
        
        ## Attempt to get the HTML to the Wikipedia Page 
        try: 
            response = requests.get(url).content
        except Exception as e: 
            raise Exception("Unable to retrieve the site.", e)

        ## Parse the HTML to retrieve the title, body without tags, and links
        try: 
            ## Get the body and title 
            soup = bs4.BeautifulSoup(response, "html.parser")
            self.title = soup.find(id="firstHeading").get_text()
            body = soup.find(id="bodyContent")
            self.body = body.get_text()

            ## Get the internal linkes 
            links = [link.get("href") for link in body.find_all("a") if link.get("href") is not None]
            links = [link for link in links if link.startswith("/wiki/") and ":" not in link]
            self.links = set(links)
        except Exception as e: 
            raise Exception("Unable to parse the HTML.", e)
            


    def BodyAsNGrames(self, n) -> dict: 
        """
        Converts the body of the Wikipedia page to ngrams. 

        Inputs: 
            n: The max ngram to get. For example, n=1 would only give single
                words. n=2 would be pairs of works.  

        Returns: 
            A dictionary. Keys are the ngrams, values are the number of times 
            they were encountered. 
        """
        tokens = nltk.word_tokenize(self.body.lower())

        grams = {}
        for i in range(1, n+1):
            for g in nltk.ngrams(tokens, i): 
                ## Check that the NGram only contains characters
                only_characters = True
                for word in g: 
                    if not self._char_match.match(word): 
                        only_characters = False
                        break
                
                ## Add the ngram to grams object
                if only_characters:
                    key = tuple(g)
                    if key in grams: ## Ngram already in grams
                        grams[key] = grams[key] + 1
                    else: 
                        grams[key] = 1
        return grams

    

    def GetAllChildPages(self, exclude_urls=[]) -> dict: 
        """
        Gets this page's links to all other Wikipedia pages. 

        Inputs: 
            exclude_urls: any pages that should be excluded from the list of
                returned urls. 

        Returns: A dictionary: page url -> WikipediaPage object for url
        """
        to_be_returned = {}
        for i in set(self.links) - set(exclude_urls):
            full_url = self._base_url + i
            try: 
                new_page = WikipediaPage(full_url)
                to_be_returned[full_url] = new_page
            except Exception: 
                warnings.warn("Unable to get site for " + str(full_url))
                to_be_returned[full_url] = None
        return to_be_returned
        


def GetRandomPage() -> WikipediaPage:
    """
    Returns: A random Wikipedia page. 
    """
    return WikipediaPage(WikipediaPage._base_url + "/wiki/Special:Random") 



def GetRandomTitles(n: int) -> list:
    """
    Parameters:
        n: The number of titles to get.

    Returns: A list of random Wikipedia titles. 
    """
    if n < 1: 
        raise ValueError("n must be greater than or equal to 1.")

    titles = [None] * n
    for i in range(0, n): 
        page = GetRandomPage()
        titles[i] = page.title
    return titles
