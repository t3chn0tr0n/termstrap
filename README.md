# py_css

a css file (Bootstrap like) for unicode text formatting in python console output :)

## USAGE

Install it using pip: `pip install termstrap`

Import in your code: `import css` or ` from css import Bootstrap, printc`.

Create an object: `text = Bootstrap()`

Use as: `text.colorize(<string>, <color>)` or `text.stylize(<string>, < b / i / u >)` or `text.start_block(<color>, <formatter>)`

## Accessible functions/methods

Simple ones :

- `colorize()` : Takes a text, font color(optional) and bgcolor(optional).
- `stylize()` : Takes a text, style name (bold, italics, underline and blink). Passing only initials work (e.g. 'b' for bold). You can pass multiple styles simultaneously.

_INFO_ : blink is experimental, if it doesn't work, it does not break anything! Therefore no shorthand for it!

Lil advanced ones:

- `get_color()` : Takes name of a font color and returns its color code
- `get_bgcolor()` : Takes name of a background color and returns its color code
- `new_color()`: Takes a color name and color code. Can be used to add a new custom font color entry
- `new_bgcolor()`: Takes a color name and color code. Can be used to add a new custom background color entry

_WARNING_ : Only use `new_color()` or `new_bgcolor()` if you know what you are doing!

## Accessible Variables

All colors can be accessed by the class instance. Overwriting them will/may break functionality.

- **Color variables**: Bootstrap names - primary, danger, warning, etc.
- **Background color variables**: bg_primary, bg_danger, bg_warning, etc.
- **Style variables**: bold, italics, underline, selected, blink

## More Utility Functions
THESE ARE NOT MEMBERS OF BOOTSTRAP CLASS. NO NEED FOR INSTANCE CREATION. just import and use.
- **printc**: Like standard print(). Except: Does not have flush and file params. Have color param, takes name of the color. style param, takes a list or tuple of all styles. bgcolor param, takes name of the bgcolor!
- **hide_cursor**: Hides cursor in the console
- **show_cursor**: Restores cursor visibility.

## Example

```Python
    from css import  Bootstrap, printc # make sure you have downloaded the css.py file in the same folder/directory
    text = Bootstrap()

    # Using colorize to color
    print(text.colorize("THIS IS RED", "red")) # You can also use Bootstrap classes, eg. danger
    print(text.colorize("THIS IS blue", "primary")) # blue will also work.

    # Using stylize to format text- bold(b), italics(i), underline(u), selected(s), blink
    print(text.stylize("A BOLD move", "bold")) # b also works in place of bold
    print(text.stylize("Slightly slanted", "i"))
    print(text.stylize("More the merrier", 'b', 'u', 's', 'i'))

    # You can also combine colors and formats:
    print(text.stylize(text.colorize("This is bold in red"), 'b'))

    # Change color for multiple lines if needed!
    text.start_block('red', bold=True)
    # Any text in this clock will be printed in RED, and BOLD by default
    text.end_block()
    
    # Using the printc
    printc("RED text in *BOLD*", color='red', style=('b'))
    printc("[1,2,3,4]", color='warning', style=('b', 'u'), sep='***') # yellow text, styled bold and underlined, seperated by - ***
    printc("a", "b", "cdf", color="primary", end='') # print multiple strings and specify end param as none, ie. no newline at end!
```

_IMPORTANT_: Info is not the same color as bootstrap info, its violet!

## KNOWN ISSUES

1. Style - blink DOES NOT work in most cases.
2. Windows cmd only supports color in windows 10 (v1511 onwards)!

## INSPIRATION

[This](https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python/39452138#39452138) stackoverflow was the inspiration for this project.
