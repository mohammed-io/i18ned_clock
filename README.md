# i18ned_clock (Internationalized Clock)

The purpose of this project, is to have clock—eventually internationalized (across multiple timezones)—on the command-line interface. With possible extention to have multiple clocks running on the screen, and user able to add and delete them on demand.

## Stage 1

The first version is just to have one clock on the screen showing the current time in the default timezone, with the colons ":" toggles the blink every half second, and clock updates itself each second.

In the console, it should be only the clock visible, so the screen should be cleared on every update.

![Conceptual clock](https://raw.githubusercontent.com/mohammed-io/i18ned_clock/master/clock_concept.png)


## Stage 2

The clocks should to be arranged in columns and/or rows as needed without explicitly specifying the x and y position in the stdout. It could be made by 2 constructs, `Row` and `Column`, the first one orders the items horizontally, the latter one orders them vertically. They should support arbitrary number of clocks, ignoring the width of the terminal window.
All of them should have unified API for painting (i.e. `paint()`).

You might get inspiration from Flutter `Row` and `Column`.
