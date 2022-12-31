# Stacks and Queues
<!-- Short summary or background information -->
- Stack is like last one in and first one out method. Queue is like waiting in line to get into the club.

## Challenge
<!-- Description of the challenge -->
- Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I approached this by using the test to help guide me in what it wants me to do. Once I passed all the test, I knew I had competed the challenge.

## API
<!-- Description of each method publicly available to your Stack and Queue-->

- push
adds a new node with that value to the top of the stack with an O(1) Time performance.

- pop
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

- peek
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

- is empty
Returns: Boolean indicating whether or not the stack is empty.

- enqueue
adds a new node with that value to the back of the queue with an O(1) Time performance.

- dequeue
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue
