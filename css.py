''' 
The Bootstrap CSS for Python Developers
AUTHOR: Avik Mukherjee
LICENSE: MIT, Copyright (c) 2019 Avik Mukherjee
HOME: https://github.com/t3chn0tr0n/termstrap/
'''
import sys


class Bootstrap:
    def __init__(self):
        if sys.platform == 'win32':
            from ctypes import windll
            kernel32 = windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    default = '\33[0m'

    # Font color
    primary = '\33[34m'
    success = '\33[92m'
    danger = '\33[91m'
    warning = '\33[33m'
    info = '\33[95m'
    light = '\33[37m'
    white = '\33[97m'
    dark = '\33[90m'

    # Bg color
    bg_primary = '\33[44m'
    bg_success = '\33[42m'
    bg_danger = '\33[41m'
    bg_warning = '\33[43m'
    bg_info = '\33[45m'
    bg_light = '\33[47m'
    bg_white = '\33[107m'
    bg_dark = '\33[40m'

    # Font style
    bold = '\33[1m'
    italics = '\33[3m'
    underline = '\33[4m'
    selected = '\33[7m'
    blink = '\33[5m'

    __color_key = {
        'primary': primary,
        'blue': primary,
        'success': success,
        'green': success,
        'danger': danger,
        'red': danger,
        'yellow': warning,
        'warning': warning,
        'info': info,
        'violet': info,
        'light': light,
        'white': white,
        'dark': dark,
        'black': dark,
        'default': default
    }

    __bgcolor_key = {
        'primary': bg_primary,
        'blue': bg_primary,
        'success': bg_success,
        'green': bg_success,
        'danger': bg_danger,
        'red': bg_danger,
        'yellow': bg_warning,
        'warning': bg_warning,
        'info': bg_info,
        'violet': bg_info,
        'light': bg_light,
        'white': bg_white,
        'dark': bg_dark,
        'black': bg_dark,
    }

    __style_key = {
        'b': bold,
        'bold': bold,
        'i': italics,
        'italics': italics,
        'u': underline,
        'underline': underline,
        's': selected,
        'selected': selected,
        'blink': blink
    }

    def get_color(self, color):
        '''
            Returns the font color code for a given color name
        '''
        try:
            return self.__color_key[color]
        except KeyError:
            return ''

    def get_bgcolor(self, color):
        '''
            Returns the background color code for a given color name
        '''
        try:
            return self.__bgcolor_key[color]
        except KeyError:
            return ''

    def get_style(self, style):
        '''
            Returns the style code for a given style
        '''
        try:
            return self.__style_key[style]
        except KeyError:
            return ''

    def colorize(self, text, color='', bg=''):
        return self.get_color(color) + self.get_bgcolor(bg) + text + self.default

    def stylize(self, text, *styles):
        applied_styles = ''
        for style in styles:
            applied_styles += self.__style_key[style]
        applied_styles.strip()
        return applied_styles + text + self.default

    def new_color(self, color_name, color_code):
        self.__color_key[color_name] = color_code

    def new_bgcolor(self, color_name, color_code):
        self.__bgcolor_key[color_name] = color_code


def hide_cursor():
    '''
    Hides the cursor in the console
    '''
    if sys.platform == 'win32':
        kernel32 = windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    sys.stdout.write("\033[?25l")


def show_cursor():
    '''
    Enables the cursor in the console
    '''
    sys.stdout.write("\033[?25h")


def printc(*objects, style=(), color='default', bgcolor='default', sep=' ', end='\n'):
    '''
    params: objects[, style, color, bgcolor, sep, end].

    * Pass objects like standard print() takes. sep and end have same useage.

    * style MUST BE ITERABLE, i.e. list or tuple, where each element is a style.

    * color is font color.

    * bgcolor is background color.
    '''
    b = Bootstrap()
    print(b.get_color(color) + b.get_bgcolor(bgcolor), end="")
    for s in style:
        print(b.get_style(s), end="")
    for obj in objects:
        print(obj, end='')
    print(b.default, end=end, sep=sep,)
