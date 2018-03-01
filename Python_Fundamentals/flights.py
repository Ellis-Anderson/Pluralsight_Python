#!/usr/bin/env python3

class Flight:
    
    """A flight with a particular passenger aircraft"""
    
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
            
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
            
        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{}'".format(number))
            
        self._number = number
        
        self._aircraft = aircraft
        
        rows, seats = self._aircraft.seating_plan()
        
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
       
    
    def number(self):
        return self._number
    
    
    def airline(self):
        return self._number[:2]
    
    
    def aircraft_model(self):
        return self._aircraft.model()
    
    
    def _parse_seat(self, seat):
        """ Validates proper seat format.
        
        Args:
            seat: a seat designator such as '12C' or '24J'
            
        Raises:
            ValueError: if seat is unavailable
            
        Returns:
            A tuple containint an int and a string for a row and seat
        """
        rows, seat_letters = self._aircraft.seating_plan()
        
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
            
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except:
            raise ValueError("Invalid seat row {}".format(row_text))
        
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        
        return row, letter
    
    
    def allocate_seat(self, seat, passenger):
        """ Allocates a seat to a passenger.
        
        Args:
            seat: a seat designator such as '12C' or '24J'
            passenger: the name of a passenger
        
        Raises:
            ValueError: if seat is unavailable
        """
        row, letter = self._parse_seat(seat)
            
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} is already occupied".format(seat))
            
        self._seating[row][letter] = passenger
        
        
    def relocate_passenger(self, from_seat, to_seat):
        """ Moves a passenger from one seat to another.
        
        Args:
            from_seat: specifies the seat a passenger should be moved from
            to_seat: specifies the seat a passenger should be moved to
        
        Raises:
            ValueError: if from_seat is already empty or to_seat is filled
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("Seat {} is unoccupied".format(from_seat))
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} is occupied already".format(to_seat))
            
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
        
        
    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                  for row in self._seating
                  if row is not None)
    
    
    def make_boarding_cards(self, card_printer):
        
        """
        This method demonstrates how multiple functions can be used as card printers depending on circumstance.
        In our case we would generally use the console_card_printer() built in,
        but a html card printer could also be used.
        """
        
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())
            
            
    def _passenger_seats(self):
        
        """This function yields a generator object of passenger names and their seats in the form of a tuple"""
        
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row, letter))
        
        
class Aircraft:
    
    """
    This is the base class on which our Airbus and Boeing classes are built.
    Those classes inherit the initialization, registration and num_seats methods.
    However, alone, the aircraft class is rather useless. 
    Calling num_seats depends on the seating_plan method only found in the child class.
    """
    
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        
    def registration(self):
        return self._registration
    
    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows) * len(seats)
    

class AirbusA319(Aircraft):
    
    """
    These are children classes of the Aircraft base class and inherit the init, registration and num_seats methods.
    The base class is specified by the putting the base class in parantheses next to the class name.
    """
    
    def model(self):
        return "AirbusA319"
    
    def seating_plan(self):
        return range(1, 23) "ABCDEF"
    

class Boeing777(Aircraft):
    
    def model(self):
        return "Boeing777"
    
    def seating_plan(self):
        return range(1, 56) "ABCDEFGHJK" 
    

def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat('12A', 'George')
    f.allocate_seat('15F', 'Michale')
    f.allocate_seat('15E', 'Marjane')
    f.allocate_seat('1C', 'Ellis')
    f.allocate_seat('1D', 'Clooney')
    return(f)

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"     \
             "  Flight: {1}"   \
             "  Seat: {2}"     \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()