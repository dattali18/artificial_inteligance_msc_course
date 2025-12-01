## Search Algorithm Performance Analysis (Assignment 2, Question 5 & 6)

### Performance Summary Table

The following table presents the statistical results from 100 simulation runs conducted on a $5 \times 5$ maze using four different search strategies.

| Algorithm | Percentage Solved | Average Path Length (Solved) | Average Expansions (Solved) | Average Expansions (No Solution) |
| :--- | :---: | :---: | :---: | :---: |
| **Uniform Cost Search (UCS)** | 73.00% | 9.00 | 17.63 | 9.00 |
| **Greedy Search (Manhattan)** | 73.00% | 9.08 | **8.70** | 11.00 |
| **A\* (Euclidean Heuristic)** | 73.00% | **9.00** | 14.63 | 9.00 |
| **A\* (Manhattan Heuristic)** | 73.00% | **9.00** | 14.27 | 9.00 |

*(Note: "Expansions" refer to the number of states removed from the open list, which serves as a metric for computational effort.)*

***

### Conclusion (Assignment 2, Question 6)

The simulation results lead to clear conclusions regarding the trade-offs between optimality and computational efficiency for the explored search algorithms.

#### 1. Optimality and Solution Quality

The data confirms the theoretical guarantees of the search algorithms based on path length:

* **Optimal Algorithms:** **UCS, A\* (Euclidean), and A\* (Manhattan)** all achieved an identical average path length of **$9.00$**. Since UCS and A\* are designed to be **optimal** (finding the minimum cost path), this value represents the average shortest path length across the $73.00\%$ of solvable mazes.
* **Sub-Optimal Algorithm:** **Greedy Search** produced an average path length of **$9.08$**. This slight increase confirms that Greedy Search is **sub-optimal**, as its focus solely on minimizing the heuristic estimate ($h(n)$) can lead to longer, less efficient paths to the goal.

#### 2. Computational Efficiency

Efficiency, measured by the average number of expanded states, reveals the impact of heuristic guidance:

* **Greedy Search** exhibited the lowest average expansions (**$8.70$**). This extreme efficiency is a result of its **aggressive, purely greedy nature**, which significantly reduces search breadth by always pursuing the state closest to the goal.
* **UCS** demonstrated the highest expansion count (**$17.63$**). As an uninformed search that explores states based only on their true cost ($g(n)$), it explores broadly, confirming it is the least efficient for this task.
* **A\* Search** successfully balanced optimality and efficiency:
    * **A\* (Manhattan)** required **$14.27$** expansions.
    * **A\* (Euclidean)** required **$14.63$** expansions.
    Both A\* variants were significantly more efficient than UCS but sacrificed some of the rapid speed of Greedy Search to maintain path optimality.

#### 3. Heuristic Comparison

The **Manhattan distance** heuristic resulted in a slightly lower expansion count (**$14.27$**) compared to the **Euclidean distance** (**$14.63$**) when used with A\*. This marginal advantage is typical in grid-based environments where movement is restricted to four cardinal directions, as the Manhattan distance more closely models the true path cost (the sum of horizontal and vertical steps).

#### Overall Conclusion

The **A\* algorithm with the Manhattan Distance heuristic** is the recommended strategy for this maze problem. It achieves the key academic objective of **guaranteed optimality** (average path length $9.00$) while maintaining a high degree of **efficiency** ($14.27$ expansions), effectively capitalizing on informed search techniques to minimize computational cost compared to the uninformed UCS. Greedy Search, while the fastest, is unsuitable for applications where finding the shortest path is a requirement.