!apt-get install nco
import os
inpo = input('Enter : ')
sys_inp = r'ncks '
sys_inp += inpo
sys_inp += r' /content/output.nc'
os.system(sys_inp)
