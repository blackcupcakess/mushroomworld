"""Simple ASCII mushroom drawing."""


def draw_mushroom():
    art = [
        "   _",
        "  / \\",
        " /___\\",
        "   | |",
        "   |_|",
    ]
    for line in art:
        print(line)


if __name__ == "__main__":
    draw_mushroom()
