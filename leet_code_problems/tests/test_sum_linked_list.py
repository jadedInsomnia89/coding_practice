import unittest
from sum_linked_list import ListNode, Solution

class TestAddLinkedLists(unittest.TestCase):
    def test_add_two_numbers(self):
        sol = Solution()

        # ---------------------------------------------------------------

        # Test two nodes with length of 1 and values of 0
        n1 = ListNode()
        n2 = ListNode()
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [0])

        # ---------------------------------------------------------------

        # Test two lists with length of 1 and values 2 and 5
        n1 = ListNode(2)
        n2 = ListNode(5)
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [7])

        # ---------------------------------------------------------------

        # Test two nodes with lengths of 3 and 1  with remainders
        n1 = ListNode(9, ListNode(9, ListNode(1)))
        n2 = ListNode(1)
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [0, 0, 2])

        # ---------------------------------------------------------------

        # Test two nodes with lengths of 2 and 3  with no remainders
        n1 = ListNode(2, ListNode(4))
        n2 = ListNode(5, ListNode(5, ListNode(4)))
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [7, 9, 4])

        # ---------------------------------------------------------------

        # Test two nodes with lengths of 2 and 3  with remainders
        n1 = ListNode(2, ListNode(4))
        n2 = ListNode(5, ListNode(6, ListNode(4)))
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [7, 0, 5])

        # ---------------------------------------------------------------

        # test two nodes with lengths of 3 with remainders
        n1 = ListNode(2, ListNode(4, ListNode(3)))
        n2 = ListNode(5, ListNode(6, ListNode(4)))
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [7, 0, 8])

        # ---------------------------------------------------------------

        # test two nodes with lengths of 10 and 9 with remainders
        n1 = ListNode(0, ListNode(8, ListNode(8, ListNode(8, ListNode(8, ListNode(2, ListNode(9, ListNode(3, ListNode(1, ListNode(1))))))))))
        n2 = ListNode(0, ListNode(9, ListNode(1, ListNode(5, ListNode(5, ListNode(5, ListNode(1, ListNode(1, ListNode(6)))))))))
        summed_linked_list = sol.add_two_numbers(n1, n2)

        # convert linked list values to a list
        summed_list = []
        while summed_linked_list:
            summed_list.append(summed_linked_list.val)
            summed_linked_list = summed_linked_list.next

        self.assertEqual(summed_list, [0,7,0,4,4,8,0,5,7,1])

if __name__ == '__main__':
    unittest.main()
