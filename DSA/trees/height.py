#
# Complete the 'getBinarySearchTreeHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY leftChild
#  3. INTEGER_ARRAY rightChild
#

def getBinarySearchTreeHeight(values, leftChild, rightChild):
    return get_height(0, values, leftChild, rightChild)

def get_height(i, values, leftChild, rightChild):
    if leftChild[i] == -1 and rightChild[i] == -1:
        return 1
    elif leftChild[i] == -1:
        return 1 + get_height(rightChild[i], values, leftChild, rightChild)
    elif rightChild[i] == -1:
        return 1 + get_height(leftChild[i], values, leftChild, rightChild)
    else:
        return 1 + max(get_height(leftChild[i], values, leftChild, rightChild), get_height(rightChild[i], values, leftChild, rightChild))

'''
7
4 2 6 1 3 5 7
7
1 3 5 -1 -1 -1 -1
7
2 4 6 -1 -1 -1 -1
'''

if __name__ == '__main__':
    values_count = int(input().strip())
    values = [int(i) for i in input().strip().split()]

    leftChild_count = int(input().strip())
    leftChild = [int(i) for i in input().strip().split()]

    rightChild_count = int(input().strip())
    rightChild = [int(i) for i in input().strip().split()]

    result = getBinarySearchTreeHeight(values, leftChild, rightChild)

    print(result)
