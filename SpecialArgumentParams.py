def standard_arg(arg):
     print(arg)

def pos_only_arg(arg, /):
     print(arg)

def kwd_only_arg(*, arg):
     print(arg)

def combined_example(pos_only, /, standard1,standard2, *, kwd_only):
     print(pos_only,standard1, standard2, kwd_only)


standard_arg(2)
combined_example(2,5,standard2=7,kwd_only=4)