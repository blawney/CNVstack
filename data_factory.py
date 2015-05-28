import pandas as pd
import bed_ops
from data import CNVData
import numpy as np


class DataFactory(object):

    def __init__(self, bedfile_path):
        self.bedfile_path = bedfile_path
        self.data = CNVData()


    def read_bedfile(self):
        self.data.cnv_intervals = pd.read_table(self.bedfile_path,
                                      sep="\t",
                                      header=None,
                                      names=["chr", "start", "stop", "sample", "score"])


    def get_sample_count(self):
        '''
        Retrieves the number of samples under consideration
        :return: integer giving the number of samples in the BED file
        '''
        return self.data.get_sample_count()


    def read_viewing_windows(self):
        '''
        Calls another method to merge the BED file.  This gets a DataFrame
        with the coordinates of the viewing windows
        :return: None
        '''
        self.viewing_intervals = bed_ops.merge_bed(self.bedfile_path)


    def get_length_of_viewing_windows(self):
        '''
        Counts the number of base pairs in the viewing windows
        :return:
        '''
        # create a Series with the lengths of each window, then index by the chromosome
        window_sizes = pd.Series(self.viewing_intervals["stop"]-self.viewing_intervals["start"])
        window_sizes.index = self.viewing_intervals["chr"]

        # sum the lengths within each chromosome and return in a Series
        return window_sizes.groupby(level="chr").sum()