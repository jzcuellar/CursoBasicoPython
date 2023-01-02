"""
Description:

You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. We want to 
create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names
of people that like an item. It must return the display text as 
shown in the examples:


[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


"""

## Ejecutar Solo 1 Funcion que son soluciones unicas del problema 

##  SOLUCION #1 - Solucion Creada Por mi 

def likes(names):
    if len(names)<1:
        return 'no one likes this'
    elif len(names)==1:
        return (f'{names[0]} likes this')
    elif len(names)==2:
        return (f'{names[0]} and {names[1]} like this')
    elif len(names)==3:
        return (f'{names[0]}, {names[1]} and {names[2]} like this')
    else:
        return (f'{names[0]}, {names[1]} and {len(names)-2} others like this')

##  SOLUCION #2 - https://www.codewars.com/kata/reviews/564425cc55d0e45b8c000087/groups/587d40312ec7b84b2f00102f

def likes(names):

    d = { #1
        0: "no one likes this",
        1: "{} likes this", #2
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)

    return d[min(4, length)].format(*names, others = length - 2) #4 #5 #6
    
    ##1  Make a dictionary d of all the possible answers. 
    #    Keys are the respective number of people who liked it.
    
    ##2  {} indicate placeholders. They do not need any numbers but are simply 
    #    replaced/formatted in the order the arguments in names are given to format
    # 
    ##3  {others} can be replaced by other value; below the argument "others = length - 2"
    #    is passed to str.format()

    ##4  d[min(4, length)] insures that the appropriate string is called from the dictionary
    #    and subsequently returned. Min is necessary as len(names) may be > 4
    #    funtion min(list or dictionary) returns the minimum value

    ##5  The * in *names ensures that the list names is blown up and that format is called
    #    as if each item in names was passed to format individually, i. e.
    #
    ##6  format(names[0], names[1], .... , names[n], others = length - 2
