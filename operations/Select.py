
from Operation import Operation
import re

class Select(Operation):
    def __init__(self, condition, relation):
        self.condition = condition
        self.relation = relation

    def evaluate(self, relations_info):
        relation_info = relations_info[self.relation]
        num_tuples = relation_info["total_tuples"]

        conditions = self.condition.split(" AND ")  # Split conditions based on 'AND'

        select_factors = []
        for condition in conditions:
            if "!=" in condition:
                attr, value = condition.split("!=")
                attr = attr.strip().split('.')[-1]  # Extract attribute name
                value = value.strip()

                if attr in relation_info["distinct_values"]:
                    num_distinct_values = relation_info["distinct_values"][attr]
                    factor = (num_distinct_values - 1) / num_distinct_values
                    select_factors.append(factor)
            elif "=" in condition:
                attr, value = condition.split("=")
                attr = attr.strip().split('.')[-1]  # Extract attribute name
                value = value.strip()

                if attr in relation_info["distinct_values"]:
                    num_distinct_values = relation_info["distinct_values"][attr]
                    factor = 1 / num_distinct_values
                    select_factors.append(factor)
            elif "<" in condition or ">" in condition:
                factor = 1 / 3
                select_factors.append(factor)

        result = num_tuples
        for factor in select_factors:
            result *= factor

        return result

    def __str__(self):
        return f"Select: {self.condition}"
