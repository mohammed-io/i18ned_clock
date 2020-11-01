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


## Stage 3

The clock should be displayed in 7-segment-like format. Just like the "12" printed on the screen. Each Symbol might be mapped to a _matrix_ of 5\*5 just like the provided example. Also should support `Column` and `Row` as well, where the latter will be broken.

![7-Segment clock](https://raw.githubusercontent.com/mohammed-io/i18ned_clock/master/7_segment_clock.png)

You might read more about how characters look like [here](https://www.wikiwand.com/en/Seven-segment_display#/Decimal)

Keep in mind, you have additional characters like "UTC" or ":" that are not included in the link above.

Expect that the `Row` class from last stage will easily break, which is normal.
