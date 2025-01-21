from Operation import Operation

class Project(Operation):
    def __init__(self, attributes):
        self.attributes = attributes

    def evaluate(self, relations_info, block_size=1024, block_header_size=24):

        """
        Calculates the number of blocks required to store the tuples of the relations.

        Args:
            relations_info (dict): A dictionary containing information about the relations.
                Keys are relation names and values are dictionaries with keys 'total_tuples' and 'attributes'.
                'total_tuples' is the total number of tuples in the relation.
                'attributes' is a dictionary with attribute names as keys and their sizes in bytes as values.
            block_size (int, optional): The size of a block in bytes. Defaults to 1024.
            block_header_size (int, optional): The size of the block header in bytes. Defaults to 24.

        Returns:
            int: The total number of blocks required to store the tuples of the relations.

        Example:
            relations_info = {
                'R': {'total_tuples': 1000, 'attributes': {'A': 4, 'B': 4, 'C': 4}},
                'S': {'total_tuples': 800, 'attributes': {'C': 4, 'D': 4, 'E': 4}}
            }
            block_size = 1024
            block_header_size = 24
            num_blocks = calculate_num_blocks(relations_info, block_size, block_header_size)
        """

        num_blocks = 1
        tuple_header_size = 12  # Assume tuple header size is 12 bytes

        for relation, attr_list in self.attributes.items():
            relation_info = relations_info[relation]
            total_tuples = relation_info["total_tuples"]
            tuple_size = sum(relation_info["attributes"][attr] for attr in attr_list) + tuple_header_size
            tuples_per_block = (block_size - block_header_size) // tuple_size
            num_blocks *= total_tuples / tuples_per_block

        return num_blocks

    def __str__(self):
        attr_str = ', '.join(f"{relation}.{attr}" for relation, attrs in self.attributes.items() for attr in attrs)
        return f"Projection: {attr_str}"
