print("{:5d}".format(12)) # field bit
print("{:2d}".format(1234))
print("{:8.3f}".format(12.2346)) # 8 fields, where 4 are before decimal, 1 is ., 3 are decimal
print("{:05d}".format(12)) # padding field with 0
print("{:08.3f}".format(12.2346)) # padding remaining with 0
print("{:^10.3f}".format(12.2346)) # center align
print("{:<05d}".format(12)) # left align
print("{:>08.3f}".format(12.2346)) # right align
print("{:=8.3f}".format(-12.2346)) # sign on leftmost
print("Hello {} your balance is {}".format("Dayeem", 10))
# print(f"Hello {} your balance is {}", "Dayeem", 10)
