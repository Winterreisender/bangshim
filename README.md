<div align="center" >
    
# #BanG Shim!
<img src='asset/banner.jpg' width="33%"/>

[![PyPI - Downloads](https://img.shields.io/pypi/dm/bangshim)](https://pypi.org/project/bangshim)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bangshim.svg)](https://pypi.org/project/bangshim)
![GitHub Created At](https://img.shields.io/github/created-at/Winterreisender/bangshim)

Make scripts with shebang executable in Windows by adding [shim](https://docs.chocolatey.org/en-us/features/shim/).

</div>

## Usage
1. Install bangshim with [scoop](https://scoop.sh/)
```sh
scoop install https://raw.githubusercontent.com/Winterreisender/bangshim/refs/heads/master/bangshim.json
```
or [uv](https://docs.astral.sh/uv/)
```sh
uv tool install bangshim
```
or pip
```sh
pip install bangshim
```
It's also recommended to install [uutils/coreutils](https://github.com/uutils/coreutils) for the `env` in shebang

2. Write any script with [shebang](https://www.in-ulm.de/~mascheck/various/shebang/), supposing you have an intepreter (Git Bash, MSYS2, etc.) installed for your scripts.

```python
#!/usr/bin/sh
print("Hello World")
```

3. Make your script executable
```sh
bangshim ./myscript.sh
./myscript
# "Hello World"
```


## FAQ

1. Q: Why doing this?  
A: shebang is the Unix way for executable scripts, while shim are the best practice for Windows. And this is a tool to make the Unix style work in Windows. 


2. Q: How it works?  
A: bangshim do a simple things, search intepreter from shebang in `PATH`, and generate args for [shim](https://docs.chocolatey.org/en-us/features/shim/).

3. Q: How to work with `/usr/bin/env` ?  
A: We suppose you installed an `env.exe` in your `PATH`. For example, you can install [uutils/coreutils](https://github.com/uutils/coreutils) by `scoop install uutils-coreutils`


## Build

See [Makefile](Makefile) for more information

## Credit
1. `shim.exe` from [kiennq/scoop-better-shimexe](https://github.com/kiennq/scoop-better-shimexe) licensed under `MIT OR Unlicense`

## License

    Copyright 2025 Winterreisender

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
