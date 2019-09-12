from timed_command_class import TimedCommand

command_list = [
    TimedCommand(
        ["python", "fib.py"],
        "run python script"
    ),
    TimedCommand(
        ["./a.out"],
        "run in C++",
        [["g++", "fib.cpp"]],
        "compile C++ file",
        [["rm", "a.out"]]
    ),
    TimedCommand(
        ["java", "fib"],
        "run in java",
        [["javac", "fib.java"]],
        "compile java file",
        [["rm", "fib.class"]]
    ),
    TimedCommand(
        ["php", "fib.php"],
        "run in php"
    )
]


for timed_command in command_list[1:]:
    timed_command.run()
