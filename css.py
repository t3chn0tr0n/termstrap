''' 
The Bootstrap CSS for Python Developers
AUTHOR: Avik Mukherjee
LICENSE: MIT, Copyright (c) 2019 Avik Mukherjee
HOME: https://github.com/t3chn0tr0n/py_css/
'''


class Bootstrap:

    # Font color
    primary = '\33[34m'
    success = '\33[92m'
    danger = '\33[91m'
    warning = '\33[33m'
    info = '\33[95m'
    light = '\33[37m'
    white = '\33[97m'
    dark = '\33[90m'
    default = '\33[0m'

    # Bg color
    bg_primary = '\33[44m'
    bg_success = '\33[42m'
    bg_danger = '\33[41m'
    bg_warning = '\33[43m'
    bg_info = '\33[45m'
    bg_light = '\33[47m'
    ng_white = '\33[107m'
    bg_dark = '\33[40m'

    # Font style
    bold = '\33[1m'
    italics = '\33[3m'
    underline = '\33[4m'
    selected = '\33[7m'
    blink = '\33[7m'

    def get_color(self, color):
        '''
            Returns the font color code for a given color name
        '''
        color_key = {
            'primary': self.primary,
            'blue': self.primary,
            'success': self.success,
            'green': self.success,
            'danger': self.danger,
            'red': self.danger,
            'yellow': self.warning,
            'warning': self.warning,
            'info': self.info,
            'violet': self.info,
            'light': self.light,
            'white': self.white,
            'dark': self.dark,
            'black': self.dark,
            'default': self.default
        }
        return color_key[color]
        try:
            return color_key[color]
        except KeyError:
            return ''

    def get_bg(self, color):
        '''
            Returns the background color code for a given color name
        '''
        bg_key = {}
        try:
            return bg_key[color]
        except KeyError:
            return ''

    def colorize(self, text='', color='', bg=''):
        return self.get_color(color) + self.get_bg('jasjds') + text + self.default


# DRIVERS
color = Bootstrap()
print(color.colorize("hello", "red"))
print(color.colorize("hello", "info"))
print(color.colorize("hello", "green"))
print(color.colorize("hello", "blue"))
