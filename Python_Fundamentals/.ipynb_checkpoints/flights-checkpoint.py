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
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())
            
            
    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row, letter))
        
        
class Aircraft:
    
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
               "ABCDEFGHJK"[:self._num_seats_per_row])
    

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