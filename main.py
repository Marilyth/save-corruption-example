import time


def write_file():
    print("Writing the header")
    with open("output.txt", "w") as f:
        f.write("Save data start\n")

    # Simulate some other work.
    print("Don't quit the program please")
    time.sleep(5)

    print("Writing the body")
    with open("output.txt", "a") as f:
        f.write("Save data end")

    print("Done saving")

while True:
    write_file()
    time.sleep(2)
