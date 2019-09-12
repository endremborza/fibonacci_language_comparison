import time
import subprocess

from typing import Union

START_TEXT = """

____________________________
####  {}
____________________________


"""

END_TEXT = """


DONE!!! ran in {0:0.3f} seconds
----------------------------

"""

PREPARE_TEXT = """
initially, preparing with:
{}

"""

PREPARE_DONE_TEXT = """
done in {0:0.2f} seconds
"""


class TimedCommand:

    def __init__(self,
                 main_command: list,
                 description: Union[str, None] = None,
                 prepare_commands: Union[list, None] = None,
                 preparation_description: Union[str, None] = None,
                 cleanup_commands: Union[list, None] = None):

        self.main_command = main_command
        self.description = description or ' '.join(main_command)

        self.prepare_commands = prepare_commands
        self.preparation_description = preparation_description or '\n'.join([' '.join(c)
                                                                             for c in prepare_commands or []])
        self.cleanup_commands = cleanup_commands or []

        self.prepare_time = 0
        self.proc_time = 0

    def _do_preparations(self):
        if self.prepare_commands:
            print(PREPARE_TEXT.format(self.preparation_description))
            input("\nready?\n")
            start = time.time()
            for prep_comm in self.prepare_commands:
                print("running command:\n{}\n".format(' '.join(prep_comm)))
                subprocess.call(prep_comm)
            self.prepare_time = time.time() - start
            print(PREPARE_DONE_TEXT.format(self.prepare_time))

    def run(self):
        print(START_TEXT.format(self.description))
        self._do_preparations()

        input("ready to run main command?\n\n")
        print("running command:\n{}\n".format(' '.join(self.main_command)))
        start = time.time()
        subprocess.call(self.main_command)
        self.proc_time = time.time() - start
        print(END_TEXT.format(self.proc_time))
        for cleanup_comm in self.cleanup_commands:
            subprocess.call(cleanup_comm)
