import re
from glob import glob
from pathlib import Path


if __name__ == "__main__":
    # Search for all snctxt files in the current directory, but only pick the first one...will still work if only one file in dir...so only repro
    files_in = [Path(x) for x in glob("*.snctxt")]
    for i, file in enumerate(files_in):
        print(file.name)

        # Pattern here is for start-extraction and end-extraction...basically when to roll camera and when to cut.
        scan_pattern = re.compile('BEGIN SCAN(.*?)END SCAN', re.DOTALL)
        dose_table_pattern = re.compile('BEGIN DOSE TABLE(.*?)END DOSE TABLE', re.DOTALL)

        # Read snctxt file
        with open (file,'r') as f:    
            in_data_str = f.read()

        # Don't need to finish at end of scan, just split at beginning
        in_data_scans = scan_pattern.findall(in_data_str)

        for i, scan in enumerate(in_data_scans):

            dose_table = dose_table_pattern.findall(scan)[0].splitlines()
            # To clean and remove tab indent
            # Slicing appears to be valid here as even normalise then smooth only has single line under begin dose table flag
            out_data = [x + "\n" for x in dose_table[2:]]
            summary_data = [x + "\n" for x in scan.splitlines() if "Summary" in x]
            # Writing data out to txt                
            with open ((file.parent / f"{file.stem}_{i}.txt"),'w') as f:
                f.writelines(summary_data)
                f.write("\n")
                f.writelines(out_data)




    
