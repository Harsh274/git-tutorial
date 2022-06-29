# Project 1
# Password Authentication using Python
'''
To create a password authentication system using Python you have to follow the steps mentioned below:

Create a dictionary of usernames with their passwords.
Then you have to ask for user input as the username by using the input function in Python.
Then you have to use the getpass module in Python to ask for user input as the password.
 Here we are using the getpass module instead of the input function to make sure that the user
doesn’t get to see what he/she write in the password field.
'''

'''import getpass
database = {"harshit_joshi": "qwerty123", "joshi_harshit": "hjkl890"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")'''
# Project 2
# Resume Scanner
'''from resume_parser import resumeparse
def scan_resume(resume):
    data = resumeparse.read_file(resume)
    for i, j in data.items():
        print(f"{i}:>>{j}")
    
scan_resume("Harshit Joshi.docx")'''
# Project 3
# Counting each character in string

'''def counting(n):
    d={}
    for x in n:
        d[x]=d.get(x,0)+1
    for x,y in d.items():
        return d
print(counting('accbdee'))'''
'''
n='qnhhcjjshbjjd'
print(nonrepeating(n))
'''
'''class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

    def insert(self,key):
        if self is None:
            self=Node(key)
        if key<self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left=Node(key)
        if key>self.key:
            if self.right:
                self.right.insert(key)
            else:
                self.right=Node(key)
class BinarySearchTree:
    def __init__(self,key):
        self.root=Node(key)
    def insert(self,key):
        self.root.insert=Node(key)'''

'''bst=BinarySearchTree(6)
bst.insert(3)
bst.insert(4)
bst.insert(8)
bst.insert(1)
bst.insert(5)
inorder(bst.root)'''

'''def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key)
        inorder(root.left)
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.key)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
inorder(root)
print()
preorder(root)
print()
postorder(root)
'''