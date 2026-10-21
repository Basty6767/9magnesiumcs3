class Publication:
  def __init__(self, title: str, author: str):
    self._title = title
    self._author = author

  @property
  def get_title(self):
    return self._title

  @property
  def get_author(self):
    return self.author

class Book(Publication):
  def __init__(self, title: str, author: str, numpages: int):
    super().__init__(title, author)
    self._numpages = numpages

  @pagesetter
  def set_numpages(self, numpages):
    if numpages < 0:
      print("The number of pages must be positive.")

