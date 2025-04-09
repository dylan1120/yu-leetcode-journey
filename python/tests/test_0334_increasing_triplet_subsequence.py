import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import importlib
module = importlib.import_module("python.array.0334_increasing_triplet_subsequence")
Solution = module.Solution

def test():
    s = Solution()
    s.increasingTriplet([1, 2, 3, 4, 5]) == True
    s.increasingTriplet([5, 4, 3, 2, 1]) == False
    s.increasingTriplet([2, 1, 5, 0, 4, 6]) == True
    s.increasingTriplet([1, 2, 3]) == True
    s.increasingTriplet([1, 2]) == False
    s.increasingTriplet([1]) == False
    print('✅ Passed all test cases')

if __name__ == '__main__':
    test()
