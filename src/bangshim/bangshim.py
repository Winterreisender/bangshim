from pathlib import Path
from shutil import which, copy
import argparse
import logging
from importlib import resources
from collections.abc import Iterable
from sys import exit
import os

PROG_NAME="#BanG Shim!"
PROG_SLUG="bangshim"
MAX_SHEBANG_LENGTH=127 # Reference: https://www.in-ulm.de/~mascheck/various/shebang/

def generate_shim_config(exe_path :str, args: Iterable[str]) -> str:
    args = ' '.join(args)
    return f""" path = "{exe_path}"\nargs = {args} """.strip()

def shebang_mapping(argv :list[str]) -> tuple[str, list[str]]:
    exe_path, *arg = argv

    # exe_path = Path(exe_path).expanduser().resolve() # Do we really need .expanduser().resolve()?
    # if Path(exe_path).expanduser().resolve().exists():
    #     return str(exe_path), arg
    # elif exe

    cmd = Path(exe_path).name
    exe_path = which(cmd)
    assert exe_path is not None, f"Can not find {cmd} in PATH"
    return exe_path, arg


def parse_shebang(shebang_line :str) -> list[str]:
    """
    Parse and split the shebang line and return the argv
    """
    argv = shebang_line.removeprefix("!#").removesuffix("\n").split(" ")
    return argv

def bangshim(script_name :str, dry_run :bool, verbose: bool, no_clobber :bool, quiet :bool, no_path :bool):
    match (quiet, verbose):
        case True, _:
            logging.basicConfig(level=logging.CRITICAL)
        case _, True:
            logging.basicConfig(level=logging.DEBUG)
        case _,_:
            logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(PROG_NAME)
    # logger.debug(f"{prog_arg=}")

    script_path_abs = Path(script_name).expanduser().resolve()

    # Search in PATH
    if not no_path and not script_path_abs.exists():
        script_name_which = which(script_name, mode=os.F_OK)
        if script_name_which is None:
            logging.error(f"{script_name} not found and not in PATH")
            exit(2)
        logging.info(f"found {script_name} in PATH: {script_name_which}")
        script_path_abs = Path(script_name_which).expanduser().resolve()

    assert script_path_abs.exists()

    with open(script_path_abs, "r", encoding="utf-8") as f:
        shebang_line = f.readline(MAX_SHEBANG_LENGTH)
    assert shebang_line[:2] == "#!", 'Invalid shebang line'
    logger.debug(f"parse_shebang_line: {shebang_line=}")

    argv = parse_shebang(shebang_line)
    logger.debug(f"parse_shebang: {argv=}")

    interpreter_path, args = shebang_mapping(argv)
    logger.debug(f"shebang_mapping: {interpreter_path=} {args=} {script_path_abs=}")

    shim_confg_path = script_path_abs.with_suffix(".shim")
    shim_exe_path   = script_path_abs.with_suffix(".exe")
    logger.debug(f"{shim_confg_path=} {shim_exe_path=}")
    if (shim_confg_path.exists() or shim_exe_path.exists()):
        if no_clobber:
            logging.error(f"{shim_confg_path} or {shim_exe_path} already exists, exiting")
            exit(1)
        else:
            logging.warning(f"{shim_confg_path} or {shim_exe_path} already exists, overwriting...")

    args.append( script_path_abs.as_posix() ) # Use unix for better compatbility for MSYS2
    shim_config = generate_shim_config(interpreter_path, args)

    if dry_run:
        print(f"Wrtting these content to {shim_confg_path}")
        print(shim_config)
        exit(0)

    logger.info(f"generated shim config:\n{shim_config}")
    with open(shim_confg_path, 'w', encoding='utf-8') as f:
        f.write(shim_config)

    with resources.as_file(resources.files("bangshim.asset") / "shim.exe") as shim_exe_src:
        copy(shim_exe_src, shim_exe_path)


def main():
    argparser = argparse.ArgumentParser(PROG_SLUG) # Still need a better type annotion for argparser, but no good solutions
    argparser.add_argument("script_name", type=str, help="the path or name of your script")
    argparser.add_argument("--dry-run", "--what-if", action="store_true", default=False, help="show what would happen, but do not make changes")
    argparser.add_argument("--verbose", '-v', action="store_true", default=False, help="show more info")
    argparser.add_argument("--quiet"  , '-q', action="store_true", default=False, help="show less info, no interacting")
    argparser.add_argument("--no-clobber", action="store_true", default=False, help="do not overwrite existing files")
    argparser.add_argument("--no-path", action="store_true", default=False, help="do not search in path if not found")
    # argparser.add_argument("--interactive", '-i', type=bool, default=False, help="choose intepreter interactively when there's more than one inteprater found")
    prog_arg = vars(argparser.parse_args())

    bangshim(**prog_arg)

if __name__=='__main__':
    main()
