
cinema = [

    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True]

    # --------------------------- #
]

while True:
    def print_cinema():
        for row in cinema:
            for seat in row:
                if seat == True:
                    print("0", end=" ")
                else:
                    print("X", end=" ")
            print()
        print("--ЕКРАН--")


    print_cinema()


    def valid_seat(row_num: int, seat_num: int) -> bool:
        if row_num >= 0 and row_num <= len(cinema):
            row = cinema[row_num]
            if seat_num >= 0 and seat_num <= len(row):
                # seat is present in cinema
                if row[seat_num] == True:
                    if row[seat_num + 1] == True and row[seat_num - 1] == True:
                        return True
        return False


    book_seats = int(input('How many seats you want to book? :  '))
    for i in range(book_seats):
        seats_row = int(input(f'Pick your seats row: ')) - 1
        seats_num = int(input('Pick your seats num: ')) - 1
        if valid_seat(seats_row, seats_num):
            cinema[seats_row][seats_num] = False
            print('Your seats are booked:\n')
        print_cinema()
