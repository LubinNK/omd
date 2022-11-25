""" 27.10.2022 Avito Practice with Classes 2 """


def main():
    """Main Launch"""
    red = Color(255, 0, 0)
    print(0.5 * red)


class Color:
    """Color class"""
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red_level, green_level, blue_level):
        self.red = red_level
        self.green = green_level
        self.blue = blue_level

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};' \
               f'{self.blue}{self.MOD}●{self.END}{self.MOD}' \
               f' {self.red} {self.green} {self.blue}'

    def __eq__(self, other):
        if self.red == other.red \
                and self.blue == other.blue \
                and self.green == other.green:
            return True
        return False

    def __add__(self, other):
        return Color((self.red+other.red) % 256,
                     (self.green+other.green) % 256,
                     (self.blue+other.blue) % 256)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __rmul__(self, coef):
        list_color = [self.red, self.green, self.blue]
        new_list_color = [int((259 * (-256 * (1 - coef) + 255))
                              * (color - 128) /
                              (255 * (259 + 256 * (1 - coef))) + 128)
                          for color in list_color]
        return Color(*new_list_color)

    def __mul__(self, other):
        return other * self


if __name__ == '__main__':
    main()
