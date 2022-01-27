#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

def cli():
        parser = ArgumentParser()
        parser.add_argument(
            "-i",
            "--input_file", 
            required=False,
            help="File to be converted"
        )
        parser.add_argument(
            "-o",
            "--output_file",
            required=False,
            help="Path for the converted file"
        )
        args = parser.parse_args()

        Main(args.input_file, args.output_file)


class Main():
    def __init__(self, input_file, output_file):

        self.input_file = input_file
        self.output_file = output_file

        self.start(self.input_file, self.output_file)


    def start(self, a, b):
        print(a)
        print(b)


if __name__ == "__main__":
    cli()
