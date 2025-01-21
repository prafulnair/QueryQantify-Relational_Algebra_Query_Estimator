def parse_range_query(query_str):
    """
    Parses a range query string and extracts conditions.

    Args:
        query_str (str): The range query string.

    Returns:
        tuple: A tuple containing the relation name and a dictionary of attribute information.
            The dictionary keys are attribute names, and the values are dictionaries
            with keys 'operator' and 'value' representing the operator and value of the condition, respectively.

    Example:
        query_str = "A < 5 AND B > 10 OR C = 7"
        relation, attributes_info = parse_range_query(query_str)
    """

    conditions = query_str.split(" AND ") if " AND " in query_str else query_str.split(" OR ")
    relation = None
    attributes_info = {}

    for condition in conditions:
        relation, attribute, operator, value = parse_condition(condition, relation)
        if attribute:
            if attribute not in attributes_info:
                attributes_info[attribute] = {"operator": operator, "value": value}
            else:
                # If attribute already exists, choose the operator with higher precedence
                current_operator = attributes_info[attribute]["operator"]
                if precedence(operator) > precedence(current_operator):
                    attributes_info[attribute] = {"operator": operator, "value": value}

    total_no_tuples = int(input("Enter the total number of tuples in this relation: "))
    relation_info = {"total_tuples": total_no_tuples}  # Example relation information
    result = evaluate_range_query(relation_info, attributes_info)
    print("Result:", result)

    if result:
        return result

    return relation, attributes_info


def parse_condition(condition, relation):

    """
    Parses a condition string and extracts the relation name, attribute, operator, and value.

    Args:
        condition (str): The condition string to parse.
        relation (str): The current relation name.

    Returns:
        tuple: A tuple containing the relation name, attribute name, operator, and value.

    """

    parts = condition.split()
    attribute = None
    operator = None
    value = None

    for part in parts:
        if '.' in part:
            relation, attribute = part.split('.')
        elif part in ['=', '!=', '<', '>']:
            operator = part
        elif part.isdigit():
            value = int(part)

    return relation, attribute, operator, value


def precedence(operator):
    if operator in ['=', '!=']:
        return 3
    elif operator in ['<', '>']:
        return 2
    else:
        return 1


def evaluate_range_query(relation_info, attributes_info):
    """
    Evaluates a range query given relation information and attributes information.

    Args:
        relation_info (dict): Information about the relation, including the total number of tuples.
        attributes_info (dict): Information about attributes and their operators/values.

    Returns:
        float: The result of the range query evaluation.

    Example:
        relation_info = {"total_tuples": 1000}
        attributes_info = {"A": {"operator": "=", "value": 5}, "B": {"operator": ">", "value": 10}}
        result = evaluate_range_query(relation_info, attributes_info)
    """

    total_tuples = relation_info["total_tuples"]
    result = total_tuples

    for attribute, info in attributes_info.items():
        operator = info["operator"]
        value = info["value"]

        if operator == '=':
            while True:
                range_values = input(f"Enter the inclusive range for attribute {attribute} in the relation (in the form [a, b]): ")
                try:
                    start, end = map(int, range_values.strip()[1:-1].split(','))
                    if start <= end:
                        break
                    else:
                        print("Invalid range! Start value must be less than or equal to end value.")
                except ValueError:
                    print("Invalid input! Please enter integers separated by comma.")
            
            num_tuples_in_range = int(input(f"Enter the number of tuples in the range [{start}, {end}]: "))
            factor = (num_tuples_in_range / total_tuples) * (1 / (end - start + 1))
        elif operator in ['<', '>']:
            while True:
                range_values = input(f"Enter the inclusive range for attribute {attribute} in the relation (in the form [a, b]): ")
                try:
                    start, end = map(int, range_values.strip()[1:-1].split(','))
                    if start <= end:
                        break
                    else:
                        print("Invalid range! Start value must be less than or equal to end value.")
                except ValueError:
                    print("Invalid input! Please enter integers separated by comma.")

            num_values_satisfied = 0
            for value in range(start, end + 1):
                if (operator == '<' and value < info["value"]) or (operator == '>' and value > info["value"]):
                    num_values_satisfied += 1
            
            total_possible_values = end - start + 1
            factor = num_values_satisfied / total_possible_values
        
        else:
            factor = 1 / 3

        result *= factor

    return result