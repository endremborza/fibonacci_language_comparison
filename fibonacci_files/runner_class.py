import json
import os

from typing import List
from timed_command_class import TimedCommand


class CommandListRunner:

    def __init__(self, command_list: List[TimedCommand]):

        self.command_list = command_list
        self.names = [c.description for c in command_list]
        self.times = [{'command': n, 'outcome': None}
                      for n in self.names]
        self._dump_times()

    def run(self):
        for timed_command in self.command_list:
            timed_command.run()
            self._update_times(timed_command.description,
                               timed_command.proc_time)
            self._dump_times()
        input("Done?")

    def _dump_times(self):
        with open(os.environ.get('DUMP_LOC', '/out.json'), 'w') as fp:
            json.dump(self.times, fp)

    def _update_times(self, command, time):
        for row in self.times:
            if row['command'] == command:
                row['outcome'] = round(time, 3)
