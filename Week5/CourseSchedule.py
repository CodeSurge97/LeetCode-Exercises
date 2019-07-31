def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for course,pre_course in prerequisites:
            graph[course].append(pre_course)
  
        def DFS(course,seen):
			# if node have been traveled
            if seen[course]==0:
                return False
            elif seen[course]==1:
                return True
            
            seen[course] = 1
            for pre_course in graph[course]:  
                if DFS(pre_course,seen):
                    seen[course] = 0
                    return True
            seen[course] = 0
       
            return False
			
        seen = {i:-1 for i in range(numCourses)}    
        for course in range(numCourses):         
            if DFS(course,seen):
                return False
        return True