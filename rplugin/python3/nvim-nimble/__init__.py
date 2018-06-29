import glob
import neovim
import os
import re
import sys

from subprocess import Popen, PIPE

@neovim.plugin
class NvimNimble(object):
    NIMBLE_CMD = 'nimble'

    def __init__(self, nvim):
        self.nvim = nvim
        self._ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

    def _is_nimble_project(self):
        cur_dir = os.path.abspath(".")
        nimble_file = glob.glob(os.path.join(cur_dir, '*.nimble'))
        if len(nimble_file) == 0:
            return False
        return os.path.isfile(nimble_file[0])

    def _echo(self, msg):
        self.nvim.command("echo '" + msg + "'")

    def _run_nimble(self, args):
        cmd = list(args)
        cmd.insert(0, self.NIMBLE_CMD)
        with Popen(" ".join(cmd), stdout=PIPE, shell=True) as proc:
            ret = proc.stdout.read()
            echo_str = self._ansi_escape.sub('', ret.decode('utf-8'))
            self._echo(echo_str)

    @neovim.command('Nimble', range='', nargs='*')
    def nimble(self, args, _):
        if self._is_nimble_project():
            self._run_nimble(args)
            return True
        else:
            self._echo('nimble file is not exists')

