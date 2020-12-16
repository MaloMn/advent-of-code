from utils import get_lines


def find_bus_id(timestamp):
    while True:
        for i in ids:
            if timestamp % i == 0:
                return timestamp, i
        timestamp += 1


if __name__ == "__main__":
    ts, ids = get_lines("shuttle.txt")
    ts = int(ts)
    ids = ids.split(",")
    ids = [int(a) for a in ids if a != "x"]

    arrival, bus = find_bus_id(ts)

    print((arrival - ts)*bus)
