try:
    total_banana = int(input("total input:"))
    total_people = int(input("number of person:"))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except ValueError:
    print("oops! not valid number detected")
except ZeroDivisionError:
    print("oops! unable to distribute banana because there is no person available")