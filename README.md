# py_css

a css file (Bootstrap like) for unicode text formatting in python console output :)

## USAGE

(Will try to add a pip installable, later. As of now, this is it:)

Copy the css.py file to your project repo.

Import in your code: `import Bootstrap from css`.

Create an object: `text = Bootstrap()`

Use as: `text.colorize(<string>, <color>)` or `text.format(<string>, < b / i / u >)` or `text.start_block(<color>, <formatter>)`

## Accessible functions/methods

Simple ones :

- `colorize()` : Takes a text, font color(optional) and bgcolor(optional).
- `stylize()` : Takes a text, style name (bold, italics, underline and blink). Passing only initials work (e.g. 'b' for bold)

_INFO_ : blink is experimental, if it doesn't work, it does not break anything! Therefore no shorthand for it!

Lil advanced ones:

- `get_color()` : Takes name of a font color and returns its color code
- `get_bgcolor()` : Takes name of a background color and returns its color code
- `new_color()`: Takes a color name and color code. Can be used to add a new custom font color entry
- `new_bgcolor()`: Takes a color name and color code. Can be used to add a new custom background color entry

_WARNING_ : Only use `new_color()` or `new_bgcolor()` if you know what you are doing!

## Example

```Python
    import  Bootstrap from css # make sure you have downloaded the css.py file in the same folder/directory
    text = Bootstrap()

    # Using colorize to color
    print(text.colorize("THIS IS RED", "red")) # You can also use Bootstrap classes, eg. danger
    print(text.colorize("THIS IS blue", "primary")) # blue will also work.

    # Using stylize to format text- bold(b), italics(i), underline(u), selected(s), blink
    print(text.stylize("A BOLD move", "b")) # bold also works in place of b
    print(text.stylize("Slightly slanted", "i"))
    print(text.stylize("Have a look at me", "u"))

    # You can also combine colors and formats:
    print(text.stylize(text.colorize("This is bold in red"), 'b'))

    # Change color for multiple lines if needed!
    text.start_block('red', bold=True)
    # Any text in this clock will be printed in RED, and BOLD by default
    text.end_block()
```

_IMPORTANT_: Info is not the same color as bootstrap info, its violet!

## KNOWN ISSUES

1. This DOES NOT work in Windows CMD. Use PowerShell, Git Bash(using MinGW Terminal) or VScode terminal. The problem is with cmd, it does not support colors like these.

2. Style - blink DOES NOT work on Windows.

## INSPIRATION

[This](https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python/39452138#39452138) stackoverflow was the inspiration for this project.
