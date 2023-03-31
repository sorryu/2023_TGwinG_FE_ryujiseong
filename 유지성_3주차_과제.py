# 1번
def grade(score:int):
    #your code
    if(score>=90):
        return "A"
    elif(score>=80):
        return "B"
    elif(score>=70):
        return "C"
    elif(score>=60):
        return "D"
    else:
        return "F"
print(grade(94))
print(grade(64))
print(grade(34))


# 2번
def quadrant(x:int, y:int):
    #your code
    if(x>0 and y>0):
        return "제 1사분면"
    elif(x>0 and y<0):
        return "제 2사분면"
    elif(x<0 and y>0):
        return "제 3사분면"
    else:
        return "제 4사분면"

print(quadrant(1,3))
print(quadrant(-1,3))
print(quadrant(-1,-3))
print(quadrant(1,-3))

# 3번
def leapYear(year:int):
    # your code
    if(year%4==0 and year%100!=0 or year%400==0):
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."
print(leapYear(2024))
print(leapYear(1900))
print(leapYear(2000))
print(leapYear(2023))

# 4번
def dice(a, b, c):
    # your code
    i = [a, b, c]
    i.sort()
    if(i[0]==i[1]==i[2]):
        return 10000+1000*i[0]
    elif(i[0]==i[1] or i[1]==i[2]):
        return 1000+100*i[1]
    else:
        return 100*i[2]
print(dice(3,3,6))
print(dice(2,2,2))
print(dice(6,2,5))


# 5번
def alarm(time:int):
    # your code
    if(time<45):
        return f"23시 {time+15}분"
    elif(time<60):
        return f"0시 {time-45}분"
    elif(int(str(time)[-2:])<45):
        return f"{str(time+9900)[-4:-2]}시 {str(time+15)[-2:]}분"
    else:
        return f"{str(time+10000)[-4:-2]}시 {str(time-45)[-2:]}분"
print(alarm(900))
print(alarm(30))
print(alarm(2315))
print(alarm(1050))