ENTRY_POINT=src/bangshim/bangshim.py

run:
	uv run bangshim ./example/demo.ps1
	./example/demo

build:
	uv build

dist:
	uv run pyinstaller --name=bangshim --add-data "src/bangshim/asset:bangshim/asset" -F $(ENTRY_POINT)

test: ./dist/bangshim.exe ./example/demo.sh
	./dist/bangshim.exe ./example/demo.sh
	./example/demo

install:
	uv tool install .

clean: ./build ./dist
	rm -rf ./build ./dist
	rm *.spec
	rm example/*.shim
	rm example/*.exe
	uv tool uninstall bangshim
