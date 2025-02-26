n=int(input())
tree={}
def preorder(node):
    if(node =='.'):
        return
    print(node,end='')        
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if(node == '.'):
        return
    inorder(tree[node][0])
    print(node,end='')        
    inorder(tree[node][1])

def postorder(node):
    if(node== '.'):
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node,end='')        

for i in range(n):
    a,b,c=map(str,input().split())
    tree[a]=(b,c)
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()