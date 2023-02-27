import list as exercise1
from inspect import getmembers, isfunction

def main():
    print(getmembers(exercise1, isfunction))
    


main()