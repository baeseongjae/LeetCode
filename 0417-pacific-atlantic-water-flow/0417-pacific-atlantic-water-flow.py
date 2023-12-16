from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]    #동, 서 남, 북
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)

            while queue:
                curX, curY = queue.popleft()
                for dx, dy in d:
                    nx = curX + dx
                    ny = curY + dy

                    # 육지내에 속하고, 방문하지 않았고, 이전 셀의 높이보다 높아야함.
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and heights[nx][ny] >= heights[curX][curY]:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            
            return visited

        # 각 바다와 인접한부분의 좌표를 각 바다의 스타트 배열로 만든다.
        pStart = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        aStart = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]

        pacific = bfs(pStart)
        atlantic = bfs(aStart)
    
        return list(pacific & atlantic) # 교집합 구해서 리스트 변환.
        # 핵심 아이디어: BFS
    
        # for문 돌려서 각지점에서 BFS 전부 시행??
        # 아틀란틱 => 우, 하 / 패시픽 -> 좌, 상 인데 체크조건을 어떻게 잡아야할까??

