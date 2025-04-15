#!/usr/bin/env python3

import subprocess
import argparse
import os
import pathlib
import shutil

class Args:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser()
        parser.add_argument('--clean', action='store_true') #create a clean build (remove old build files)
        parser.add_argument('--ninja', action='store_true') #use Ninja as build tool (recommended)
        parser.add_argument('--release', action='store_true') #create a release build (faster execution but cannot be debuged)
        args_namespace = parser.parse_args()
        self.clean: bool = args_namespace.clean
        self.ninja: bool = args_namespace.ninja
        self.release: bool = args_namespace.release

file_path = pathlib.PurePath(os.path.realpath(__file__))
os.chdir(file_path.parent) #making sure we're in the project's directory

args = Args()

cmake_additionnal_args: list[str] = []
if args.clean:
    if os.path.exists("out"):
        shutil.rmtree("out")
if args.ninja:
    cmake_additionnal_args += ["-G", "Ninja"]
if args.release:
    cmake_additionnal_args += ["-DCMAKE_BUILD_TYPE=Release"]
else:
    cmake_additionnal_args += ["-DCMAKE_BUILD_TYPE=Debug"]

try:
    subprocess.check_call(["cmake", ".", "-B", "out", "-DCMAKE_EXPORT_COMPILE_COMMANDS=1"] + cmake_additionnal_args)
    subprocess.check_call(["cmake", "--build", "out"])
except (subprocess.CalledProcessError) as e:
    print(e)
    exit(1)
