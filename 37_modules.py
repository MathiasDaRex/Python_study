# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

import messages as msg

msg.hello()
msg.bye()

# if we want to import just some of the functions, there is another way
# by this way we don't have to call the module name, we can use the functions directly

# from messages import hello,bye
#
# hello()
# bye()

# we can access all of the modules
# also we can look up the documentation - https://docs.python.org/3/py-modindex.html
help("modules")