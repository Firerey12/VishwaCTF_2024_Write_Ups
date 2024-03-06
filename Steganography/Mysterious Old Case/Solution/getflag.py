with open("flag.txt", "w") as flag:
    with open("flight_logs/flight_logs/Flight-305.log") as f:
        for line in f:
            buffer = line.strip()
            if len(buffer) == 1:
                flag.write(buffer)