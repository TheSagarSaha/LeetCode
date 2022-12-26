class Solution:
    def average(self, salary: List[int]) -> float:
        max = -1
        min = 100001
        ind1 = -1
        ind2 = -1
        for i in range(len(salary)):
            if max < salary[i]:
                ind1 = i
                max = salary[i]
            if salary[i] < min:
                ind2 = i
                min = salary[i]
        count = 0
        total = 0
        for i in range(len(salary)):
            if i != ind1 and i != ind2:
                total += salary[i]
                count += 1
        return total/count
