# Example taken from Gries et al. 2013. Practical Programming: An Introduction to Computer Science Using Python 3

import unittest
import tools

class TestRunningSum(unittest.TestCase):
    '''Tests for running_sum.'''

    def test_running_sum_empty(self):
        '''Test an empty list.'''
        argument = []
        expected = []
        tools.running_sum(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_running_sum_one(self):
        '''Test a one-item list.'''
        argument = [2]
        expected = [2]
        tools.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_running_sum_two(self):
        '''Test a two-item list.'''
        argument = [2, 5]
        expected = [2, 7]
        tools.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_sum_multi_neg(self):
        '''Test a list of negative values.'''
        argument = [-1, -5, -3, -4]
        expected = [-1, -6, -9, -13]
        tools.running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only negative values.")

    def test_running_sum_multi_zeros(self):
        '''Test a list of zeros.'''
        input = [0, 0, 0, 0]
        output = tools.running_sum(input)
        output_expected = [0, 0, 0, 0]
        self.assertEqual(output_expected, output, "Not working with zeros.")

    def test_running_sum_multi_pos(self):
        '''Test a list of positive values.'''
        input = [4, 2, 3, 6]
        output = tools.running_sum(input)
        output_expected = [4, 6, 9, 15]
        self.assertEqual(output_expected, output, "Not working with positive values.")

    def test_running_sum_multi_mix(self):
        '''Test a list of mixed values.'''
        input = [4, 0, 2, -5]
        output = tools.running_sum(input)
        output_expected = [4, 4, 6, 1]
        self.assertEqual(output_expected, output, "Not working with mixed values.")

if __name__ == '__main__':
    unittest.main()
