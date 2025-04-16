class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time

class FlightStack:
    def __init__(self):
        self.stack = []

    def push(self, flight):
        self.stack.append(flight)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class AirportFlightManagementSystem:
    def __init__(self):
        self.flight_stack = FlightStack()

    def display_menu(self):
        print("Airport Flight Management System")
        print("1. Add Flight")
        print("2. Remove Flight")
        print("3. Display Flights")
        print("4. Search Flight")
        print("5. Update Flight")
        print("6. Print Flight Ticket")
        print("7. Exit")

    def add_flight(self):
        flight_number = input("Enter flight number: ")
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        arrival_time = input("Enter arrival time: ")
        flight = Flight(flight_number, origin, destination, departure_time, arrival_time)
        self.flight_stack.push(flight)
        print("Flight added successfully!")

    def remove_flight(self):
        if not self.flight_stack.is_empty():
            flight = self.flight_stack.pop()
            print(f"Flight {flight.flight_number} removed successfully!")
        else:
            print("No flights to remove.")

    def display_flights(self):
        if not self.flight_stack.is_empty():
            print("Flights:")
            for flight in self.flight_stack.stack:
                print(f"Flight {flight.flight_number}: {flight.origin} -> {flight.destination}, Departure: {flight.departure_time}, Arrival: {flight.arrival_time}")
        else:
            print("No flights to display.")

    def search_flight(self):
        flight_number = input("Enter flight number to search: ")
        for flight in self.flight_stack.stack:
            if flight.flight_number == flight_number:
                print(f"Flight {flight_number} found!")
                print(f"Origin: {flight.origin}, Destination: {flight.destination}, Departure: {flight.departure_time}, Arrival: {flight.arrival_time}")
                return
        print("Flight not found.")

    def update_flight(self):
        flight_number = input("Enter flight number to update: ")
        for flight in self.flight_stack.stack:
            if flight.flight_number == flight_number:
                origin = input("Enter new origin: ")
                destination = input("Enter new destination: ")
                departure_time = input("Enter new departure time: ")
                arrival_time = input("Enter new arrival time: ")
                flight.origin = origin
                flight.destination = destination
                flight.departure_time = departure_time
                flight.arrival_time = arrival_time
                print("Flight updated successfully!")
                return
        print("Flight not found.")

    def print_flight_ticket(self):
        if not self.flight_stack.is_empty():
            flight = self.flight_stack.peek()
            print("Flight Ticket:")
            print(f"Flight Number: {flight.flight_number}")
            print(f"Origin: {flight.origin}")
            print(f"Destination: {flight.destination}")
            print(f"Departure Time: {flight.departure_time}")
            print(f"Arrival Time: {flight.arrival_time}")
        else:
            print("No flights to print ticket for.")

    def run(self):
        while True:
            self.display_menu()
            option = input("Enter option: ")
            if option == "1":
                self.add_flight()
            elif option == "2":
                self.remove_flight()
            elif option == "3":
                self.display_flights()
            elif option == "4":
                self.search_flight()
            elif option == "5":
                self.update_flight()
            elif option == "6":
                self.print_flight_ticket()
            elif option == "7":
                print("Exiting system.")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    system = AirportFlightManagementSystem()
    system.run()