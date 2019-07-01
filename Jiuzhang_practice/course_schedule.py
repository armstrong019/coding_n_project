from collections import deque


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        in_degree = {x: 0 for x in range(numCourses)}  # number of classes taken before can take class i
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            in_degree[course] += 1

        course_elig = {x: [] for x in range(numCourses)}  # after taken i which class can we take
        for i in range(len(prerequisites)):
            course = prerequisites[i][1]
            course_elig[course].append(prerequisites[i][0])

        q = deque([])
        for c in in_degree.keys():
            if in_degree[c] == 0:
                q.append(c)

        while q:
            course_taken = q.popleft()
            next_classes_can_take = course_elig[course_taken]
            for course in next_classes_can_take:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    q.append(course)

        if any(in_degree.values()):
            return False
        else:
            return True

#这道题要记录两部分 第一部分是in——degree， 记录修辞课程需要修的课程数目（左边的）
# 第二部分是course——eligibility 记录的是如果此门课程已经take 那么那些课程就可以take了 （右边的）