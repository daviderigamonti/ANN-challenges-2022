# ANN-challenges-2022
Repository dedicated to the challanges of Artificial Neural Networks course at Politecnico di Milano a.a. 2022-2023 with Professor Matteucci.

## Homework 1

### Autozip

In order to facilitate development and submission of the various models we implemented an **autozip Github Action** which automatically creates an archive called `submission.zip` whenever a commit modifies the submission deliverables of a certain model.

**NOTE:** When a new model *X* has been created and the corresponding folder called *X* (which must contain a model configuration folder called `ANN_Homework1_Model` and the main submission file called `model.py`) has been placed inside the `Models` folder, the name of the folder (*X*) must be added to the array with entry *MODEL* inside the file [`homework1_model_matrix.json`](Homework1/homework1_model_matrix.json) in order for the Github Action to automatically create zip submissions for that particular model.