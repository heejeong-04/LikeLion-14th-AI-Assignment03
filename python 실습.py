scores = [85, 92, 55, 78, 40, 96, 73]

# 총 학생 수 출력
print(f"총 학생 수: {len(scores)}명")

# 통계
print(f"최고점: {max(scores)}점")
print(f"최저점: {min(scores)}점")
print(f"평균: {sum(scores)/len(scores):.1f}점")

# 점수별 등급 출력
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"점수: {score} -> {grade}학점")

# 정렬 후 상위 3개
scores.sort(reverse=True)
print(f"상위 3개: {scores[:3]}")