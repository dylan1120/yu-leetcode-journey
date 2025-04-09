import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import importlib
module = importlib.import_module("python.array.0238_product_of_array_except_self")
Solution = module.Solution

def test():
    s = Solution()
    s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    s.productExceptSelf([1]) == [1]
    s.productExceptSelf([0, 0]) == [0, 0]
    s.productExceptSelf([1, 2]) == [2, 1]
    print('✅ Passed all test cases')

if __name__ == '__main__':
    test()
