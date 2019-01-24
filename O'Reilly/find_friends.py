from functools import reduce

def check_connection(network, first, second):

    unique_drones = [i.split('-') for i in network]
    unique_drones = reduce(lambda x,y: x+y, unique_drones)
    unique_drones = set(unique_drones)
    direct_friends = {name: [] for name in unique_drones}

    for drone in unique_drones:
        for connection in network:
            two_drones_in_connection = connection.split('-')
            if drone in two_drones_in_connection:
                direct_friends[drone].append(*[i for i in two_drones_in_connection if i != drone])

    first_net = set([first] + direct_friends[first])

    connection_heap = [[k] + v for k,v in direct_friends.items()]
    ##Below is to make sure that all connections are checked against eachother
    ##If we only pass through once then only the closest neighbors might get discovered
    for _ in connection_heap:
        for heap in connection_heap:
            if len(first_net.union(heap)) < (len(heap) + len(first_net)):
                first_net = first_net.union(heap)

    return_flag = False

    if second in first_net:
        return_flag = True

    return return_flag

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."