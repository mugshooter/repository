class BinaryTreeException(Exception):
    """Basic class for binary tree exceptions"""

class HeightSubZeroException(BinaryTreeException):
    """Exception for height below zero"""

class InvalidRootArgumentException(BinaryTreeException):
    """Exception for invalid root argument"""
