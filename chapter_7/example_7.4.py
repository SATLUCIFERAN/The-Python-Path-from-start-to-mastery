
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
else:
    print("All went well!")
finally:
    print("Execution complete.")


# Enter a number: 10
# 10.0
# All went well!
# Execution complete.


# Enter a number: Obiwan
# Error: invalid literal for int() with base 10: 'Obiwan'
# Execution complete.