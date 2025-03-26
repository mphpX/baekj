import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []

while True:
    try:
        data = int(input())
        preorder.append(data)
    except:
        break

def postorder(li, start, end):
    if start > end:
        return

    root = li[start]
    mid = start + 1

    while mid <= end and li[mid] < root:
        mid += 1

    postorder(li, start + 1, mid - 1)  # 왼쪽 서브트리
    postorder(li, mid, end)           # 오른쪽 서브트리
    print(root)                       # 루트 (후위 순회 출력)

postorder(preorder, 0, len(preorder) - 1)
