class Tree:
    # def __init(self):
    #     self.val = None
    #     self.left = None
    #     self.right = None
        
    def __init__(self, val=None):
        if val != None:
            self.val = val     
        else:
            self.val = None         
        self.left =None
        self.right = None  
        
        
tree = Tree()

print(tree)       
        