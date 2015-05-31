class CNVData(object):

    def __init__(self):
        pass


    def get_sample_count(self):
        return len(self.cnv_intervals['sample'].unique())


    def get_contigs(self):
        return self.cnv_intervals['chr'].unique()