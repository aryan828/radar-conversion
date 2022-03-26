#!/usr/bin/python3

import os
import sys
from tkinter import *
from tkinter import filedialog


class RadarConversion():
    def __init__(self, master):
        self.nc_to_ascii = None
        self.h5_to_ascii = None
        self.nc_to_h5 = None
        self.h5_to_nc = None
        self.button = None
        self.label = None
        self.selected_file = None
        self.selected_file_format = None
        self.master = master
        master.title("Radar Conversion")
        master.geometry("400x200")
        master.resizable(False, False)
        self.create_widgets()
        self.pack_widgets()

    def create_widgets(self):
        self.label = Label(self.master, text="Select a file to convert")
        self.button = Button(self.master, text="Select File", command=self.select_file)
        self.h5_to_nc = Button(self.master, text="Convert", command=self.convert_to_nc)
        self.h5_to_ascii = Button(self.master, text="Convert to ASCII", command=self.convert_to_ascii)
        self.nc_to_h5 = Button(self.master, text="Convert to HDF5", command=self.convert_to_h5)
        self.nc_to_ascii = Button(self.master, text="Convert to ASCII", command=self.convert_to_ascii)

    def pack_widgets(self):
        self.label.pack(padx=10, pady=10)
        self.button.pack()

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(initialdir="~", title="Select file",
                                                        filetypes=(("HDF5", "*.h5"), ("NetCDF", "*.nc")))
        if self.selected_file:
            self.selected_file_format = self.selected_file.split(".")[-1]
            label = Label(self.master, text='Selected File:\n' + self.selected_file)
            label.pack(padx=10, pady=10)
            if self.selected_file_format == "h5":
                self.h5_to_nc.pack(side=LEFT, padx=10)
                self.h5_to_ascii.pack(side=RIGHT, padx=10)
            elif self.selected_file_format == "nc":
                self.nc_to_h5.pack(side=LEFT, padx=10)
                self.nc_to_ascii.pack(side=RIGHT, padx=10)
            else:
                print("File format not supported")

    def convert_to_nc(self):
        sys_inp = r'ncks '
        sys_inp += self.selected_file
        sys_inp += r'output.nc'
        os.system(sys_inp)

    def convert_to_ascii(self):
        if self.selected_file_format == 'nc':
            system_input = r'ncdump -b c '
            system_input += self.selected_file
            system_input += r' > '
            system_input += r'output.cdl'
            os.system(system_input)
        elif self.selected_file_format == 'h5':
            system_input = r'h5dump -o output.cdl -y -w 4000 '
            system_input += self.selected_file

    # TODO: Add convert to h5
    def convert_to_h5(self):
        pass


root = Tk()
app = RadarConversion(root)
root.mainloop()
