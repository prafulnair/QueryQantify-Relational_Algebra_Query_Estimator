from Project import Project
from Select import Select
from Join import Join
from CartesianProduct import CartesianProduct
from parse_query import parse_query
import and_or  
import range_query  
import sys
from complex_query import parse_complex_query


print("Enter you query. type exit to quit the program")

while True: 
    is_range_query = input("Is it a range statistic query? (yes/no): ").lower().strip()
    if is_range_query == "yes":
        query_str = input("Please enter the query here: ")
        range_query.parse_range_query(query_str)
        sys.exit(0)

    elif is_range_query == "exit":
        sys.exit(0)

    elif is_range_query == "no":
        
        # Take input query from the user
        query_str = input("Please enter the query here: ")

        if "|" in query_str:
            result = parse_complex_query(query_str)
            print(result)
            sys.exit(0)


        if "AND" in query_str or "OR" in query_str:
            and_or.parse_and_or_query(query_str)  # Call the function using the module name as prefix
            sys.exit(0)
        else:
            # Parse the query string
            query, relations_info = parse_query(query_str)

            # Print the parsed query
            print("Parsed Query Structure:")
    
            for item in query:
                print("This is item ", item)

            # Evaluate the query
            result = []
            for operation in query:
                result.append(operation.evaluate(relations_info))

            for item in result:
                print("The result is : ", item)


        
    else:
        print("Enter a valid input. Either a yes or a no.")