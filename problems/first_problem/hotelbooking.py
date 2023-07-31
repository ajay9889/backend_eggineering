from problems.first_problem.room import Room
from problems.first_problem.roomstatus import RoomStatus


class HotelRoomBooking:
    def __init__(self, floors, room_per_floor):
        self.hotel_rooms = {
            f"{floor}{room_alphabet}": Room(f"{floor}{room_alphabet}")
            for floor in range(1, floors+1)
            for room_alphabet in "ABCDE"[:room_per_floor]
        }

    @staticmethod
    def getdistance_room(room_number):
        # for example the room number 2A, the floor will be 2 and room letter will be A and the calculate the ASCI value from the letter
        floor, room_letter = int(room_number[:-1]), room_number[-1]
        return (floor - 1) * 5 + ord(room_letter) - ord('A')

    def find_nearest_available_room(self):
        # the all available room first
        availableroom = [
            room for room in self.hotel_rooms.values() if room.is_available()]
        # find the minimum distance available from the enterance.
        return min(availableroom, key=lambda room: self.getdistance_room(room.room_number))

    # create the function, A method to request room assignment, which will reply with the assigned room number upon success

    def request_room_assignment(self, guest_name):
        nearestroom = self.find_nearest_available_room()
        nearestroom.change_status(RoomStatus.Occupied)
        print(f"Room {nearestroom.room_number} assigned to {guest_name}")
        return nearestroom.room_number

    # A method to check out of a room (Vacant)

    def checkout(self, room_number):
        room = self.hotel_rooms.get(room_number)
        if room:
            room.change_status(RoomStatus.Vacant)
            print(
                f"Room {room_number} has been checkout out and mark checkout i.e vacant")
        else:
            print(f"Room {room_number} is not found")

    # A method to mark a room cleaned (Available).

    # A method to mark a room for out of service (Repair).

    # A method to mark a room as repaired (Vacant).

    # A method to list all the available rooms.
