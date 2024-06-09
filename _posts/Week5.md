---
layout: post
title: Week 5
---
## TMK Modeling Progress

## Literature Review on Hierarchical Task Network (HTN)

## Literature Review on TMKs and HTNs
As suggested by Dr. Ashok, I read the paper ***"A Study of Process Languages for Planning Tasks"*** by Stephen Lee-Urban, Héctor Muñoz-Avila. It briefly discusses the definition of a process and the importance of reuse and modification of processes to achieve knowledge transfer. TMK is both a process language and a process model. Its downfall, which is the lack of clear semantics, can be remedied by conversion to HTNs. HTN stands for Hierarchical Task Network and uses high-level tasks decomposed into simpler ones until reduced to primitive actions. HTN planning is encompassed in the Methods of TMK. The expressivity of two languages is demonstrated when there is a polynomial or Turing computable transformation between them. 
The translation from TMK to HTN starts with the translation process, which converts TMKs to HTNs by processing each TMK method recursively, translating statements, and constructing HTN methods from the results. To handle nested statements, recursive calls are implemented, breaking them down from the most to the least deeply nested. This method ensures a clear equivalence between TMKs and HTNs, but more compact translation can be achieved with PDDL (a STRIPS-based planning language).
The **toHTNs** procedure translates TMK statements into HTN methods. It starts with a sequence of TMK statements and processes them in reverse order. For a single statement with no body, a new task is created and appended as the last subtask. If the statement has a body, a recursive call is made to process it. For multiple statements, each is translated in reverse order with recursive calls, updating the task for each iteration. The result is a collection of HTN methods and the final task.




## Other Reading
