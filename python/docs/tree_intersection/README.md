# Tree intersection
## Challenge
Implement a function that takes 2 binary trees as an input and returns the intersection of their node values as a list.


## Whiteboard

![](./CC_32.png)


## Approach & Efficiency
- start empty dictionary
- for each binary tree
- post order traversal
- check if value is in the dictionary
-  if not then add dictionary with value 1
- else return None


Time: O(n) because the number of operations is linearly proportional to the total number of nodes between the 2 trees.
Space: O(n) because a python dictionary and list of no greater length than the max number of nodes in a single tree are stored in memory.


## Contributors

- Angelos

