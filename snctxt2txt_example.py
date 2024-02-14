import snctxt2txt
from glob import glob


if __name__ == "__main__":
    # Search for all snctxt files in the current directory, but only pick the first one...will still work if only one file in dir...so only repro
    files_in = glob("*.snctxt")
    for file in files_in:
        #Name out file whatever in file is but as txt file
        file_out = f"{file.split('.')[0]}.txt"

        # Pattern here is for start-extraction and end-extraction...basically when to roll camera and when to cut.
        pattern = ['BEGIN DOSE TABLE','END DOSE TABLE']

        # Read snctxt file
        with open (file,'r') as f:    
            in_data = f.readlines()
        out_data = snctxt2txt.process_data(in_data, pattern)

        # To clean and remove tab indent
	# Slicing appears to be valid here as even normalise then smooth only has single line under begin dose table flag
        out_data = [x[1:] for x in out_data]
                        
        # Writing data out to txt                
        with open (file_out,'w') as f:
            f.writelines(out_data)