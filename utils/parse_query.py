import re
from Project import Project
from Select import Select
from Join import Join
from CartesianProduct import CartesianProduct

def parse_query(query_str):

    """
    Parses the given query string to extract operations and relational information.

    Args:
        query_str (str): The query string containing the operations.

    Returns:
        tuple: A tuple containing the parsed query operations and relational information.
            The parsed query operations are represented as a list of Operation objects.
            The relational information is represented as a dictionary with relation names as keys.
            For each relation, the dictionary contains information about the total number of tuples and
            the distinct values for each attribute.

    Raises:
        ValueError: If the query string format is invalid or incomplete.

    Example:
        query_str = "Project: A, B | Select: A > 5 | JOIN: R, S"
        or
        just Select: A > 5 or just JOIN: R, S
        parsed_query, relations_info = parse_query(query_str)
    """

    lines = query_str.split('\n')
    parsed_query = []
    relations_set = set()  # Set to store identified relations
    attributes_dict = {}   # Dictionary to store identified attributes for each relation
    for line in lines:
        if line.startswith("Project:"):
            attributes = re.findall(r'([A-Za-z]+)\.([A-Za-z]+)', line[len("Project:"):])
            attributes_dict = {}
            for relation, attr in attributes:
                if relation not in attributes_dict:
                    attributes_dict[relation] = []
                attributes_dict[relation].append(attr)
            parsed_query.append(Project(attributes_dict))
            for relation in attributes_dict.keys():
                relations_set.add(relation)  # Add the identified relation to the set
                # Prompt user for relation and attribute information
            relations_info = {}
            for relation in relations_set:
                total_tuples = int(input(f"Enter the total number of tuples in relation {relation}: "))
                relation_attributes = {}
                for attr in attributes_dict.get(relation, []):
                    attr_size = int(input(f"Enter the size of attribute {attr} in relation {relation}: "))
                    relation_attributes[attr] = attr_size
                relations_info[relation] = {"total_tuples": total_tuples, "attributes": relation_attributes}

                return parsed_query, relations_info
            
        elif line.startswith("Select:"):
            condition = line[len("Select:"):].strip()
            relation = condition.split('=')[0].split('.')[0].strip()  # Extracting the relation name from the condition
            relations_set.add(relation)  # Add the identified relation to the set
            
            if relation not in attributes_dict:
                attributes_dict[relation] = set()
            
            if '!=' in condition:
                attr = condition.split('!=')[0].split('.')[1].strip()
                attributes_dict[relation].add(attr)
            if '=' in condition:
                attr = condition.split('=')[0].split('.')[1].strip()  # Extracting the attribute name for conditions with "="
                attributes_dict[relation].add(attr)
            if '<' in condition:
                attr = condition.split('<')[0].split('.')[1].strip()  # Extracting the attribute name for conditions with "<"
                attributes_dict[relation].add(attr)
            if '>' in condition:
                attr = condition.split('>')[0].split('.')[1].strip()  # Extracting the attribute name for conditions with ">"
                attributes_dict[relation].add(attr)
              # Initialize set for attributes if relation is seen for the first time
            # attributes_dict[relation].add(attr)  # Add the identified attribute to the set
            parsed_query.append(Select(condition, relation))

        elif line.startswith("JOIN:"):
            parts = line[len("JOIN:"):].strip().split(', ')
            parsed_query.append(Join(parts))
            for table in parts:
                relations_set.add(table.strip())  # Add the identified relation to the set
        elif line.startswith("Cartesian Product:"):
            relations = line[len("Cartesian Product:"):].strip().split(', ')
            for relation in relations:
                relations_set.add(relation.strip())  # Add the identified relation to the set
            parsed_query.append(CartesianProduct(relations))
     
    # Prompt user for relation and attribute information
    
    relations_info = {}
    for relation in relations_set:
        total_tuples = int(input(f"Enter the total number of tuples in relation {relation}: "))
        distinct_values = {}
        for attr in attributes_dict.get(relation, []):
            num_distinct = int(input(f"Enter the number of distinct values for attribute {attr} in relation {relation}: "))
            distinct_values[attr] = num_distinct
        relations_info[relation] = {"total_tuples": total_tuples, "distinct_values": distinct_values}

    return parsed_query, relations_info
    


