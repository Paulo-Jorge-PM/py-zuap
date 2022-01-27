#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from gooey import Gooey, GooeyParser#GUI

@Gooey(
    program_name="Video Converter",
    program_description="Convert between different video formats",
    default_size=(600, 720),
    #navigation="TABBED",
)

def cli():
        #parser = ArgumentParser()
        parser = GooeyParser(description="My Cool Gooey App!")
        parser.add_argument(
            "-i",
            "--input_file", 
            required=False,
            help="File to be converted",

            #Gooey extra arguments:
            widget="FileChooser",
            gooey_options=dict(wildcard="Video files (*.mp4, *.mkv)|*.mp4;*.mkv")
        )
        parser.add_argument(
            "-o",
            "--output_file",
            required=False,
            help="Path for the converted file",

            #Gooey extra arguments:
            widget="FileSaver",
            gooey_options=dict(wildcard="MPEG-4 (.mp4)|*.mp4")

        )
        args = parser.parse_args()

        Main(args.input_file, args.output_file)

'''def cli():
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

        Main(args.input_file, args.output_file)'''


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
