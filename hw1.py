"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data 


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    #  this takes a word and then counts each vowel
    #  the word is a string that is given
    #  the output is a number from the funtion where it counts each vowel
    #  It Goes through all letters in the text, scanning for capital or noncaptial vowels and accumulating a total.
    VowelTotal = 0
    if text == []:
            return ([])
    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            VowelTotal += 1
    return (VowelTotal)

print(vowel_count("Kyle RIchardson"))


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # Purpose: To get only lists containing two items
    # Input(s): A list of lists with a variety of different values
    # Output: The output is a list of lists only containing from the input any list that has two items inside of it.
    shortList= []
    for i in range(len(items)):
        if len(items[i]) == 2 :
            shortList.append(items[i])
    return (shortList)




# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    #Purpose: To reorder lists that contain two items so they are in the proper order
    #Input(s): You input a list of lists that could contain a variety of response
    # Output: that same lists of lists, with any lists containing two items having their items be in ascending order.
    ascending_list = []
    for i in range(len(items)):
            if len(items[i]) == 2:
                if items[i][0] <= items[i][1]:
                    ascending_list.append([items[i][0],items[i][1]])    
                else:
                    ascending_list.append([items[i][1],items[i][0]])
            else:
                ascending_list.append(items[i])   
    return (ascending_list)
    

# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # Purpose: Adds together two different prices to get a combined total
    # Input(s): two different amount of money. In each amount there is a dollar total and cent total
    # Output: Combines the two amounts, and if the cent amount would add to over 100, rolls it over to the next dollar amount
    dollar_total = 0
    cent_total = 0
    cent_total = first.cents + second.cents
    dollar_total = first.dollars + second.dollars
    if first.cents + second.cents >= 100:
        cent_total = abs (100 - (first.cents + second.cents))
        dollar_total += 1
        price_total = dollar_total + (cent_total/100) 
        return (price_total)
    else:
        cent_total = first.cents + second.cents
        price_total = dollar_total + (cent_total/100) 
    return (price_total)

# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # Purpose: Given two points this allows you to find the area built by the rectangle the two points make
    # Input(s): Two points with each having an x and y point.
    # Output: An area given by the points.
    width = abs (rectangle.top_left.x - rectangle.bottom_right.x)
    height = abs (rectangle.top_left.y - rectangle.bottom_right.y) 
    area = height * width
    return (area)

    


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # Purpose: To find all books by an author in a list of books that contain the authors name and the title of a book
    # Input(s): An authors name, along with a string of author names+ a book they wrote.
    # Output: Every book title in the list by the desired author
   
    author_list = []
    for i in range(len(books)):
        if author in books[i].authors:
            author_list.append(books[i].title)
    return (author_list)
        
  


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # Purpose: To find the smallest circle that would have the same center as a rectangle and its side would touch the corners of the circle.
    # Input(s): Two Points in an (x,y) fashion
    # Output: the radius of the circle and the center of the circle
    radius = (((rectangle.top_left.x - rectangle.bottom_right.x)**2 + (rectangle.top_left.y - rectangle.bottom_right.y)**2)**0.5)/2
    center = (((rectangle.top_left.x+rectangle.bottom_right.x)/2),(rectangle.top_left.y + rectangle.bottom_right.y)/2)
    return(radius,center)

    #This is code below that i did because I read the prompt wrong for the circle function, but this I believe gives the smallest circle inside of a square I just don't want to delete it because I worked on it so I thought I would leave it in here as a comment
        #if rectangle.top_left.x < rectangle.bottom_right.x and rectangle.top_left.y < rectangle.bottom_right.y:
            #if rectangle.top_left.x < rectangle.top_left.y:
                #radius = (((rectangle.top_left.x+rectangle.bottom_right.x)/2)+rectangle.top_left.x)
            #else:
                #radius = (((rectangle.top_left.y + rectangle.bottom_right.y)/2)+rectangle.top_left.y)
        #elif rectangle.top_left.x > rectangle.bottom_right.x and rectangle.top_left.y > rectangle.bottom_right.y:
            #if rectangle.bottom_right.x < rectangle.bottom_right.y:
                #radius = (((rectangle.top_left.x+rectangle.bottom_right.x)/2)+rectangle.bottom_right.x)
           # else:
                #radius = (((rectangle.top_left.y + rectangle.bottom_right.y)/2)+rectangle.bottom_right.y)
    

# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # Purpose: find the average pay of the employees and see who is not making at least the average
    # Input(s): There is a list of Employees, which contains data about their name, along with their pay rate.
    # Output: the list of names of employees who are paid under the average
    name_list = []
    total = 0
    avg = 0
    if employees == []:
        return ([])
    for i in range(len(employees)):
        total += employees[i].pay_rate
    avg = total /len(employees)
    for i in range(len(employees)):
        if employees[i].pay_rate < avg:
            name_list.append(employees[i].name)
            return(name_list)
