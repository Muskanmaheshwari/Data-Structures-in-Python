# import queue
# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         q = queue.Queue()
#         q.put([root, 0,0])
#         d={}
#         while(not q.empty()):
#             x,y, z = q.get()
#             if z not in d:
#                 d[z] = [x.val]
#             else:
#                 d[z].append(x.val)
#             if x.left!=None:
#                 q.put([x.left, y+1, z-1])
#             if x.right != None:
#                 q.put([x.right, y+1, z+1])
#         a=[]
#         for i , j in sorted(d.items()):
#             a.append(j)
#         return a
import queue


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        q.put([root, 0, 0])
        d = {}
        while (not q.empty()):
            x, y, z = q.get()
            if z not in d:
                d[z] = [[x.val, y]]
            else:
                d[z].append([x.val, y])
            if x.left != None:
                q.put([x.left, y + 1, z - 1])
            if x.right != None:
                q.put([x.right, y + 1, z + 1])
        a = []
        q = {}
        w = []
        for i, j in sorted(d.items()):
            # print(i, j)
            s = []
            for k in sorted(j):
                s.append(k[0])
                print(k[0])
            w.append(s)
        return w

        return