!sudo apt install netcdf-bin
import os
var=input()
system_input=r'ncdump -b c '
system_input+=var
system_input+=r' > '
system_input+=r'final.cdl'
os.system(system_input)
