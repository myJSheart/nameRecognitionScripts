class LowestCommonAncestor:
    '''
    This class contains functions that find out the lowest common ancestor
    '''

    def __init__(self, soup):
        self.soup = soup


    def lowest_common_ancestor_from_two(self, child_node_one, child_node_two):
        '''
        Get the lowest common ancestor from two nodes
        :param child_node_one: a node
        :param child_node_two: a node
        '''
        node_one_level = child_node_one.level
        node_two_level = child_node_two.level
        while node_one_level != node_two_level:
            if node_one_level > node_two_level:
                child_node_one = child_node_one.parent
                node_one_level -= 1
            elif node_two_level > node_one_level:
                child_node_two = child_node_two.parent
                node_two_level -= 1

        while child_node_one != child_node_two:
            child_node_one = child_node_one.parent
            child_node_two = child_node_two.parent

        return child_node_one
