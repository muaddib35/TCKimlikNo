"""
    @author Mehmet Arun
    @date   2020-04-22
    @version 1.0

"""

def verify_turkish_citizen_id(citizen_id: int):
    """
    Verifies the turkish citizen id
    :param citizen_id: int
    """    
    if len(str(citizen_id)) != 11:
        return False

    for x in range(0,11):
        try:
            int(str(citizen_id)[x])
        except ValueError:
            return False

    if str(citizen_id)[0] == '0':
        return False

    total_even = 0
    total_odd = 0
    for x in range(0,9):
        if x % 2 == 0:
            total_even += int(str(citizen_id)[x])
        else:
            total_odd += int(str(citizen_id)[x])
    difference  = total_even * 7 - total_odd
    if difference % 10 != int(str(citizen_id)[9]):
        return False

    total_ten = 0
    for x in range(10):
        total_ten += int(str(citizen_id)[x])
    
    if (total_ten % 10) != int(str(citizen_id)[10]):
        return False
    return True

