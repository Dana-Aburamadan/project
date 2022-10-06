
class Constants:
    Full_Time = 1
    Part_Time = 2
    Active = 4
    Inactive = 5

class Methods_Utils:

    @staticmethod
    def check_value_is_empty(*value: str):
        for item in value:
            if item.isspace() or item == "":
                return True