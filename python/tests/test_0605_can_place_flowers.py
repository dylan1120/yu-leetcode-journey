import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import importlib
module = importlib.import_module("python.array.0605_can_place_flowers")
Solution = module.Solution

def test():
    s = Solution()
    # Test cases
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
    assert s.canPlaceFlowers([0, 0, 1, 0, 1], 1) == True
    assert s.canPlaceFlowers([0, 0, 0, 0, 1], 2) == True
    assert s.canPlaceFlowers([0, 0, 0, 0, 0], 3) == True
    print('✅ Passed all test cases')

if __name__ == '__main__':
    test()
