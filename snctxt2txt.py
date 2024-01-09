from glob import glob

def process_data(in_data):
    # Just a tag to tell for loop that we don't want to write data yet. 
    # If conditions check this and check if each line begins with start/end pattern to know we we need to append
    # Also check for if line starts with an action like "normalize", which we don't really care about...just the dose
    in_recording_mode = False
    out_data = []
    for line in in_data:
        if not in_recording_mode:
            if line.startswith(pattern[0]):
                in_recording_mode = True
        elif line.startswith(pattern[1]):
            in_recording_mode = False
        else:
            if line.startswith("Action"):
                pass
            else:
                out_data.append(line)

    return out_data


if __name__ == "__main__":
    # Search for all snctxt files in the current directory, but only pick the first one...will still work if only one file in dir...so only repro
    file_in = glob("*.snctxt")[0]

    #Name out file whatever in file is but as txt file
    file_out = f"{file_in.split('.')[0]}.txt"

    # Pattern here is for start-extraction and end-extraction...basically when to roll camera and when to cut.
    pattern = ['BEGIN DOSE TABLE','END DOSE TABLE']

    # Read snctxt file
    with open (file_in,'r') as f:    
        in_data = f.readlines()
    
    out_data = process_data(in_data)

    # To clean and remove tab indent
    out_data = [x[1:] for x in out_data]
                    
    # Writing data out to txt                
    with open (file_out,'w') as f:
        f.writelines(out_data)
