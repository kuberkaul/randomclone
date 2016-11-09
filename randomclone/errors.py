"""
Error class for randomclone
"""

#creating a class of errors for randomclone
class RandomCloneResourceError(Exception):
    def __init__(self, error_string):
        super(RandomCloneResourceError, self).__init__(error_string)
