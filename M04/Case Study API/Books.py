



class books():
    def __init__(self, idn, name, author, publisher):
        self.idn = idn
        self.name = name
        self.author = author
        self.publisher = publisher
        
        def __eq__(self, other):
            if isinstance(other, books):
                return (self.author == other.author)
       
        
    def __repr__(self):
        return f'{self.name} is created by {self.author} and is published by, {self.publisher}'
        