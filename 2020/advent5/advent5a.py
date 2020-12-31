f1 = open("aventlist5a.txt", "r")
boarding = f1.readlines()
seat_rows = []
seat_columns = []
seats = []
max_seat = 0
for i in range(0, len(boarding)):
    boarding[i] = boarding[i].replace("\n", '').replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    seat_rows.append(int(boarding[i][:7], 2))
    seat_columns.append(int(boarding[i][7:], 2))
    seats.append((seat_rows[i]*8) + seat_columns[i])
    if max_seat < seats[i]:
        max_seat = seats[i]
seats.sort()
for i in range(0, len(seats)-1):
    if seats[i+1]-seats[i] > 1:
        print(seats[i])
        print(seats[i+1])
# print(boarding)
# print(seat_rows)
# print(seat_columns)
print(seats)
# print(max_seat)
