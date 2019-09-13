from timed_command_class import TimedCommand
from runner_class import CommandListRunner

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
import subprocess
subprocess.Popen(["python", "/app/app.py"],
                 stdout=subprocess.PIPE)

CommandListRunner(command_list).run()
