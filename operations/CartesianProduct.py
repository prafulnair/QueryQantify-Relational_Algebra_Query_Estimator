from Operation import Operation

class CartesianProduct(Operation):
    def __init__(self, relations):
        self.relations = relations

    def evaluate(self, relations_info):
        num_tuples = 1
        for relation in self.relations:
            num_tuples *= relations_info[relation]["total_tuples"]
        return num_tuples

    def __str__(self):
        return f"Cartesian Product: {', '.join(self.relations)}"
