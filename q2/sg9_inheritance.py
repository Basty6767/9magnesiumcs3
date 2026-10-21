class Publication: #Defines a class called Publication
  def __init__(self, title: str, author: str): #The initializer method that runs automaticallly when a new Publication is created.  
    self._title = title #Assigns the title parameter to the _title attribute of the Publication object.
    self._author = author #Assigns the author parameter to the _author attribute of the Publication object.

  @property #A decorator that allows the get_title method to be accessed like an attribute.
  def get_title(self): 
    return self._title #Returns the value of the _title attribute of the Publication object.

  @property #A decorator that allows the get_author method to be accessed like an attribute.
  def get_author(self):
    return self._author #Returns the value of the _author attribute of the Publication object.

class Book(Publication): #Defines a class called Book that inherits from Publication
  def __init__(self, title: str, author: str, numpages: int): #The initializer method that runs automatically when a new Book is created. It takes three parameters, which are title, author, and numpages.
      super().__init__(title, author) #Calls the initializer method of the parent class (Publication) to initialize the title and author attributes of the Book object.
      self._numpages = numpages #Assigns the numpages parameter to the _numpages attribute of the Book object.

  @property #A decorator that allows the numpages method to be accessed like an attribute.
  def numpages(self): 
    return self._numpages #Returns the value of the _numpages attribute of the Book object.

  @numpages.setter #A decorator that allows the numpages attribute to be set with a new value.
  def numpages(self, numpages): #Sets the value of the _numpages attribute of the Book object to the new value passed as a parameter. It also checks if the new value is positive, and if not, it prints an error message.
    if numpages <= 0:
      print("The number of pages must be positive.")
    else:
      self._numpages = numpages #Assigns the new value to the _numpages attribute of the Book object.
    

class Magazine(Publication): #Defines a class called Magazine that inherits from Publication
  def __init__(self, title: str, author: str, issue_number: int): #The initializer method that runs automatically when a new Magazine is created. It takes three parameters, which are title, author, and issue_number.
        super().__init__(title, author)  #Calls the initializer method of the parent class (Publication) to initialize the title and author attributes of the Magazine object.
        self._issue_number = issue_number #Assigns the issue_number parameter to the _issue_number attribute of the Magazine object.
    
  
  @property #A decorator that allows the issue_number method to be accessed like an attribute.
  def get_issue_number(self):
    return self._issue_number #Returns the value of the _issue_number attribute of the Magazine object.
  
  @get_issue_number.setter #A decorator that allows the issue_number attribute to be set with a new value.
  def issue_number(self, issue_number: int): #Sets the value of the _issue_number attribute of the Magazine object to the new value passed as a parameter. It also checks if the new value is positive, and if not, it prints an error message.
    if issue_number <= 0:
      print("The issue number must be a positive integer.")
    else:
      self._issue_number = issue_number #Assigns the new value to the _issue_number attribute of the Magazine object.
      

pub1 = Publication("The Great Gatsby", "F. Scott Fitzgerald") #Creates a new Publication object called pub1 with the title "The Great Gatsby" and the author "F. Scott Fitzgerald".
print("Publication Information:") #Prints a header for the publication information.
print(f"Title: {pub1.get_title}") #Prints the title of the publication using the get_title property of the pub1 object.
print(f"Author: {pub1.get_author}") #Prints the author of the publication using the get_author property of the pub1 object.

book1 = Book("Strike the Zither", "Joan He", 348) #Creates a new Book object called book1 with the title "Strike the Zither", the author "Joan He", and 348 pages.
print("\nBook Information:") #Prints a header for the book information.
print(f"Title: {book1.get_title}") #Prints the title of the book using the get_title property of the book1 object.
print(f"Author: {book1.get_author}") #Prints the author of the book using the get_author property of the book1 object.
print(f"Number of Pages: {book1.numpages}") #Prints the number of pages in the book using the numpages property of the book1 object.

mag1 = Magazine("National Geographic", "Various Authors", 202) #Creates a new Magazine object called mag1 with the title "National Geographic", the author "Various Authors", and issue number 202.
print("\nMagazine Information:") #Prints a header for the magazine information.
print(f"Title: {mag1.get_title}") #Prints the title of the magazine using the get_title property of the mag1 object.
print(f"Author: {mag1.get_author}") #Prints the author of the magazine using the get_author property of the mag1 object.
print(f"Issue Number: {mag1.get_issue_number}") #Prints the issue number of the magazine using the get_issue_number property of the mag1 object.