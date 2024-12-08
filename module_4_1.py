from fake_math import divide as FDiv
from true_math import divide as Tdiv

result1 = FDiv(69, 3)
result2 = FDiv(3, 0)
result3 = Tdiv(49, 7)
result4 = Tdiv(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)