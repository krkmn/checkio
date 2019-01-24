class Friends:
    def __init__(self, connections):
        if isinstance(connections, list):
            connections = tuple(connections)
        self.connections = connections

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            if isinstance(self.connections, set):
                self.connections = (self.connections,) + (connection,)
            else:
                self.connections = self.connections + (connection,)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections = tuple(x for x in self.connections if x != connection)
            return True
        else:
            return False

    def names(self):
        all_names = [element for mini in self.connections for element in mini]

        return set(all_names)

    def connected(self, name):
        connected = set()

        for mini in self.connections:
            if name in mini:
                connected = connected.union(element for element in mini if element != name)

        return connected



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
