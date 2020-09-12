

class Movie:
    def __init__(self, title, director, cast, length):
        self.title = title
        self.director = director
        self.cast = cast
        self.length = length
        self.rating = -1

    def get_info(self):
        return 'title: %s ; director: %s ; cast: %s ; length: %d ; rating: %d' % (self.title, self.director, self.cast, self.length, self.rating)
        
    def __str__(self):
        return 'title: %s ; director: %s' % (self.title, self.director)


class DLLNode:
    def __init__ (self, item , prev, next):
        self.item = item
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return 'movie: %s' % self.item
    
class DLinkedList:
    def __init__(self):
        self.head = DLLNode(None,None,None)
        self.tail = DLLNode(None,self.head,None)
        self.head.next = self.tail
        self.size=0

    def add_after(self, item, before):
        if (self.size==0):
            return None
        else:
            node=DLLNode(item, before, before.next)
            before.next=item 
            before.next.prev=item 
            self.size+=1
            return node
        
    def add_first(self, item):
        node=DLLNode(item, self.head, self.head.next)
        self.head.next.prev=node
        self.head.next=node
        self.size+=1
        return node

    def add_last(self, item):
        node=DLLNode(item,self.tail.prev, self.tail)
        self.tail.prev.next=node
        self.tail.prev=node
        self.size+=1
        return node

    def get_first(self):
        return self.head.next

    def get_last(self):
        return self.tail.prev

    def remove_node(self, node):
        if self.size == 0 :
            return None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.item = None
            node.next = None
            self.size-=1

    def remove_first(self):
        return self.remove_node(self.head.next)

    def remove_last(self):
        return self.remove_node(self.tail.prev)

class PyFlix:
    def __init__(self):
        self.library = DLinkedList()
        self.current = None

    def add_movie(self,movie):
        node = self.library.add_last(movie)
        return node

    def get_current(self):
        if self.current == None or self.current.item == None:
            return None
        else:
            return self.current.item

    def next_movie(self):
        if self.library != 0:
            if self.current == None:
                self.current = self.library.head.next
            elif self.current.next != self.library.tail:
                self.current = self.current.next
            else:
                self.current = self.library.head.next
            return self.current
    
    def prev_movie(self):
        if self.library != 0:
            if self.current == None:
                self.current = self.library.tail.prev
            elif self.current.prev != self.library.head:
                self.current = self.current.prev
            else:
                self.current = self.library.tail.prev
            return self.current
        
    def reset(self):
        if self.library.size != 0:
            self.current = self.library.head

    def rate(self):
        if (self.current != None and self.length() != 0):
            while True:
                userInput = input("Enter your rating[0 to 4]:")
                castInput = int(userInput)
                if castInput <= 4 and castInput >= 0:
                    self.current.item.rating = castInput
                    print("Your rating is %s" % (castInput))
                    return
                else:
                    print("Please enter valid input.")

    def info(self):
        if self.length() != 0:
            if self.current.item.rating != -1:
                print(self.current.item.get_info())
            else:
                print('title: %s ; director: %s ; cast: %s ; length: %d' % (self.current.item.title, self.current.item.director, self.current.item.cast, self.current.item.length))
        

    def remove_current(self):
        if self.library != 0 and self.current != None:
            temp = self.current
            if temp.next == self.library.tail:
                self.current = self.library.get_first()
            else:
                self.current = temp.next
            self.library.remove_node(temp)

    def length(self):
        return self.library.size

    def __str__(self):
        node = self.library.head
        output = ""
        while node:
            if node.item != None:
                if self.current == node:
                    output += "--> " + str(self.current.item) + "\n"
                else:
                    output += str(node.item) + "\n"
            node = node.next
        return output
                
    def search(self, word):
        if self.length() != 0:
            found = False
            counter = 0
            if self.current != None:
                node = self.current.next
            else:
                node = self.library.head.next
            while found == False:
                if node == self.library.tail:
                    node = self.library.head.next
                if word.lower() in node.item.get_info().lower():
                    self.current = node
                    found = True
                    print(node.item.get_info())
                    return node
                if node == self.current:
                    print('No matching movie')
                    return node
                if counter == self.length():
                    return node
                counter += 1
                node = node.next

if __name__ == "__main__":

    mylib = PyFlix()
    print("Adding movies \n")
    movie1 = Movie("El Camino", "Vince Gilligan", "Aaron Paul", 122)
    movie2 = Movie("Joker", "Todd Phillips", "Joaquin Phoenix", 122)
    movie3 = Movie("Midsommar", "An Aster", "Florence Pugh", 138)
    mylib.add_movie(movie1)
    mylib.add_movie(movie2)
    mylib.add_movie(movie3)
    print("Library:")
    print(mylib)
    print("movie 4 added \n")
    movie4 = Movie("Hustlers", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
    mylib.add_movie(movie4)
    print("Library:")
    print(mylib)
    print("Getting next movie:")
    mylib.next_movie()
    mylib.get_current()
    print("Getting previous movie:")
    mylib.prev_movie()
    mylib.get_current()
    mylib.prev_movie()
    mylib.prev_movie()
    mylib.prev_movie()
    mylib.prev_movie()
    mylib.next_movie()
    mylib.next_movie()
    mylib.next_movie()
    mylib.next_movie()
    print("Library:")
    print(mylib)
    print(mylib.length())
    mylib.info()
    mylib.rate()
    mylib.info()
    mylib.search("harry potter")
    mylib.search("joker")
    movie5= Movie("AAA", "BBB", "CCC", 110)
    mylib.add_movie(movie5)
    print(mylib)
    mylib.prev_movie()
    print(mylib)
    mylib.remove_current()
    print(mylib)
    mylib.remove_current()
    print(mylib)
    movie6 = Movie("rrrrrrrrrrrrrrr", "Lorene Scafaria", "Constance Wu, Jennifer Lopez", 110)
    mylib.add_movie(movie6)
    print(mylib)
   
