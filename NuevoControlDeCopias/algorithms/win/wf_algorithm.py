from .local_moss_edited import local_moss

class WF_algorithm:
	def __init__(self, file_name_a, file_name_b, window, kgrams):
		self.file_name_a = file_name_a
		self.file_name_b = file_name_b
		self.window = window
		self.kgrams = kgrams

	def get_per_similarity(self):
		paths = [self.file_name_a, self.file_name_b]
		try:
			percentage = local_moss(paths, self.window, self.kgrams)
		except Exception as e:
			percentage = 0.00
		return percentage