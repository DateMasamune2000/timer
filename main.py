#!/usr/bin/env python
import sys
import os
from time import sleep

import rich
from rich.progress import track

class CmdSyntaxErr(Exception):
    pass

slpmins = 25

if len(sys.argv) > 2:
    raise CmdSyntaxErr('Too many arguments')
elif len(sys.argv) == 2:
    try:
        slpmins = int(sys.argv[1])
    except ValueError as e:
        raise CmdSyntaxErr('Argument must be an integer') from e

rich.print(
        f'[bold]*** [yellow]Starting timer for {slpmins} minutes[/yellow] ***[/bold]',
        )

for i in track(range(slpmins*60), description="Timer running..."):
    sleep(1);

rich.print('[bold green]Time is up![/bold green]')

