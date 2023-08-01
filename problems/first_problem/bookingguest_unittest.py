
'''
import all required dependancy
'''
from spread_infection import get_all_infected_amount_of_time
from hotelbooking import HotelRoomBooking

# Unit test


def run_unittest_part1():
    hotel_manager = HotelRoomBooking(floors=3, room_per_floor=5)
    # step1 make occupied by asssigning the room to the specific persons
    assert hotel_manager.request_room_assignment("John")
    assert hotel_manager.request_room_assignment("Allen")
    assert hotel_manager.request_room_assignment("Alex")
    assert hotel_manager.request_room_assignment("Sam")

    # Available rooms: 1E, 2A, 2B, 2C, 2D, 2E, 3A, 3B, 3C, 3D, 3E
    hotel_manager.list_available_rooms()

    # Mark room 1A out of service
    # John as guest need to checkout from room 1A and then mark for out of service
    hotel_manager.checkout_room("1A")
    hotel_manager.mark_room_out_of_service("1A")

    hotel_manager.checkout_room("1C")
    hotel_manager.mark_room_cleaned("1C")

    assert hotel_manager.request_room_assignment("Michael")

    hotel_manager.mark_room_cleaned("1A")
    assert hotel_manager.request_room_assignment("Sara")
    hotel_manager.list_available_rooms()
    hotel_manager.checkout_room("1B")
    hotel_manager.mark_room_cleaned("1B")
    assert hotel_manager.request_room_assignment("David")
    hotel_manager.list_available_rooms()

    hotel_manager.mark_room_out_of_service("2B")
    hotel_manager.mark_room_repaired("2B")
    hotel_manager.list_available_rooms()
    hotel_manager.checkout_room("2D")
    # Non-existent room
    hotel_manager.list_available_rooms()
    hotel_manager.checkout_room("3A")
    hotel_manager.mark_room_cleaned("3C")

    hotel_manager.list_available_rooms()

    hotel_manager.mark_room_cleaned("1B")
    hotel_manager.list_available_rooms()

    hotel_manager.checkout_room("3D")
    hotel_manager.list_available_rooms()
    hotel_manager.mark_room_repaired("1C")
    # Room 1C is not under repair


if __name__ == "__main__":
    # Question 1: Part 1
    print("\n", "-----------Question1: Part1------------------", "\n")
    run_unittest_part1()

    # Question 1: Part 2 to get infected rooms amount of time
    hotel_matrix = [[2, 1, 0, 2, 1],
                    [2, 2, 0, 2, 2],
                    [2, 2, 2, 2, 2]]
    print("\n", "-----------Question1: Part2------------------", "\n")
    print("Infected Room Amount Of Time: ",
          get_all_infected_amount_of_time(hotel_matrix))
