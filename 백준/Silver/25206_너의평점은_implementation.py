grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
num = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
major = 0
credit_sum = 0
for _ in range(20):
    name, credit, g = input().split()

    if g == "P":
        continue

    credit_sum += float(credit)
    major += float(credit) * num[grade.index(g)]


major = major / credit_sum
print(f"{major:.4f}")
