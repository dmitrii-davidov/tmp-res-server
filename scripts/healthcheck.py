import subprocess
from argparse import ArgumentParser


class Tool:
    command = None
    pipes = {}
    encoding = 'utf-8'

    def run(self, path, fix=False):
        command = [self.command] + self._get_arguments(fix=fix) + [path]
        print('-' * 5)
        print('# run:', ' '.join(command))
        process = subprocess.run(
            command,
            **self.pipes,
        )
        error = self._analyze(process) or process.returncode
        print('# end:', self.command, ' with error' if error else '')
        print()
        if error:
            exit(1)

    def _get_arguments(self, fix: bool):  # pylint:disable=W0613
        return []

    def _analyze(self, process):
        error = False
        for key in ['stdout', 'stderr']:
            if getattr(process, key, None):
                print(f'# {key}')
                text: str = getattr(process, key).decode(self.encoding)
                text = text.strip('\r\n ')
                print(text)
                error |= self._find_error(text)
        return error

    def _find_error(self, text):  # pylint:disable=W0613
        return False


class ISortTool(Tool):
    command = 'isort'
    pipes = {'stdout': subprocess.PIPE}

    def _get_arguments(self, fix):
        arguments = ['-rc']
        if not fix:
            arguments.append('-c')
        return arguments

    def _find_error(self, text):
        return 'ERROR' in text


class YAPFTool(Tool):
    command = 'yapf'

    def _get_arguments(self, fix):
        arguments = ['-r']
        arguments.append('-i' if fix else '-d')
        return arguments


class PyLintTool(Tool):
    command = 'pylint'

    def _get_arguments(self, fix):  # pylint:disable=W0613
        return ['--errors-only']


class Flake8Tool(Tool):
    command = 'flake8'


tools = [ISortTool(), YAPFTool(), PyLintTool(), Flake8Tool()]


def healthcheck(args):
    for tool in tools:
        tool.run(args.path, fix=args.fix)


def main():
    parser = ArgumentParser()

    parser.set_defaults(func=healthcheck)
    parser.add_argument('--fix', action='store_true')
    parser.add_argument('path')

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
