# https://programmers.co.kr/learn/courses/30/lessons/49993
# 큐를 사용하여 스킬트리 순서와 맞는지 확인

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    
    for i in skill_trees:
        queue = deque()
        for s in i:
            if s in skill:
                queue.append(s)
        isOk = True      
        for i in range(len(queue)):
            isOk = queue.popleft() == skill[i] and isOk
        if isOk:
            answer += 1
    
    
    return answer
