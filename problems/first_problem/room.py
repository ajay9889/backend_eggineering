
from problems.first_problem.roomstatus import RoomStatus
class Room:
    def __init__(self, room_number):
        self.room_number    = room_number
        self.status         = RoomStatus.Available

    def change_status(self, newstatus):
        self.status         = newstatus
        
    def is_available(self):
        return self.status == RoomStatus.Available
    

        