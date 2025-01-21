import re

def parse_complex_query(query_str):
    output_str = query_str.split("|", 1)[1].strip()
    select_clause, join_clause = output_str.split("|")  # Separate Select and JOIN clauses
    
    select_clause = select_clause.strip()
    join_clause = join_clause.strip()
    
    # Extract relations from the JOIN clause
    relations = re.findall(r'(\w+)', join_clause.split(":")[1])

    relations_info = {}
    common_attributes = []
    relation_attr = {}
    for relation in relations:
        total_tuples = int(input(f"Enter the total number of tuples in relation {relation}: "))
        distinct_values = {}
        relations_info[relation] = {"total_tuples": total_tuples, "distinct_values": distinct_values}
        
        attribute_j = input(f"Enter all the attributes for this Relation {relation} separated by ',' ")
        relation_attr[relation] = attribute_j

        

    x = list(relation_attr.values())[0]
    y = list(relation_attr.values())[1]

    set1 = set(x.replace(", ", ""))
    set2 = set(y.replace(", ", ""))
    common_attr = set1.intersection(set2)
   
    

    common_attributes = common_attr
    common_attribute_values = {}
    cav = []
    denominator_values = []
    for relation in relations:
        for attr in common_attributes:
            cav_v = int(input(f"Enter the number of unique values for attribute {attr} that are common in relations {relation}: "))
            common_attribute_values[attr] = cav_v
            cav.append(cav_v)
            denominator_values.append(cav_v)

    # Calculate denominator
    denominator = max(denominator_values)

    """------------------------------------------"""
    condition = select_clause.split(":")[1].strip()
    relation = condition.split("<")[0].strip() if "<" in condition else condition.split(">")[0].strip() if ">" in condition else condition.split("=")[0].strip()
    attribute = relation.strip()
    num_tuples = 1
    for relation_info in relations_info.values():
        num_tuples *= relation_info["total_tuples"]

    unique_vals = {}
    if "=" in condition:
        print("ENTERED here")
        for relation in relations:
            # if attribute in relations_info[relation]["distinct_values"]:
            unique_val = int(input(f"Enter the number of unique values for attribute {attribute} in relation {relation}: "))
            unique_vals[relation] = unique_val

    
    factor = 1
    if "=" in condition:
        for relation in relations:
            factor = factor * (1 / unique_vals[relation])


    else:
        if attribute in common_attributes:
            for relation in relations:
                factor = factor * (1 / 3)
        else:
            factor = 1 / 3  # Assume factor is 1/3 for '<' and '>' conditions

    return num_tuples * factor / denominator


