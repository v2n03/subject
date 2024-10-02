# 두 정수 입력 받기
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

# 덧셈과 뺄셈 계산
sum_result = num1 + num2
sub_result = num1 - num2
# 덧셈, 뺄셈, 곱셈, 나눗셈 계산 추가
mul_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "나눗셈 불가"

# 결과 출력 추가
print(f"두 수의 곱: {mul_result}")
print(f"두 수의 나눗셈: {div_result}")

# 결과 출력
print(f"두 수의 합: {sum_result}")
print(f"두 수의 차: {sub_result}")
