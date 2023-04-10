# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    count = 0
    lst.sort()
    for i in range(len(lst)):
        if lst[i]*2 in lst:
            count += 1
        else:
            continue
    return count

# 2번
def pascal(n):
    pasTri = []
    for i in range(n):
        pasTri.append(1)
        pasTri2 = pasTri.copy()
        if i == 0 or i == 1:
            continue
        else:
            for j in range(1, i):
                pasTri2[j] = pasTri[j-1]+pasTri[j]
        pasTri = pasTri2
    return pasTri2
print(pascal(3))

# 3번
def beerRefrigerator(n):
    a = []
    for j in range(3,0,-1):
        for i in range(1,n+1):
            if n%i==0 and i**j>=n:
                a.append(i)
                n=n//i
                break
    a.sort()
    return a
print(beerRefrigerator(12))

# 4번
def matrixMul(mat1, mat2):
    def swapRC(matrix):
        mat = []
        for i in range(len(matrix[0])):
            mat.append([])
            for j in range(len(matrix)):
                mat[i].append(matrix[j][i])
        return mat
    def mulRC(a,b):
        c = 0
        for i in range(len(a)):
            c += a[i]*b[i]
        return c
    mat = []
    mat2 = swapRC(mat2)
    for i in range(len(mat1)):
        mat.append([])
        for j in range(len(mat2)):
            mat[i].append(mulRC(mat1[i],mat2[j]))
    return mat