# py_css

a css file (Bootstrap like) for unicode text formatting in python console output :)

## USAGE

Copy the css.py file to your project repo.

Import in your code: `import Bootstrap from css`.

Create an object: `text = Bootstrap()`

Use as: `text.colorize(<string>, <color>)` or `text.format(<string>, < b / i / u >)` or `text.start_block(<color>, <formatter>)

```Python

    # Using colorize to color
    print(text.colorize("THIS IS RED", "red")) # You can also use Bootstrap classes, eg. danger
    print(text.colorize("THIS IS blue", "primary")) # blue will also work.

    # Using format to format - bold, italics, url
    print(text.format("A BOLD move", "b"))
    print(text.format("Slightly slanted", "i"))
    print(text.format("Have a look at me", "u"))

    # You can also combine colors and formats:
    print(text.format(text.colorize("This is bold in red"), 'b'))

    # Change color for multiple lines if needed!
    text.start_block('red', bold=True)
     # Any text in this clock will be printed in RED, and BOLD by default
    text.end_block()
```

## KNOWN ISSUES

This DOES NOT work in Windows CMD. Use PowerShell, Git Bash or VScode terminal.

The problem is with cmd, it does not support colors like these.
