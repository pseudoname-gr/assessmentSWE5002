import heapq
import random
import string



class AircraftSimulation:

    """
    Simulates air traffic control management for aircraft takeoff and landing requests.

    Landing Queue:
    - Data Structure: Priority Queue (implemented using heapq)
    - Description: This queue stores tuples representing landing requests. Each tuple contains:
        Priority: An integer representing the priority of the request (0 for emergency landing, 1 for regular landing).
        Flight Number: An integer representing the flight number.
        Call Sign: A string representing the call sign of the aircraft.

    Takeoff Queue:
    - Data Structure: FIFO Queue (implemented using a list)
    - Description: This queue stores tuples representing takeoff requests. Each tuple contains:
        Flight Number: An integer representing the flight number.
        Call Sign: A string representing the call sign of the aircraft.

    Attributes:
    - landing_queue: A priority queue to store landing requests.
    - takeoff_queue: A FIFO queue to store takeoff requests.

    Methods:
    - generate_call_sign(): Generates a random call sign for an aircraft. Picks one out of three.
    - add_request(): Randomly adds landing or takeoff requests to the respective queues.
    - process_requests(): Processes landing and takeoff requests, handling emergency landings with higher priority.

    At the end of the source code:
    - Create an instance of the class, AircraftSimulation.
    - Use the add_request method to add landing or takeoff requests.
    - Call the process_requests method to simulate the air traffic control management.
    """
    
    def __init__(self):
        self.landing_queue = []  # Priority queue for landing requests
        self.takeoff_queue = []  # FIFO queue for takeoff requests

    @staticmethod # Can be called directly from the class without creating the class instance, so we can generate call signs as we please
    def generate_call_sign():
        # Randomly choose the type of call sign
        call_sign_type = random.choice(['a', 'b', 'c'])

        if call_sign_type == 'a':
            # Type 'a' - registration marking only
            registration_marking = ''.join(random.choices(string.ascii_uppercase, k=5))
            return registration_marking
        elif call_sign_type == 'b':
            # Type 'b' - telephony designator + last 4 characters of registration marking
            telephony_designator = ''.join(random.choices(string.ascii_uppercase, k=3))
            registration_marking = ''.join(random.choices(string.ascii_uppercase, k=5))
            return f"{telephony_designator}{registration_marking[-4:]}"
        else:
            # Type 'c' - telephony designator + flight identification
            telephony_designator = ''.join(random.choices(string.ascii_uppercase, k=3))
            flight_identification = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            return f"{telephony_designator} {flight_identification}"

    def add_request(self):
        """
        Randomly add requests (landing, takeoff, emergency landing) to the appropriate queues.

        This method randomly selects the type of request for each aircraft based on specified probabilities:
        - 70% chance of a landing request
        - 20% chance of a takeoff request
        - 10% chance of an emergency landing request

        For each request:
        1. Generate a random flight number and call sign for the aircraft.
        2. If the request is a takeoff:
            - Add the aircraft to the takeoff queue.
            - Print a message indicating the takeoff request.
        3. If the request is an emergency landing:
            - Push the aircraft to the landing queue with a priority of 0 (highest priority).
            - Print a message indicating the emergency landing request.
        4. If the request is a normal landing:
            - Push the aircraft to the landing queue with a priority of 1 (lower priority than emergency landing).
            - Print a message indicating the landing request.
        """
        # Randomly adding requests (landing, takeoff, emergency landing)
        request_type = random.choices(
            ["landing", "takeoff", "emergency landing"], weights=[0.7, 0.2, 0.1] # Weighing the chances of a plane in an emergency to be rare.
        )[0]
        flight_number = random.randint(100, 999)
        call_sign = self.generate_call_sign() # Randomly picks out of type a, b or c.

        if request_type == "takeoff":
            self.takeoff_queue.append((flight_number, call_sign))
            print(f"Flight {flight_number} ({call_sign}) requests takeoff")
        else:
            if request_type == "emergency landing":
                heapq.heappush(
                    self.landing_queue, (0, flight_number, call_sign)
                )  # Emergency landing has higher priority
                print(
                    f"Flight {flight_number} ({call_sign}) requests emergency landing"
                )
            else:
                heapq.heappush(
                    self.landing_queue, (1, flight_number, call_sign)
                )  # Normal landing
                print(f"Flight {flight_number} ({call_sign}) requests landing")

    def process_requests(self):
        """
          Process aircraft requests from landing and takeoff queues.

          This method iterates as long as there are aircraft in either the landing or takeoff queues.
          For each iteration:
          1. If there are aircraft in the landing queue:
              a. Pop the aircraft with the highest priority (emergency landing first) from the landing queue.
              b. Check if the same aircraft is also in the takeoff queue. If so, remove it from the takeoff queue.
              c. Print a message indicating that the aircraft is landing, with optional 'Emergency' tag.
          2. If there are no aircraft in the landing queue but there are aircraft in the takeoff queue:
              a. Pop the aircraft from the takeoff queue.
              b. Print a message indicating that the aircraft is taking off.

          The logic ensures that emergency landing requests are given priority over regular landings and takeoffs.
          If an aircraft is in both the landing and takeoff queues (e.g., emergency landing followed by immediate takeoff),
          it is removed from the takeoff queue to avoid processing it for takeoff.
          """
        while self.landing_queue or self.takeoff_queue:
            if self.landing_queue:
                _, flight_number, call_sign = heapq.heappop(self.landing_queue)
                if flight_number in self.takeoff_queue:
                    self.takeoff_queue.remove((flight_number, call_sign))
                print(
                    f"CONTROL: {flight_number} ({call_sign}) land{' (Emergency)' if _ == 0 else ''}"
                )

            elif self.takeoff_queue:
                flight_number, call_sign = self.takeoff_queue.pop(0)
                print(f"CONTROL: {flight_number} ({call_sign}) takeoff")


if __name__ == "__main__":
    simulation = AircraftSimulation()
    for _ in range(10):  # Run it for this many loops.
        simulation.add_request()
    simulation.process_requests()
