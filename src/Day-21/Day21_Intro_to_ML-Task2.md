#  Types of Machine Learning

## 1. Supervised Learning

Supervised Learning is a type of machine learning where the dataset contains both input data and the correct output (labels). The model learns the relationship between inputs and outputs by minimizing the difference between its predictions and the actual answers. It is commonly used for prediction and classification tasks.

**Key Idea:**  
Input + Correct Output → Learn the mapping

---

## 2. Unsupervised Learning

Unsupervised Learning is used when the dataset does not contain labeled answers. The model tries to identify hidden patterns, structures, or clusters within the data without being told what the correct output should be.

**Key Idea:**  
Input Only → Discover hidden structure

---

## 3. Reinforcement Learning

Reinforcement Learning is a learning method where an agent interacts with an environment and learns by receiving rewards or penalties based on its actions. The goal is to maximize long-term rewards by improving decision-making over time.

**Key Idea:**  
Action → Reward/Penalty → Improve Strategy

---

# Comparison Table – Real-World Examples

| Learning Type | Definition | Example 1 | Example 2 |
|--------------|------------|------------|------------|
| Supervised Learning | Data has labeled outputs | Spam Detection (Email → Spam/Not Spam) | House Price Prediction (Features → Price) |
| Unsupervised Learning | No labeled outputs; find hidden patterns | Customer Segmentation | Market Basket Analysis |
| Reinforcement Learning | Learning through rewards and penalties | Self-Driving Cars | Game Playing AI (Chess/Go) |

---

# Why Choosing the Wrong Learning Type Causes Failure

Choosing the wrong machine learning framework can lead to poor results before even writing code. If labeled data exists but you use clustering, or if no labels exist but you try supervised learning, your model will not perform correctly. Understanding the problem type first ensures you select the correct algorithm and approach.