class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        answer = []

        for item in strs:
            anagram = "".join(sorted(item))
            if anagram not in myDict:
                myDict[anagram] = [item]
            else:
                myDict[anagram].append(item)

        for item in myDict:
            answer.append(myDict[item])

        return answer

        # 1. 각 알파벳들을 쪼개서 정렬
        # 2. {애너그램: 원래문자열} 형태로 딕셔너리 삽입
        # 3. 같이 묶여있는 값들 리스트에 삽입 => 리스트 형태로 출력해야하므로      
  