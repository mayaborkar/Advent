# https://adventofcode.com/2020/day/5
f1 = open("adventlist5.txt", "r")
boarding = f1.readlines()
# creating empty arrays
seat_rows = []
seat_columns = []
seats = []
# setting counter equal to 0
max_seat = 0
for i in range(0, len(boarding)):
    # replacing all F's with 0 B's with 1, L's with 0, and R's with 1
    boarding[i] = boarding[i].replace("\n", '').replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    # appending 7 onwards and converting from binary
    # input: binary, output: decimal
    seat_rows.append(int(boarding[i][:7], 2))
    seat_columns.append(int(boarding[i][7:], 2))
    # generating the seat ID 8*row + column
    seats.append((seat_rows[i]*8) + seat_columns[i])
    # finding the max seat
    if max_seat < seats[i]:
        max_seat = seats[i]
# sorts seat numbers in order
seats.sort()
# day 5 part B
# checking if there is an open seat in between
for i in range(0, len(seats)-1):
    if seats[i+1]-seats[i] > 1:
        print(seats[i])
        print(seats[i+1])
print(seats)

