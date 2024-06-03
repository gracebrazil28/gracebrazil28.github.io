---
layout: post
title: Week 4
---
## TMK Modeling Progress
As advised, I tried decomposing the method model even further. 
The method model was created to define the specific operations and transitions involved in comparing a given state to a goal state, detailing the steps for breaking down block positions, extracting individual positions, comparing these positions, and counting differences. The task model refers to this method model by specifying the conditions, inputs, outputs, and the corresponding methods to be used for each task, ensuring that the transitions in the method model align with the task names.

The method model was created to outline sequential operations based on tasks, forming a simple one-directional state machine. So, the Method Model JSON file is the following:

```json
{
  "model": "Method",
  "methods": [
    {
      "name": "Evaluate",
      "description": "Initiates the process of comparing given state to the goal state.",
      "initial state": "Initial",
      "inputs": "Set of blocks with their positions",
      "outputs": "Set of individual positions for each block",
      "transitions": {
        "break down each block position": {
          "type": "operation",
          "source subtask to target subtask": ["Initial", "Evaluate"]
        }
      }
    },
    {
      "name": "Individual Position Extraction",
      "description": "Extracts the position of each block from the given state.",
      "initial state": "Evaluate",
      "inputs": "Set of given state",
      "outputs": "Individual positions for each block",
      "transitions": {
        "extract position for each box": {
          "type": "operation",
          "source subtask to target subtask": ["Evaluate", "Individual Position Extraction"]
        }
      }
    },
    {
      "name": "Position Check",
      "description": "Compares the given position of each block to the goal position.",
      "initial state": "Individual Position Extraction",
      "inputs": "Individual positions for each block",
      "outputs": "Boolean values indicating position match for each block",
      "transitions": {
        "compare positions": {
          "type": "operation",
          "source subtask to target subtask": ["Individual Position Extraction", "Position Check"]
        }
      }
    },
    {
      "name": "Delta Counter",
      "description": "Counts the number of differences between the given and goal positions.",
      "initial state": "Position Check",
      "inputs": "Boolean values indicating position match for each block",
      "outputs": "Delta counter value",
      "transitions": {
        "increment delta counter": {
          "type": "operation",
          "source subtask to target subtask": ["Position Check", "Delta Counter"]
        }
      }
    }
  ]
}

```

The task model is the following:
```json
{
  "model": "Task",
  "tasks": [
    {
      "name": "Evaluate",
      "description": "Initiates the process of comparing given state to the goal state.",
      "inputs": "Set of blocks with their positions",
      "outputs": "Set of individual positions for each block",
      "given condition": "A set of blocks with initial positions is provided",
      "post-condition": "The given state is broken down into individual box positions",
      "method": "Evaluate"
    },
    {
      "name": "Individual Position Extraction",
      "description": "Extracts the position of each block from the given state.",
      "inputs": "Set of given state",
      "outputs": "Individual positions for each block",
      "given condition": "The given state is broken down into individual box positions",
      "post-condition": "Individual positions for each block are extracted",
      "method": "Individual Position Extraction"
    },
    {
      "name": "Position Check",
      "description": "Compares the given position of each block to the goal position.",
      "inputs": "Individual positions for each block",
      "outputs": "Boolean values indicating position match for each block",
      "given condition": "Individual positions for each block are available",
      "post-condition": "Boolean values indicating position match for each block are determined",
      "method": "Position Check"
    },
    {
      "name": "Delta Counter",
      "description": "Counts the number of differences between the given and goal positions.",
      "inputs": "Boolean values indicating position match for each block",
      "outputs": "Delta counter value",
      "given condition": "Boolean values indicating position match for each block are available",
      "post-condition": "Delta counter value indicating the number of differences is determined",
      "method": "Delta Counter"
    }
  ]
}

```
The Knowledge Model is the following:

