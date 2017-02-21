def mark_level(self, level, soup):
    '''
    Mark every node with a level num (0 - n)
    :param soup: a BeautifulSoup object
    '''
    soup.level = level
    if soup.contents.__len__() > 0:
        for child in soup.children:
            self.mark_level(level + 1, child)
