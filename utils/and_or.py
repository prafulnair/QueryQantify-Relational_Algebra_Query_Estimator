def parse_and_or_query(query_str):
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
    # relation, attributes_info = parse_and_or_query(query_str)
    or_flag = False
    if "OR" in query_str:
        or_flag = True
    result = evaluate_and_or_query(relation_info, attributes_info, or_flag)
    print("Result:", result)

    if result:
        return result

    return relation, attributes_info


def parse_condition(condition, relation):
    parts = condition.split()
    attribute = None
    operator = None
    value = None

    for part in parts:
        # print(part)
        if '.' in part:
            relation, attribute = part.split('.')
        elif part in ['=', '!=', '<', '>']:
            operator = part
        elif type(part) == int:
            value = int(part)  # Assuming value is an integer for simplicity

    return relation, attribute, operator, value


def precedence(operator):
    if operator in ['=', '!=']:
        return 3
    elif operator in ['<', '>']:
        return 2
    else:
        return 1


def evaluate_and_or_query(relation_info, attributes_info,or_flag):
    total_tuples = relation_info["total_tuples"]
    result = total_tuples
    resulto = 0

    for attribute, info in attributes_info.items():
        operator = info["operator"]
        value = info["value"]

        if operator == '=':
            num_distinct_values = int(input(f"Enter the number of distinct values for attribute {attribute} in relation the relation: "))
            factor = 1 / num_distinct_values
        elif operator == '!=':
            num_distinct_values = int(input(f"Enter the number of distinct values for attribute {attribute} in the relation : "))
            factor = (num_distinct_values - 1) / num_distinct_values
        else:
            factor = 1 / 3

        if or_flag == True:
            resulto+=factor
        else:
            result *= factor

    if or_flag:
        total_tuples + resulto
        resulto = total_tuples * resulto
        return resulto

    return result


# Example usage

