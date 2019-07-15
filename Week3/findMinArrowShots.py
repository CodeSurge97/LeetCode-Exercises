def findMinArrowShots(self, points: List[List[int]]) -> int:
        res=1
        if not points:
            return 0
        points=sorted(points,key=lambda x:x[1])        
        right_end=points[0][1]
        for i in points:
            if i[0]>right_end:
                right_end=i[1]
                res+=1
        return res