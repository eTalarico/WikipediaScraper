import unittest
from core.WikipediaPage import WikipediaPage, GetRandomPage, GetRandomTitles

class TestStringMethods(unittest.TestCase):

    def test_GetRandomPage(self):
        """
        Get a random page and check that the title
        and body are not empty strings. 
        """
        page = GetRandomPage()
        self.assertNotEqual(page.title, "")
        self.assertNotEqual(page.body, "")


    def test_GetRandomTitles(self):
        """
        Get a list of titles and check that the
        expected number is returned and that none
        of them are empty or None. 
        """
        titles = GetRandomTitles(2)
        self.assertEqual(len(titles), 2)
        self.assertNotIn(None, titles)
        self.assertNotIn("", titles)


    def test_GetChildPages(self):
        """
        Gets a random page and them attempts to get
        all the children of the page. 
        """
        page = WikipediaPage("https://en.wikipedia.org/wiki/Scenic_Hot_Springs")
        children = page.GetAllChildPages()


    def test_BodyAsNGrames(self):
        """
        Creates 1-grams from a sample page.
        """
        page = WikipediaPage("https://en.wikipedia.org/wiki/Scenic_Hot_Springs")
        page.BodyAsNGrames(1)



if __name__ == '__main__':
    unittest.main()