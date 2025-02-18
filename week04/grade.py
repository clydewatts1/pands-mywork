percentage = int(input("Enter the percentage: "))
if percentage < 40:
    print("Under 40=>Fail")
elif percentage <=49:
    print("Between 40% and 49%=>Pass")
elif percentage <= 59:
    print("Between 50% and 59%=>Merit 2")
elif percentage <= 69:
    print("Between 60% and 69%=>Merit 1")
else:
    print("Over 70%=>Distinction")