import matplotlib.pyplot as plt

class Artist(object):


    def __init__(self, data_factory, *args, **kwargs):
        self.data_factory = data_factory
        self.setup_figure(*args, **kwargs)


    def setup_figure(self, *args, **kwargs):
        self.figure = plt.figure(*args, **kwargs)
        self.axes = self.figure.add_subplot(111)


    def draw(self):
        cnv_intervals = self.data_factory.data
        all_view_intervals = self.data_factory.viewing_intervals
        num_samples = self.data_factory.get_sample_count()

        # subset to get everything on a chromosome/contig level
        all_contigs = self.data_factory.get_contigs()
        for chr in all_contigs:
            chr_view_intervals = all_view_intervals[all_view_intervals['chr'] == chr]

            for i, view_interval in chr_view_intervals.iterrows():
                current_cnv_intervals = cnv_intervals[(cnv_intervals['chr'] == chr)
                                                      & (cnv_intervals['start'] >= view_interval['start'])
                                                      & (cnv_intervals['stop'] <= view_interval['stop'])]
                # plot these.  Remember that we need to subtract the cnv_intervals.stop from the prior viewing interval.
                # This way, the next viewing window ends up directly adjacent to the previous, cutting out the dead space
                # in between each viewing_interval