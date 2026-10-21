class Publication:
  def __init__(self, title: str, author: str):
    self._title = title
    self._author = author

  @property
  def get_title(title):
    return self._title

  @property
  def get_author(author):
    return self.author

class Book(Publication):
  def __init__(self, title: str, author: str, numpages: int):
    super().__init__(title, author)
    self._numpages = numpages

  @pagesetter
  

