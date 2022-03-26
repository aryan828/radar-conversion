#!/usr/bin/python3

import os
import subprocess
from tkinter import *
from tkinter import filedialog


class RadarConversion():
    def __init__(self, master):
        self.file_label = None
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
        self.h5_to_nc = Button(self.master, text="Convert to NetCDF", command=self.convert_to_nc)
        self.h5_to_ascii = Button(self.master, text="Convert to ASCII", command=self.convert_to_ascii)
        self.nc_to_h5 = Button(self.master, text="Convert to HDF5", command=self.convert_to_h5)
        self.nc_to_ascii = Button(self.master, text="Convert to ASCII", command=self.convert_to_ascii)

    def pack_widgets(self):
        self.label.pack(padx=10, pady=10)
        self.button.pack()

    def select_file(self):
        if self.file_label is not None:
            self.file_label.destroy()
        if self.nc_to_ascii is not None:
            self.nc_to_ascii.pack_forget()
        if self.h5_to_ascii is not None:
            self.h5_to_ascii.pack_forget()
        if self.nc_to_h5 is not None:
            self.nc_to_h5.pack_forget()
        if self.h5_to_nc is not None:
            self.h5_to_nc.pack_forget()

        self.selected_file = filedialog.askopenfilename(initialdir="~/Downloads", title="Select file",
                                                        filetypes=(("HDF5", "*.h5"), ("NetCDF", "*.nc")))
        if self.selected_file:
            self.selected_file_format = self.selected_file.split(".")[-1]
            self.file_label = Label(self.master, text='Selected File:\n' + self.selected_file)
            self.file_label.pack(padx=10, pady=10)
            if self.selected_file_format == "h5":
                self.h5_to_nc.pack(side=LEFT, padx=10)
                self.h5_to_ascii.pack(side=RIGHT, padx=10)
            elif self.selected_file_format == "nc":
                self.nc_to_h5.pack(side=LEFT, padx=10)
                self.nc_to_ascii.pack(side=RIGHT, padx=10)
            else:
                print("File format not supported")

    def convert_to_nc(self):
        out = ' ' + self.selected_file.split(".")[0] + ".nc"
        sys_inp = r'ncks '
        sys_inp += self.selected_file
        sys_inp += out
        os.system(sys_inp)

    def convert_to_ascii(self):
        if self.selected_file_format == 'nc':
            out = self.selected_file.split(".")[0] + ".cdl"
            system_input = r'ncdump -b c '
            system_input += self.selected_file
            system_input += r' > '
            system_input += out
            os.system(system_input)
        elif self.selected_file_format == 'h5':
            system_input = r'h5dump --ddl='
            system_input += self.selected_file.split(".")[0] + "_ddl.txt "
            system_input += r'-o ' + self.selected_file.split(".")[0] + "_raw.txt "
            system_input += self.selected_file
            os.system(system_input)

    def convert_to_h5(self):
        result = str(subprocess.check_output(['ncdump', '-k', self.selected_file]).strip())
        print(result, type(result))
        if result == "b'classic'" or result == "b'64-bit offset'":
            inter = self.selected_file.split(".")[0] + "_intermediate.nc"
            system_input = r'nccopy -k 4 '
            system_input += self.selected_file
            system_input += r' '
            system_input += inter
            os.system(system_input)
            os.system(r'cp ' + inter + ' ' + self.selected_file.split(".")[0] + ".h5")
            os.system(r'rm ' + inter)
        elif result == "b'netCDF-4'" or result == "b'netCDF-4 classic model'":
            os.system(r'cp ' + self.selected_file + ' ' + self.selected_file.split(".")[0] + ".h5")


root = Tk()
app = RadarConversion(root)
root.mainloop()
