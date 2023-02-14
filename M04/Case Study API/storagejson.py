from Books import books


booklist = [
    books(0,"testname","testauthor","testpublisher"),
    books(1,"Mazerunner","James Dashner","Delacorte Press"),
    books(2,"Enders game","Orson Scott Card","Tor Books")]

#### json

import json

with open('bookcontainer3.json', "w") as toFile:
    for b in booklist:
        toFile.write(json.dumps({"idn": b.idn, "name": b.name, "author": b.author, "publisher": b.publisher}) + "\n")
