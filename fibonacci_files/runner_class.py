from typing import List
from timed_command_class import TimedCommand


class CommandListRunner:

    def __init__(self, command_list: List[TimedCommand]):

        self.command_list = command_list

    def run(self):
        for timed_command in self.command_list:
            timed_command.run()
