from typing import List, Set, Tuple

class Sensor:

    def __init__(self, x:int, y:int, xb: int, yb: int) -> None:
        self.x = x
        self.y = y
        self.xb = xb
        self.yb = yb
        self.mh_dist = abs(x - xb) + abs(y - yb)

def parse_token(token: str) -> int:
    return int(token[2:-1])

def parse_input() -> List[Sensor]:
    lines = list(map(lambda e: e.strip(), open('p15.txt', 'r').readlines()))

    sensors = []
    for line in lines:
        tokens = line.split(' ')
        sensors.append(
            Sensor(parse_token(tokens[2]), parse_token(tokens[3]), parse_token(tokens[8]), parse_token(tokens[9] + ' '))
        )
    return sensors


def part1():
    Y = 2_000_000
    sensors = parse_input()

    ans = 0
    seen = set()
    for sensor in sensors:

        if sensor.y - sensor.mh_dist <= Y <= sensor.y + sensor.mh_dist:
            # sensor in range of Y level
            if (sensor.x, Y) not in seen:
                ans += 1
                seen.add((sensor.x, Y))

            remaining_dist = sensor.mh_dist - abs(sensor.y - Y)
            for i in range(1, remaining_dist+1):
                if (sensor.x - i, Y) not in seen:
                    ans += 1
                    seen.add((sensor.x - i, Y))
                if (sensor.x + i, Y) not in seen:
                    ans += 1
                    seen.add((sensor.x + i, Y))
    return ans


def part2():
    MIN_L, MAX_L = 0, 4_000_000
    sensors = parse_input()

    for x in range(MIN_L, 4_000_000+1):
        y = MIN_L
        while y <= MAX_L:
            is_valid = True
            for sensor in sensors:
                mh_dist_xy = abs(sensor.x - x) + abs(sensor.y - y)
                if mh_dist_xy <= sensor.mh_dist:
                    is_valid = False
                    if sensor.y > y:
                        y += 2*abs(sensor.y-y)
                    else:
                        y += sensor.mh_dist - mh_dist_xy
                    break
            if is_valid:
                return x * MAX_L + y
            else:
                y += 1

print(part1())
print(part2())
