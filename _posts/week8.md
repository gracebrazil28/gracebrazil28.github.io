---
layout: post
title: Week 8
---

## TMK Modeling Progress

## DILab Cross Project Meeting
The main goal of the meeting was to know (atleast for a newbie like me) and reinforce our understanding across teams on how explanations are being generated using our own internal MCM repo. Specifically, Rahul explains how a user's question is classified into one of four categories using a GPT API call. We discussed challenges in question classification and explainability in AI, particularly in the context of generative and cognitive AI. With this, it was emphasized how our project framework for with the integration of generative AI and cognitive AI, needs to be encompassed through the lens of theory of mind.

Across different projects in DI Lab, there were inconsistencies in TMK models across three teams, with missing values and inconsistent formatting. Additionally, metrics for evaluation were not uniform -- SAMI uses correctness, completeness, and confidence, VERA uses recall, precision and accuracy while IVY uses recall, correctness, completeness and precision. Spencer shares a link to a Wikipedia article on GQM (goals, quality, and metrics) to help frame the discussion on metrics for AI explanations. I was able to quickly find a paper that discusses its approach in UMD's public web domain and quickly review it for my own understanding. 

## DILab IVY Meeting 


## Literature Review: The Goal Question Metric Approach
From the paper titled ***"The Gual Question Metric Approach by "*** [Basili, Caldiera and Rombach](http://ftp.cs.umd.edu/pub/sel/papers/gqm.pdf). GQM asserts that projects must specify the goals for itself, trace its goals to the data intended to define the goals, then  provide a framework for interpreting the data with respect to the goals. Using the GQM should result to a measurement system that targets a set of issues and rules for interpretation. G stands for Goal, Q for Question and M for Metric. G is at the conceptual level where the goal is defined for an object of measurement such as products, processes and resources. Q is at the operational level where a set of questions is used to characterize the assessment of a specific goal, Finally M is at the quantitative level where a set of data is associated with every question to answer it in a quantitative way. To me, it sounds like GQM is a hierarchical structure that defines Goals with questions relevant to the goal and metrics which answers each questions quantitatively. A successful implementation of GQM model and has methodological steps that a project can follow. The main takeaway for me is that measurement must be defined in a top-down fashion and that it must be focused, based on goals and models.

## Literature Review: ReAct
From the paper titled ***" ___ "*** by . 