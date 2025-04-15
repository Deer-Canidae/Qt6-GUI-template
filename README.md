# Qt6 GUI Application template (CMake)

This repo aims to create a template upon which to build a GUI App with Qt6

First setup with CMake can be daunting (it was for me at least) so this helps you get started with it pain free!

## Requirements

- CMake >= 3.16
- Qt6
- C++17 compatible compiler
- Python >= 3.13 (if you use the  build script)

## Build

Execute the provided `build.py` script (requires Python >= 3.13)

```sh
./build.py
```

You can also run CMake by yourself (look at the script for examples)

## Arguments

The build script takes a few optional arguments:

- `release` : builds in release mode
- `clean` : makes a clean build
- `ninja` : forces CMake to use Ninja as a build tool

## Project structure

Place headers(.h) in the `include/` directory and source (.cpp) in the `src/` directory.

## Changing the project's name

This can be done in the `CMakeLists.txt` file by changing the line

```cmake
project(QtGuiApp LANGUAGES CXX)
```

Replace `QtGuiApp` with your project's name.
