#For the mission "How to find friends" , it’s nice to have access to a specially
#made data structure. In this mission we will realize a data structure which we
#will use to store and work with a friend network.
#
#The class "Friends" should contains names and the connections between them.
#Names are represented as strings and are case sensitive. Connections are
#undirected, so if "sophia" is connected with "nikola", then it's also correct
#in reverse.
#
#class Friends(connections)
#
#Returns a new Friends instance. "connections" is an iterable of sets with two
#elements in each. Each connection contains two names as strings. Connections
#can be repeated in the initial data, but inside it's stored once. Each
#connection has only two states - existing or not.
#
#>>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})) Friends([{"1",
#>>> "2"}, {"3", "1"}])
#
#
#add(connection)
#
#Add a connection in the instance. "connection" is a set of two names (strings).
#Returns True if this connection is new. Returns False if this connection exists
#already.
#
#>>> f = Friends([{"1", "2"}, {"3", "1"}]) f.add({"1", "3"})
#False
#>>> f.add({"4", "5"})
#True
#
#
#remove(connection)
#
#Remove a connection from the instance. "connection" is a set of two names
#(strings). Returns True if this connection exists. Returns False if this
#connection is not in the instance.
#
#>>> f = Friends([{"1", "2"}, {"3", "1"}]) f.remove({"1", "3"})
#True
#>>> f.remove({"4", "5"})
#False
#
#
#names()
#
#Returns a set of names. The set contains only names which are connected with
#somebody.
#
#>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"})) f.names()
#{"a", "b", "c", "d"}
#>>> f.remove({"d", "c"})
#True
#>>> f.names()
#{"a", "b", "c"}
#
#
#connected(name)
#
#Returns a set of names which is connected with the given "name". If "name" does
#not exist in the instance, then return an empty set.
#
#>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})) f.connected("a")
#{"b", "c"}
#>>> f.connected("d")
#set()
#>>> f.remove({"c", "a"})
#True
#>>> f.connected("c")
#{"b"}
#>>> f.remove({"c", "b"})
#True
#>>> f.connected("c")
#set()
#
#
#In this mission all data will be correct and you don't need to implement value
#checking.
#
#Input: Statements and expression with the Friends class.
#
#Output: The behaviour as described.
#
#Precondition: All data is correct.

class Friends:
    def __init__(self, connections):
        raise NotImplementedError

    def add(self, connection):
        raise NotImplementedError

    def remove(self, connection):
        raise NotImplementedError

    def names(self):
        raise NotImplementedError

    def connected(self, name):
        raise NotImplementedError



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
