import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight", 
                "Guy Lashbaugh", "Ginger Schlossman", "Suellen Luaces", "Jamey Kirchgesler",
                "Amiee Elwer", "Lacresha Peet", "Leonia Goretti", "Carina Bunge",
                "Renee Brendeland", "Andrew Mcgibney", "Gina Degon", "Deandra Pihl",
                "Desmond Steindorf", "Magda Growney", "Ivy Hall", "Tammi Todman",
                "Harley Mussell", "Iola Bordenet", "Alex White", "Myles Deanne",
                "Elden Dohrman", "Ira Hooghkirk", "Eileen Stigers", "Mariann Melena",
                "Maryrose Badura", "Ardelia Koffler", "Lacresha Kempker",
                "Charlyn Singley", "Lekisha Tawney", "Christena Botras",
                "Mike Blanchet", "Cathryn Hinkson", "Emma Lewis", "Mavis Bhardwaj", "Sung Filipi", "Keiko Dedeke", "Lorelei Morrical", "Jimmie Lessin", "Adrianne Hercules", "Latrisha Haen", "Denny Friedeck", "Emmett Whitesell", "Sina Sauby", "Melony Engwer", "Alina Reichel", "Rosamond Shawe", "Elinore Benyard", "Sang Bouy", "Ed Aparo", "Sheri Wedding", "Sang Snellgrove", "Shaquana Sones", "Elvia Motamed", "Candice Lucey", "Sibyl Froeschle", "Ray Spratling", "Cody Mandeville", "Donita Cheatham", "Darren Later", "Johnnie Stivanson", "Enola Kohli", "Leann Muccia", "Carey Philps", "Suellen Tohonnie"]

def binary_search(collection, target):
    first = 0
    last = len(collection) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

for n in search_names:
    index = binary_search(names, n)
    print(index)



