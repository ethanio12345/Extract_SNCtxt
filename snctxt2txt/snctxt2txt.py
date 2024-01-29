from glob import glob

def process_data(in_data,pattern):
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
