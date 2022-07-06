#문자열
sentence1 = '나는 소년입니다'
print(sentence1)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "000714-1234567"
print("성별:", jumin[7])
print("연:", jumin[0:2])  #0부터 2직전까지 (0, 1)
print("월:", jumin[2:4])
print("일:", jumin[4:6])
print("생년월일:", jumin[:6])  #처음부터 6직전까지
print("뒤 7자리:", jumin[7:])  #7부터 끝까지
print("뒤 7자리 (뒤에부터):", jumin[-7:])  #맨 뒤에서 7번째부터 끝까지

#문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))     #-1
  #print(python.index("Java"))    #error

print(python.count("n"))

#문자열포맷
print("a" + "b")
print("a", "b")
 #방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
 #방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
 #방법 3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))
 #방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
print("백문이 불여일견\n백견이 불여일타")  # \n: 줄바꿈
print("저는 \"나도코딩\"입니다.")  # \", \' : 문장 내에서 따옴표
print('저는 "나도코딩"입니다.')
print("C:\\Users\\82104\\Desktop\\python>")  # \\ : 문장 내에서 \
print("Red Apple\rPine")  #\r : 커서를 맨 앞으로 이동
print("Redd\bApple")  # \b : 백스페이스 (한 글자 삭제)
print("Red\tApple")  # \t : 탭
