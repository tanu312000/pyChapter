class Node:
    def __init__(self, val, next_ref):
        self.val = val;
        self.next = next_ref;

    # Global variable for header and tail pointer in singly linked list.


head = tail = None;


# appends new node at the end in singly linked list.
def append_node(val):
    global head, tail;
    node = Node(val, None);
    if head is None:
        head = node;
    else:
        tail.next = node;
    tail = node;


# inserts new node at specific position in singly linked list.
def insert_node(val, position):
    global head, tail;
    current_node = head;
    while (position > 1):
        position -= 1;
        current_node = current_node.next;
    temp_next = current_node.next;
    node = Node(val, temp_next);
    current_node.next = node;


# prints singly linked list values.
def print_list():
    global head, tail;
    print("Single linked list");
    current_node = head;
    print
    "head -->",;
    while (current_node is not None):
        print
        current_node.val, "-->",;
        current_node = current_node.next;
    print
    "End";


# removes matching first node for particular value in linked list.
def remove_node(val):
    global head, tail;
    current_node = head;
    previous_node = None;
    while (current_node is not None):
        if current_node.val == val:
            if previous_node is not None:
                previous_node.next = current_node.next;
            else:
                head = current_node.next;
        previous_node = current_node;
        current_node = current_node.next;

    # reverses singly linked list values.


def reverse_linked_list():
    global head, tail;
    current_node = head;
    previous_node = None;
    while (current_node is not None):
        next_node = current_node.next;
        current_node.next = previous_node;
        previous_node = current_node;
        current_node = next_node;
        head = previous_node;

    # getting nodes count in singly linked list.


def count():
    global head, tail;
    current_node = head;
    counter = 0;
    while (current_node is not None):
        counter += 1;
        current_node = current_node.next;
    print
    "Single linked list node count:", counter;


if __name__ == "__main__":
    append_node(20);
    append_node(13);
    append_node(24);
    append_node(56);
    print_list();
    insert_node(45, 2);
    print
    "After insert node at 2";
    print_list();
    remove_node(13);
    print
    "After removal of node 13";
    print_list();
    reverse_linked_list();
    print
    "After reversing singly linked list";
    print_list();
    count();
