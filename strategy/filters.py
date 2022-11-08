from .filter_interface import FilterInterface


class BlackAndWhiteFilter(FilterInterface):
    def apply(self, fileName):
        print("Applying B&W filter")
        