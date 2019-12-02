def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
import random
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):
    randomList = [random.randint(1,1000) for _ in range(2,random.randint(1,100))]
    @staticmethod
    def get_array():
        # complete this function
        returnList = list(set(TestDataUniqueValues.randomList))
        return returnList


    @staticmethod
    def get_expected_result():
        # complete this function
        returnList = list(set(TestDataUniqueValues.randomList))
        return returnList.index(min(returnList))

class TestDataExactlyTwoDifferentMinimums(object):
    randomList = [random.randint(1,1000) for _ in range(2,random.randint(1,100))]
    @staticmethod
    def get_array():
        # complete this function
        returnList = list(set(TestDataExactlyTwoDifferentMinimums.randomList))
        returnList.append(min(returnList))
        return returnList

    @staticmethod
    def get_expected_result():
        # complete this function
        returnList = list(set(TestDataExactlyTwoDifferentMinimums.randomList))
        index1 = returnList.index(min(returnList))
        return index1


