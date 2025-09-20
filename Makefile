ENTRY_POINT="src/bangshim/bangshim.py"
VERSION := $(shell uvx dunamai from git --bump --no-metadata --style pep440)


run:
	uv run bangshim ./example/demo.ps1
	./example/demo

build:
	uv build

dist:
	uv run pyinstaller --name=bangshim -i asset/icon.ico --add-data "src/bangshim/asset:bangshim/asset" -F $(ENTRY_POINT)
	sha256sum dist/bangshim.exe

test: ./dist/bangshim.exe ./example/demo.sh
	./dist/bangshim.exe ./example/demo.sh
	./example/demo

install:
	uv tool install .

.PHONY: version
version:
	uvx --from=toml-cli toml set --toml-path=pyproject.toml project.version $(VERSION)

clean: ./build ./dist
	rm -rf ./build ./dist
	rm *.spec
	rm example/*.shim
	rm example/*.exe
	uv tool uninstall bangshim

update:
	uv sync --upgrade
