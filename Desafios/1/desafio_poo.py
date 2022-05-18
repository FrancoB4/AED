
def to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    out_seconds = (seconds % 3600) % 60

    return f"{hours}:{minutes}:{out_seconds}"


def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


def run():
    times = [6551, 21720, 3123, 57862]
    for time in times:
        print(f" {time}s - {to_hms(time)}")


if __name__ == '__main__':
    run()
