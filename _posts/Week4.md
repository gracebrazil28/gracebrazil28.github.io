---
layout: post
title: Week 4
---
## TMK Modeling Progress
As advised, I tried decomposing the method model even further. 
The method model was created to define the specific operations and transitions involved in comparing a given state to a goal state, detailing the steps for breaking down block positions, extracting individual positions, comparing these positions, and counting differences. The task model refers to this method model by specifying the conditions, inputs, outputs, and the corresponding methods to be used for each task, ensuring that the transitions in the method model align with the task names. On the other hand, the method model was created to outline sequential operations based on tasks, forming a simple one-directional state machine.Finally, the knowledge model was constructed by first identifying the individual instances, representing each block in both the goal and given sets. Triples were then created to define the possible positions of blocks in relation to each other and to surfaces. Finally, concepts to encapsulate the overarching categories of blocks, states, and surfaces, while relations were to interconnect these concepts together.
* [Task Model v1](files/Task_Model_BlockWorld2_v1.json)
* [Method Model v1](files/Method_Model_BlockWorld2_v1.json)
* [Knowledge Model v1](files/Knowledge_Model_BlockWorld2_v1.json)

<!-- Sync with Erin Notes -->
After my sync with Erin, I've realized I needed to tie the TMK model back to the skill that the learner is needing to acquire. This means that the knowledge model will have the concepts for means end analysis and how it is achieved through the block world problem. I also needed to edit the knowledge model so that it will have the specific wordings that the problem is using. This was emphasized last team meeting where standardization is one of the key goals this semester. Similarly, I've written 1:1 mapping between tasks and methods, Erin has mentioned that a task can have multiple methods and suddenly I start thinking about this problem in a different manner. I've mentioned that I will approach this with two tasks: (1) Evaluating the means end difference between given and goal state and then (2) Choosing the best block arrangement that will satisfy the means end analysis. From there, I can create methods that will achieve this task. The method model seems to be the most complicated one to create since I have to think about the state transitions between them. She also recommended looking at the current Block Problem presentation and how state transitions were expressed and go from there. Her feedback gave me multiple things to work on. 

<!-- Sync with DILAB IVY Group Notes -->

### DILab Summer Reading
I started to take a stab at Chapter 12: Transformers in ["Deep Learning: Foundations and Concepts"](https://www.bishopbook.com) by Christopher Bishop. I learned about the concept of attention, transformer operation, self-attention, and soft attention. 
#### Concept of Attention
The concept of attention in neural networks is important, particularly in predicting the next word in a sequence by heavily relying on certain key words. Unlike standard neural networks, where the weights are fixed once the network is trained, attention mechanisms dynamically adjust weighting factors based on the specific input word or data. In natural language processing (NLP), words are mapped to vectors in an embedding space, capturing their semantic meaning. 
#### Basic Transformer Operation
Transformers operate on a data matrix, XX, with dimensions N (tokens) x D (features). This matrix represents a set of input tokens. The fundamental building block of a transformer takes X as input and produces a transformed matrix X~. Transformers consist of multiple layers, each with its own weights and biases, which are learned using gradient descent via a cost function. Attention coefficients play a crucial role in this process. Input tokens x1 ,x2 ,…,xn  in the embedding space are transformed into output tokens y1 ,y2 ,…,yn , with yn  being a linear combination of input vectors, weighted by attention weights anm . These weights determine the influence of each input token on the output token, with significant tokens receiving higher weights.
#### Concept of Self Attention and Soft Attention
Self-attention, an important mechanism in transformers, determines these weights by computing a measure of similarity, such as the dot product, between tokens. Soft attention, which uses continuous variables for matching queries and keys, allows for differentiable computations suitable for gradient descent. The softmax function is used to normalize these weights, ensuring they form a valid probability distribution. This mechanism allows the model to effectively capture dependencies and relationships within the input sequence.

## Literature Review on Learning Theory

## Other Reading

