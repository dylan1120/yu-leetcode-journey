import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import importlib
module = importlib.import_module("python.string.0443_string_compression")
Solution = module.Solution

def test():
    s = Solution()
    s.compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']) == 6
    s.compress(['a']) == 1
    s.compress(['a', 'b']) == 2
    s.compress(['a', 'a', 'a', 'b', 'b', 'a', 'a']) == 6
    s.compress(['a', 'b', 'c', 'd', 'e']) == 5
    print('✅ Passed all test cases')

if __name__ == '__main__':
    test()
