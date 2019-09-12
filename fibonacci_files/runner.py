import subprocess
import time

START_TEXT = """

____________________________
####  {}
____________________________


"""

END_TEXT = """


DONE!!! ran in {0:0.3f} seconds
----------------------------

"""


command_list = [
    ["run python script",
     ["python", "fib.py"],
     []
     ],
    ["compile C++ file",
     ["g++", "fib.cpp"],
     []
     ],
    ["run compiled c++ file",
     ["./a.out"],
     [["rm", "a.out"]]
     ],
    ["compile java file",
     ["javac", "fib.java"],
     []
     ],
    ["run compiled java file",
     ["java", "fib"],
     [["rm","fib.class"]]
     ],
    ["run php file",
     ["php", "fib.php"],
     []
     ]
]


for name, main_comm, after_comms in command_list[1:]:
    print(START_TEXT.format(name))
    input("ready?\n\n")
    start = time.time()
    subprocess.call(main_comm)
    print(END_TEXT.format(time.time() - start))
    for endcomm in after_comms:
        subprocess.call(endcomm)
