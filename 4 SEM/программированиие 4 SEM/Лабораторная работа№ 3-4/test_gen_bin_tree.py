from gen_bin_tree import gen_bin_tree_recursive, gen_bin_tree_non_recursive
from exceptions import BinaryTreeException, HeightSubZeroException
import pytest

def test_type_of_zero_height_tree():
    assert type(gen_bin_tree_recursive(root=5, height=0)['5']) is list
    assert type(gen_bin_tree_non_recursive(root=5, height=0)['5']) is list

def test_val_tree_with_zero_height():
    assert gen_bin_tree_recursive(root=5, height=0) == {'5': []}
    assert gen_bin_tree_non_recursive(root=5, height=0) == {'5': []}

def test_val_tree_with_height_equals_to_one():
    assert gen_bin_tree_recursive(root=5, height=1) == {'5': [{'8': []}, {'10': []}]}
    assert gen_bin_tree_non_recursive(root=5, height=1) == {'5': [{'8': []}, {'10': []}]}

def test_val_tree_with_height_equals_to_two():
    assert gen_bin_tree_recursive(root=5, height=2) == {
        '5': [{
            '8': [{
                '11': []
            }, {
                '16': []
            }]
        }, {
            '10': [{
                '13': []
            }, {
                '20': []
            }]
        }]
    }
    
    assert gen_bin_tree_non_recursive(root=5, height=2) == {
        '5': [{
            '8': [{
                '11': []
            }, {
                '16': []
            }]
        }, {
            '10': [{
                '13': []
            }, {
                '20': []
            }]
        }]
    }

def test_negative_height_raises_exception():
    with pytest.raises(HeightSubZeroException):
        gen_bin_tree_recursive(root=5, height=-1)
    with pytest.raises(HeightSubZeroException):
        gen_bin_tree_non_recursive(root=5, height=-1)
