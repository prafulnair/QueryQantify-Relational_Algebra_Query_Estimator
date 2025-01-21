from Operation import Operation

class Join(Operation):
    def __init__(self, tables):
        self.tables = tables

    def evaluate(self, relations_info):

        """
        Evaluates the Join operation given information about the relations.

        Args:
            relations_info (dict): Information about the relations, including total number of tuples and attributes.

        Returns:
            float: The result of the Join operation.

        Example:
            join = Join(["R", "S"])
            relations_info = {
                "R": {"total_tuples": 1000, "attributes": {"A": 10, "B": 20, "C": 30}},
                "S": {"total_tuples": 800, "attributes": {"C": 30, "D": 40, "E": 50}}
            }
            result = join.evaluate(relations_info)
        """
        print("Inside the class function of Join , evaluate")
        left_relation, right_relation = self.tables
        left_relation_info = relations_info[left_relation]
        right_relation_info = relations_info[right_relation]

        relation_attr = {}
    
        for relation in relations_info:
            #total_tuples = int(input(f"Enter the total number of tuples in {relation}: "))
            #distinct_values = {}
            attribute_j = input(f"Enter all the attributes for this Relation {relation} separated by ',' ")
            relation_attr[relation] = attribute_j
        
        x = list(relation_attr.values())[0]
        y = list(relation_attr.values())[1]

        set1 = set(x.replace(", ", ""))
        set2 = set(y.replace(", ", ""))
        common_attr = set1.intersection(set2)
        if len(common_attr) == 0:
            print(" NO common attribute, result is 0")
            return 0

        # common_attributes = set(left_relation_info["distinct_values"].keys()) & set(right_relation_info["distinct_values"].keys())
        # if not common_attributes:
        #     return 0  # Return 0 if there are no common attributes

        # Ask for unique values of common attributes
        common_attributes = common_attr
        common_attribute_values = {}
        cav = []
        for relation in relations_info:
            for attr in common_attributes:
                cav_v = int(input(f"Enter the number of unique values for attribute {attr} that are common in relations {relation}: "))
                common_attribute_values[attr] = cav_v
                cav.append(cav_v)

        print("This is the max attribute common val: ", max(common_attribute_values.values()))
        num_tuples = (left_relation_info["total_tuples"] * right_relation_info["total_tuples"]) / max(cav)

        return num_tuples

    def __str__(self):
        return f"JOIN: {self.tables}"
