from problems.first_problem.room import Room


class HotelRoomBooking:
    def __init__(self, floors, room_per_floor):
        self.hotel_rooms = {
            f"{floor}{room_alphabet}": Room(f"{floor}{room_alphabet}")
            for floor in range(1, floors+1)
            for room_alphabet in "ABCDE"[:room_per_floor]
        }

        self.hotel_rooms = {f"{floor}{room_letter}": Room(f"{floor}{room_letter}")
                            for floor in range(1, floors + 1)
                            for room_letter in "ABCDE"[:rooms_per_floor]}
