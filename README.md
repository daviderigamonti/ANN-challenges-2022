# ANN-challenges-2022

Repository dedicated to the challanges of Artificial Neural Networks and Deep Learning course at Politecnico di Milano a.a. 2022-2023 with Professor Matteucci.

The repository is structured in 2 main folders (`Homework1` and `Homework2`) corresponding to the two different challenges that were proposed for this course, each folder contains a `delivery` subfolder which holds the various files that were ultimately submitted for the challenge.

The final grade for each challenge was calculated by measuring arbitrary thresholds in the final leaderboard in conjunction with the T.A. review of the final delivery, which contains a notebook, the models and the report; the grade for each challenge spans from **0** to **5** and an additional **.5** is added according to the professor's discretion.

The report had to be written in accordance with the following instructions:

> The 3-page report must be written in Calibri, Times New Roman or Arial fonts with a body size of 11 \[...\]

therefore not a lot of care was put into the report designing process.

## Group

**Residual Sum of Students**
- Juliette Daniel
- Davide Rigamonti
- Raul Singh

## Homework 1

In this homework we were required to classify species of plants, which are divided into categories according to the species of the plant to which they belong. Being a classification problem, given an image, the goal is to predict the correct class label.

<table>
  <tr><td>Final Grade</td><td>5.5</td></tr>
  <tr><td>Leaderboard Position</td><td>#55</td></tr>
  <tr><td>Accuracy Score </td><td>0.8926</td></tr>
  <tr><td>Top Accuracy Score</td><td>0.9548</td></tr>
</table>

## Homework 2

In this homework, we were required to correctly classify samples in the multivariate time series format. In other words, since this is a classification problem, the objective is to correctly map the information contained in the features calculated over time to their labels.

<table>
  <tr><td>Final Grade</td><td>5.5</td></tr>
  <tr><td>Leaderboard Position</td><td>#39</td></tr>
  <tr><td>Accuracy Score </td><td>0.7326</td></tr>
  <tr><td>Top Accuracy Score</td><td>0.7711</td></tr>
</table>

## Autozip

In order to facilitate development and submission of the various models we implemented an **autozip Github Action** which automatically creates an archive called `submission.zip` whenever a commit modifies the submission deliverables of a certain model.

**NOTE:** When a new model *X* has been created and the corresponding folder called *X* (which must contain a model configuration folder called `ANN_Homework*Model` and the main submission file called `model.py`) has been placed inside the `Models` folder, the name of the folder (*X*) must be added to the array with entry *MODEL* inside the file `homework*_model_matrix.json` in order for the Github Action to automatically create zip submissions for that particular model.

**NOTE:** This feature went ultimately unused due to the large dimension of some models.
