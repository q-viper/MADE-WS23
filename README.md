# Methods of Advanced Data Engineering Project: Exploration of COVID-19 trends and Related Tweet

## Datasets
This project implements a widely used software engineering practices in Python to explore  the relationship between COVID-19 trends and related tweets in the period of 2020-07-25 to 2020-08-30. Following are the data sources that has been used:
1. [Coronavirus Pandemic (COVID-19)](https://covid.ourworldindata.org/data/owid-covid-data.csv)
2. [COVID19 Tweets](https://www.kaggle.com/datasets/gpreda/covid19-tweets)

For Kaggle data, personal credentials were used.

## Implementation
Data from the both sources are handled by the single [`data_handler.py`](project/utils/data_handler.py) where the concept of [method cascading](https://en.wikipedia.org/wiki/Method_cascading) is implemented. Furthermore, it also uses the type hinting in function attributes and error handling efficiently. In addition to that, the whole pipeline depends on the configurations and constants written in [`configs.py`](project/utils/configs.py) with the use of dataclass.

To effectively catch the errors behavior of the code flow, test cases has been written and used `pytests` to check them.

## Final Results
This project had 4 main questions to be answered and they are well written in issues and can be found in [`project-plan.md`](project/project-plan.md) as well. The final report containing the findings is available as a notebook in file [`project/report.ipynb`]. The codes which generated those findings are available as a notebook in file [`exploration.ipynb`](project/notebooks/exploration.ipynb).