# Author: PJ Glasheen
# Enum class for truth values of assumptions
class TruthValue:
    false = 0
    true = 1
    irrelevant = 2

# returns the truth value in the form of a string
def getString(value):
    if value == 0:
        return "false"
    elif value == 1:
        return "true"
    elif value == 2:
        return "irrelevant"
    else:
        print value
        return "invalid truth value"
