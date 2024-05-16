# menangkap  banyak exception sekaligus
try:
    total_banana = int(input("total banana:"))
    total_people = int(input("number of person:"))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except (ValueError, ZeroDivisionError):
    print("oops! something wrong")

# menangkap semua exception
try:
    total_banana = int(input("total banana:"))
    total_people = int(input("number of person:"))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except Exception:
    print("oops! something wrong")

# memunculkan pesan exception
try:
    total_banana = int(input("total banana"))
    total_people = int(input("number of person:"))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except ValueError as err:
    print(f"oops! not valid number detected. {err}")
except ZeroDivisionError as err:
    print(f"oops! unable to distribute banana because there is no person available. {err}")
except Exception as err:
    print(f"oops! something error. {err}")

# alternatif penulisan exception
try:
    total_banana = int(input("total banana:"))
    total_people = int(input("total people:"))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except Exception as err:
    if err == ValueError:
        print(f"oops! not valid number detected. {err}")
    elif err == ZeroDivisionError:
        print(f"oops! unable to distribute banana because there is no person available. {err}")
    else:
        print(f"oops! something wrong. {err}")

# refactor kode try, except dan else
try:
    total_banana = int(input("total banana:"))
    total_people = int(input("total people:"))
    res = total_banana / total_people
except ValueError as err:
        print(f"oops! not valid number detected. {err}")
except ZeroDivisionError as err:
        print(f"oops! unable to distribute banana because there is no person available. {err}")
except Exception as err:
        print(f"oops! something wrong. {err}")
else:
        print(f"in fair distribution, each person shall receive {res:.0f} banana")

# keyword try, except & finally
try:
    total_banana = int(input("total banana:"))
    total_people = int(input("total people:"))
    res = total_banana / total_people
    print(f"in fair distribution, each person shall receive {res:.0f} banana")
except ValueError as err:
        print(f"oops! not valid number detected. {err}")
except ZeroDivisionError as err:
        print(f"oops! unable to distribute banana because there is no person available. {err}")
except Exception as err:
        print(f"oops! something wrong. {err}")
finally:
       print("program completed") 

# keyword try, except, else & finally
try:
    total_banana = int(input("total banana:"))
    total_people = int(input("total people:"))
    res = total_banana / total_people
except ValueError as err:
        print(f"oops! not valid number detected. {err}")
except ZeroDivisionError as err:
        print(f"oops! unable to distribute banana because there is no person available. {err}")
except Exception as err:
        print(f"oops! something wrong. {err}")
else:
     print(f"in fair distribution, each person shall receive {res:.0f} banana") 
finally:
       print("program completed") 