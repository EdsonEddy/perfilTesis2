from .local_moss_edited import local_moss
class Wf_algorithm:
    def __init__(self, file_name_a, file_name_b, window, kgrams):
        paths = [file_name_a, file_name_b]
        self.args = {}
        self.args["paths"] = paths
        self.args["language"] =None
        self.args["collision_threshold"] = 10
        self.args["window_size"] = window
        self.args["kgram_len"] = kgrams

    def get_per_similarity(self):
        try:
            percentage = local_moss(self.args)
        except Exception as e:
            percentage = 0
        return percentage



