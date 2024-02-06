
class TestDataEmptyArray:
    def get_array():
        return []

class TestDataUniqueValues:
    def get_array():
        return [1,2,3]

    def get_expected_result():
        return 0

class TestDataExactlyTwoDifferentMinimums:
    def get_array():
        return [2,1,2,3,1,2]
    
    def get_expected_result():
        return 1

