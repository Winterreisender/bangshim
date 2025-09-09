ENTRY_POINT=bangshim/__main__.py

run:
	uv run $(ENTRY_POINT) ./example/demo.sh

build:
	uv build

dist:
	uv run pyinstaller --name=bangshim --add-data "bangshim/asset:bangshim/asset" -F $(ENTRY_POINT)

clean: ./build ./dist
	rm -rf ./build ./dist
	rm *.spec

test: ./dist/bangshim.exe ./example/demo.sh
	./dist/bangshim.exe ./example/demo.sh
	./example/demo