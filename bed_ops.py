import subprocess

def merge_bed(bed_path):
    '''

    :param bed_path: path to a sorted BED-format file
    :return: a DataFrame describing the viewing coordinates for the overlay
    '''

    #TODO: call out to BEDtools

    # temporary mock of this process:
    import pandas as pd
    merged_coords = pd.read_table("merged.bed", sep = "\t", header = None, names = ["chr", "start", "stop"])
    return merged_coords
