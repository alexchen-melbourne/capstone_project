## DSI Capstone project

_This page is for DSI Capstone project presatation._

## 0. Technology list

| Name          | Description   | 
| ------------- |:-------------:| 
| Python      | This project using Python-2.7 environment |
| Numpy      |  The fundamental package for scientific computing with Python      | 
| Pandas  | Easy-to-use data structures and data analysis tools for Python     |
| Beastiful Soup  | Convert web page to lxml so that all infomation on that page can be accessed and scraped easily     |
| Selenium  | Function as automates browsers in order to scrape infomation held by JavaScript    |
| Seaborn  |  A Python visualization library provides a high-level interface for drawing attractive statistical graphics.      |
| Sci-kit Learn  | Simple and efficient tools for data mining and data analysis       |



## 1. Backgroud Description


### 1.1 Problem Statement

<img src='http://i.imgur.com/4CRCS03.jpg'>

Melbourne has become the most liveable city all over the world for 7 years. As an important part of living in Melbourne, housing market is also getting increasingly attention. In this research, I will discuess below questions:

- For the thousands of new overseas settlers who migrate to Australia every year,  how should they find a nice place to live or buy a house?
  
### 1.2 Potential Audience

- New settler who just migrate to Australia

- Potential buyers

- Investors

### 1.3 Goals

- Collecting related data.

- Exploring Australia housing market in state level.

- Exploring Australia housing market in suburb level.

- Build a model to predict house price.

### 1.4 Success Metrics

- Based on different scenarios, using collected data to give recommendation to potential audiances.

- Generate house price heatmap based on location.

### 1.5 Data Sources

#### 1.5.1 National Data

Data from Australian Bureau of Statistic: [Residential Property Price Indexes](http://www.abs.gov.au/ausstats/abs@.nsf/mf/6416.0) provides estimates of changes in residential property prices in each of the eight capital cities of Australia and related statistics. 

#### 1.5.2 Suburb Data

Direct crawling raw data from [domain subueb profile](https://www.domain.com.au/suburb-profile/) with CSS selector and selemium. See crawling script at [suburb scraping notebook](https://github.com/alexchen-melbourne/capstone_project/blob/master/web-scraping/suburb-scrap.ipynb).

<img src='https://i.imgur.com/1rbvP1V.png'>

#### 1.5.3 House Data

Direct crawling raw data from [domain.com.au](https://www.domain.com.au/) with CSS selector. See crawling script at [Houses scraping notebook](https://github.com/alexchen-melbourne/capstone_project/blob/master/web-scraping/house_scraping.ipynb).

<img src='http://i.imgur.com/LeVNbzY.png'>



## 2. Data examining and cleaning

#### Dataset description

```markdown
    Dataset attribute Information:
    
    Suburb         Suburb



```

#### Load modules

```python
# data modules
import numpy as np
import scipy.stats as stats
import pandas as pd

# plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
```
#### Load data



## 3. Explortory Data Analysis



## 4. Predict Model


## UNFINISHED
