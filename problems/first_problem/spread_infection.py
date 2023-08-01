def adjacent_rooms(hotel, row, col):
    adjacent = []
    # Move Left
    if row > 0:
        adjacent.append((row - 1, col))
    # Move Right
    if row < len(hotel) - 1:
        adjacent.append((row + 1, col))
    # Move Up
    if col > 0:
        adjacent.append((row, col - 1))
    # Move Down
    if col < len(hotel[0]) - 1:
        adjacent.append((row, col + 1))
    return adjacent


def get_initial_infected_rooms(hotel):
    # Adding here all vertices as tuple in list (row, col) format which is going to be stored into the infected_rooms
    infectedrooms = []
    for row in range(len(hotel)):
        for col in range(len(hotel[0])):
            if hotel[row][col] == 2:
                infectedrooms.append((row, col))
    return infectedrooms


def get_all_infected_amount_of_time(hotel):
    # Check if empty guests, then the infect all is 0
    if not hotel or not hotel[0]:
        return "0"
    infected_rooms = get_initial_infected_rooms(hotel)
    # No initial infection, so all guests cannot be infected
    if not infected_rooms:
        return "-1"
    time = 0
    while infected_rooms:
        new_infected_rooms = []
        for row, col in infected_rooms:
            for adj_row, adj_col in adjacent_rooms(hotel, row, col):

                if hotel[adj_row][adj_col] == 1:
                    hotel[adj_row][adj_col] = 2
                    new_infected_rooms.append((adj_row, adj_col))
        infected_rooms = new_infected_rooms
        time += 1
    if any(1 in row for row in hotel):
        return "-1"
    return str(time)

