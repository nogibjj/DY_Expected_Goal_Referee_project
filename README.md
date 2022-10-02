# Expected Goal_project_1
[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/DY_databricks_project_1/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/DY_databricks_project_1/actions/workflows/main.yml)


## A repo of accessing FREE soccer open data set via Statsbomb

### Goal of this project
Trying to analyze the difference between Expected Goal and actual final score of matches in real life 


## Project Data Import Diagram

![Expected Goal Project Diagram](https://user-images.githubusercontent.com/81750079/191083640-8796dfe5-de82-4d4f-8966-5e2dd34ded1b.jpg)


### Expected Goal
<img width="1110" alt="image" src="https://user-images.githubusercontent.com/81750079/190937944-e00b91b8-898d-47e9-800e-95c5ebbf3a77.png">


### Examples

#### For Euro 2020, the final is between Italy and England.

#### [Click here to see](https://github.com/nogibjj/DY_Expected_Goal_project_1/blob/main/test.ipynb)

Italy won the title on penalties 4:3 (1:1), and the Expected Goal for Italy is higher than England's, which is consistent.
However, in many games, there could be an inconsistency between Expected Goals and Actual Final scores.
This project would like to know how good the Expected Goals can be to predict the winner of a soccer match using Euro 2020 competition data (and more in the future).


### Limitations and future improvements

1. **[SOLVED]** Failed to pip data from StatsBomb API to Azure Databricks
1. ~~Instead of using Databricks, trying AWS s3~~
1. [List 1 SOLVED]Command line tool integration after list 1 or 2 is resolved
1. Build better FastAPI structure
1. Add more function on FastAPI


## Data Source

### [StatsBomb](https://statsbomb.com/)

### [StatsBomb Open Data](https://github.com/statsbomb/open-data)

![SB - Icon Lockup - Colour positive](https://user-images.githubusercontent.com/81750079/190938168-745a6fa0-321c-4952-af9a-1975cbffe3a1.png)
