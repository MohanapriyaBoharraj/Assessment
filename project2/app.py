import time

file_path = "/data/log.txt"

while True:
    current_time = time.ctime()
    with open(file_path, "a") as f:
        f.write("Logged at: " + current_time + "\n")

    print("Logged data")
    time.sleep(5)
