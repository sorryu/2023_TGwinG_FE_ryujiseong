# 1번
def sum(a, b):
    # your code
    return a+b

# 2번
def sub(a, b):
    # your code
    return a-b

# 3번
def mul(a, b):
    # your code
    return a*b

# 4번
def div(a, b):
    # your code
    return a/b

# 5번
def distance(x1, y1, x2, y2):
    # your code
    return ((x1-x2)**2-(y1-y2)**2)**(1/2)

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    # your code
    return lylics[-11:-1]

# 7번
def reverseStr(string):
    # your code
    return string[::-1]

# 8번
def introduce():
    # your code
    name = input("이름을 입력하세요 : ")
    hobby = input("취미를 입력하세요 : ")
    school = input("재학 중인 학교를 입력하세요 : ")
    birth = input("생년월일을 입력하세요(6자리) : ")
    print(f"제 이름은 {name}입니다. 취미는 {hobby}입니다. 저는 {school}를 다니고 있습니다. 제 생일은 {birth[2:4]}월 {birth[4:]}입니다.")
    return

# 9번
def calc():
    # your code
    a, b=input("첫 번째 수를 입력하세요 : "), input("두 번째 수를 입력하세요 : ")
    a, b= int(a),int(b)
    print(f'두 수의 합 : {a+b}\n두 수의 차 : {a-b}\n두 수의 곱 : {a*b}\n두 수의 몫 : {a//b}')
    return