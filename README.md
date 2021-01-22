# romanF
An esolang using Roman numerals, based on BF. 

## Symbols
```
I : Increment value in cell
V : Decrement value in cell
X : Go to next cell
L : Go to previous cell
D : Output a byte, replace with input byte
C : If cell in pointer is 0, go to the next matching M
M : If cell in pointer is not 0, go to the previous matching C
```
## Equivalent to BF
```
I : +
V : -
X : >
L : <
D : .,
C : [
M : ]
```
## Conversion to Arabic
Of course, you can use the raw Roman numbers, but whats the fun of that if you can use Arabic numerals?
Unfortunately, Roman numerals isn't really standardized, so the scripts you made by hand might not work.
I'm using the Roman Python library to encode and decode numerals. (If you don't have one, it will automatically install it using pip (I guess))

To convert romanF to number, take this cat program:

```DCDM```

First, the roman number is split into the longest valid Roman numeral:

`DC D M`

Then it gets converted to Arabic numeral:

`600 500 1000`

## Examples

The HELLO program:

```IIIIIIIICXIIIIIIIIILVMXCXIXILLVMXDCVMXVVVCLILIXXVMLDCVMLIIIIIIICXIXILLVMXDCVMXCLILIXXVMLDCVMLIIICXIXILLVMXDCVMX```

or, in Arabic numeral:

```3 3 2 113 3 3 55 1090 19 1 50 55 1010 605 1015 5 5 151 59 15 1050 605 1053 3 1 119 1 50 55 1010 605 1090 51 59 15 1050 605 1053 119 1 50 55 1010 605 1010```

Cat: [above](https://github.com/Gilbert189/romanf#conversion-to-arabic)
## Running the program

You can run romanF using this command:

```$ python3 romanf.py```

If you want to run a file, you can use this command:

```$ python3 romanf.py /path/to/file.rf```

To convert romanF code to numbers, use this command:

```$ python3 romanfconv.py [/optional/path/to/file.rf /optional/path/to/converted/file.rf]```

