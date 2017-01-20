# Author: Kristen Findley
# Version: Python 3.5.2
# Date: January 19, 2017
# Description: Text

from tkinter import * # text widget not a themed widget so no need to import ttk module
root = Tk()

text = Text(root, width = 40, height = 10) # number characters wide and tall (can still contain arbitrarily long amounts of text)
text.pack()

text.config(wrap = 'char') # other wrapping options are 'none' and 'word'
text.get() # with one parameter it will return the character at that index and if give two parameters, it will return the string contained between those indices

# base 4.2 refers to character at that index on line 4
# end refers to position after last character
# line refers to logical lines (ending with invisible \n), not display lines

# modifiers include +/- # chars & +/- # lines as well as linestart, lineend, wordstart, wordend

text.get('1.0', 'end') # represents 0th index (first character) of first line through the end (aka all contents)
text.get('1.0', '1.end') # retrieves everything from first line

text.insert('1.0 + 2 lines', text ='Inserted message') # located at first position, but two lines down
text.insert('1.0 + 2 lines lineend', text = 'and\nmore and\nmore')
text.delete('1.0') # deletes first character in text box

text.delete('1.0', '1.0 lineend') # deletes everything up to the last character at the end of the first line (aka the \n character since it is non-inclusive)
text.delete('1.0', '3.0 lineend + 1 chars')

text.replace('1.0', '1.0 lineend', 'This is the first line.') # basically delete + insert in one method
text.config(state = 'disabled') # prevents user from being able to enter any text and also prevents deletions or insertions until re-enabled
text.config(state = 'normal')

text.tag_add('my_tag', '1.0', '1.0 wordend') # 3 parameters: name, start, end
text.tag_configure('my_tag', background = 'yellow')
# use tag_raise and tag_lower methods to change cofiguration priorities for conflicts on the same section of text
text.tag_remove('my_tag', '1.1', '1.3') # non-inclusive end parameter
text.tag_ranges(my_tag) # returns ranged that the tag covers
text.tag_names() # shows what tags have been applied to the text (you can also give an index arguement to see what tags apply to the specifed index

text.replace('my_tag.first', 'my_tag.last', 'That')
text.tag_delete('my_tag')

text.mark_names() # insert and current are marks that tkinter automatically tracks and will always be displayed
# you can use mark as the base for an index
text.insert('insert', '_') # inserts _ where insert mark is
text.mark_set('my_mark', 'end') # mark only represents a location between characters
text.mark_gravity('my_mark', 'left') # other option is right and specifies if the mark follows the left or right side
text.mark_unset('my_mark')

image = PhotoImage(file = 'filepath')
text.image_create('insert', image = image) # inserts image at insert mark
button. Button(text, text = 'Click Me') # create button as a child widget of the text parent
text.window_create('insert', window = button) # inserts button where at insert mark
