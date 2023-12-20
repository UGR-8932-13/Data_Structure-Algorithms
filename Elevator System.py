import heapq
class Elevator:
    def __init__(self, capacity, current_floor):
        self.capacity = capacity
        self.current_floor = current_floor
        self.passengers = []
    
    def __repr__(self):
        return f"Elevator({self.capacity}, {self.current_floor}, {self.passengers})"
    
    def has_space(self):
        return len(self.passengers) < self.capacity
    
    def add_passenger(self, floor):
        self.passengers.append(floor)
        print(f"Added passenger to elevator at floor {self.current_floor}")
        
    def remove_passenger(self):
        if self.passengers:
            floor = self.passengers.pop(0)
            print(f"Removed passenger from elevator at floor {self.current_floor}")
            return floor
        else:
            return None

class ElevatorSystem:
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.elevators = [Elevator(10, 0) for _ in range(num_elevators)]
        self.requests = []
    
    def __repr__(self):
        return f"ElevatorSystem({self.num_floors}, {self.elevators})"
    
    def request_elevator(self, floor):
        heapq.heappush(self.requests, (floor, 0))
        print(f"Elevator requested at floor {floor}")
        self._process_requests()
    
    def _process_requests(self):
        while self.requests:
            request = heapq.heappop(self.requests)
            floor = request[0]
            elevator = self._get_nearest_elevator(floor)
            elevator.add_passenger(floor)
            destination = int(input("Enter destination floor: "))
            heapq.heappush(self.requests, (destination, elevator.current_floor))
            elevator.add_passenger(destination)
            self._move_elevator(elevator, destination)
    
    def _get_nearest_elevator(self, floor):
        best_elevator = None
        closest_distance = float('inf')
        for elevator in self.elevators:
            if elevator.has_space():
                distance = abs(elevator.current_floor - floor)
                if distance < closest_distance:
                    best_elevator = elevator
                    closest_distance = distance
        return best_elevator
    
    def _move_elevator(self, elevator, destination):
        while elevator.current_floor != destination:
            if elevator.current_floor < destination:
                elevator.current_floor += 1
            else:
                elevator.current_floor -= 1
            print(f"Elevator moving to floor {elevator.current_floor}")
            for request in self.requests:
                if request[0] == elevator.current_floor and request[1] == destination:
                    self.requests.remove(request)
        elevator.remove_passenger()
        elevator.remove_passenger()

elevator_system = ElevatorSystem(10, 3)

elevator_system.request_elevator(2)


