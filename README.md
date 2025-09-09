# BanG Shim!

Do one thing and do it well: Make scripts executable by adding shim from shebang.

## Usage
```sh
./myscript # Can not find if you do not add the .sh
./myscript.sh # Open in editor or can not execute

bangshim ./myscript.sh
./myscript
Hello World
```

## FAQ

1. Q: How to work with `/usr/bin/env` ?
A: We suppose you installed an `env.exe` in your `PATH`. For example, you can install [uutils/coreutils](https://github.com/uutils/coreutils) by `scoop install uutils-coreutils`


## Credit
1. `shim.exe` from [kiennq/scoop-better-shimexe](https://github.com/kiennq/scoop-better-shimexe)

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