```json
{
  "model": "Knowledge",
  "instances": [
    {
      "name": "BlockA",
      "concept": "Block"
    },
    {
      "name": "BlockB",
      "concept": "Block"
    },
    {
      "name": "BlockC",
      "concept": "Block"
    },
    {
      "name": "BlockD",
      "concept": "Block"
    },
    {
      "name": "Table",
      "concept": "Surface"
    },
    {
      "name": "DeltaCounter",
      "concept": "Counter",
      "values": [
        "0",
        "1",
        "2",
        "3",
        "4"
      ]
    },
    {
      "name": "Goal",
      "concept": "Set",
      "values": [
        "BlockA_on_BlockB",
        "BlockB_on_BlockC",
        "BlockC_on_BlockD",
        "BlockD_on_Table"
      ]
    },
    {
      "name": "Example1_GivenSet",
      "concept": "Set",
      "values": [
        "BlockA_on_BlockD",
        "BlockB_on_BlockC",
        "BlockC_on_Table",
        "BlockD_on_BlockB"
      ]
    },
    {
      "name": "Example2_GivenSet",
      "concept": "Set",
      "values": [
        "BlockA_on_Table",
        "BlockB_on_BlockC",
        "BlockC_on_Table",
        "BlockD_on_BlockA"
      ]
    },
    {
      "name": "Example3_GivenSet",
      "concept": "Set",
      "values": [
        "BlockA_on_Table",
        "BlockB_on_BlockC",
        "BlockC_on_Table",
        "BlockD_on_Table"
      ]
    }
  ],
  "triples": [
    {
      "name": "BlockA_on_BlockB",
      "instance1": "BlockA",
      "relation": "on",
      "instance2": "BlockB"
    },
    {
      "name": "BlockB_on_BlockC",
      "instance1": "BlockB",
      "relation": "on",
      "instance2": "BlockC"
    },
    {
      "name": "BlockC_on_BlockD",
      "instance1": "BlockC",
      "relation": "on",
      "instance2": "BlockD"
    },
    {
      "name": "BlockD_on_Table",
      "instance1": "BlockD",
      "relation": "on",
      "instance2": "Table"
    },
    {
      "name": "BlockA_on_BlockD",
      "instance1": "BlockA",
      "relation": "on",
      "instance2": "BlockD"
    },
    {
      "name": "BlockB_on_BlockC",
      "instance1": "BlockB",
      "relation": "on",
      "instance2": "BlockC"
    },
    {
      "name": "BlockC_on_Table",
      "instance1": "BlockC",
      "relation": "on",
      "instance2": "Table"
    },
    {
      "name": "BlockD_on_BlockB",
      "instance1": "BlockD",
      "relation": "on",
      "instance2": "BlockB"
    },
    {
      "name": "BlockA_on_BlockC",
      "instance1": "BlockA",
      "relation": "on",
      "instance2": "BlockC"
    },
    {
      "name": "BlockB_on_Table",
      "instance1": "BlockB",
      "relation": "on",
      "instance2": "Table"
    },
    {
      "name": "BlockC_on_BlockD",
      "instance1": "BlockC",
      "relation": "on",
      "instance2": "BlockD"
    },
    {
      "name": "BlockD_on_BlockB",
      "instance1": "BlockD",
      "relation": "on",
      "instance2": "BlockB"
    }
  ],
  "concepts": [
    {
      "name": "Block",
      "description": "A block that can be stacked on top of other blocks or the table",
      "properties": [{}]
    },
    {
      "name": "Set",
      "description": "A configuration of blocks and their positions",
      "properties": ["set of triples"]
    },
    {
      "name": "Surface",
      "description": "A surface that blocks can be placed on",
      "properties": [{}]
    },
    {
      "name": "Counter",
      "description": "A counter to keep track of the number of differences between given and goal states",
      "properties": ["integer value"]
    }
  ],
  "relations": [
    {
      "name": "on",
      "concept1": ["Block"],
      "concept2": ["Block", "Surface"]
    }
  ]
}

```

The knowledge model was constructed by first identifying the individual instances, representing each block in both the goal and given sets. Triples were then created to define the possible positions of blocks in relation to each other and to surfaces. Finally, concepts to encapsulate the overarching categories of blocks, states, and surfaces, while relations were to interconnect these concepts together.

<!-- Sync with Erin Notes -->

<!-- Sync with DILAB IVY Group Notes -->

### DILab Summer Reading

## Literature Review on Learning Theory

## Other Reading

