## DSI Capstone project

_This page is for DSI Capstone project presatation._

## 1. Backgroud Description


### 1.1 Problem Statement

<img src='http://i.imgur.com/4CRCS03.jpg'>

Melbourne has become the most liveable city all over the world for 7 years. As an important part of living in Melbourne, housing market is also getting increasingly attention. In this research, I will discuess below questions:

- What is the house price distribution in different region?

<img src='http://i.imgur.com/Vym86VC.png'>

- What is the house price distribution in different suburb? (Focusing on east and south-east suburb)

- Comparing 3 or more bedrooms houses, are 1 or 2 bedrooms houses more popular in Melbourne?

- Is there a reasonable model I can build to predict house price based on limited features?

Alternative qestion:

- Is there a house marking bubble in melbourne? (price/debt to income ratio.)

- Comparing to Sydney housing market, is melbourne housing market more suitable for investing? Who owns more 2 bedrooms house market?
  
### 1.2 Potential Audience

- Housing market agency

- Potential buyers

- Investors

### 1.3 Goals

Using collected data to:

- Examining house price distribution in different region.

- Examining house price distribution in different suburb.

- Examining house price distribution in different number of bedrooms house.

- Build a model to predict house price.

### 1.4 Success Metrics

- Comparing plots for different regions and suburbs.

- Generate house price heatmap based on location.

<img src='http://i.imgur.com/ozOQ5BM.png'>

- For training/testing split model validation, reach to reasonalbe positive recognition (60%) on testing data. 

### 1.5 Data Sources

Direct crawling raw data from [domain.com.au](https://www.domain.com.au/) with CSS selector. See crawling script at [crawling.py](https://github.com/alexchen-melbourne/capstone_project/blob/master/web_crawling.py).

<img src='http://i.imgur.com/LeVNbzY.png'>

More data on [realestate.com.au](https://www.realestate.com.au/sold/in-melbourne/list-1)

Data from [Kaggle -- Melbourne housing market](https://www.kaggle.com/anthonypino/melbourne-housing-market). Kaggle dataset: 19k house sold infomation in Mlebourne from 2016 to 2017.





## 2. Data examining and cleaning

#### Dataset description

```markdown
    Dataset attribute Information:
    
    Suburb         Suburb
    Address        Address
    Rooms          Number of rooms
    Price          Price in dollars
    Method         S - property sold; 
                   SP - property sold prior;
                   PI - property passed in; 
                   PN - sold prior not disclosed; 
                   SN - sold not disclosed; 
                   NB - no### Dataset characteristics
    Type           br - bedroom(s); 
                   h - house,cottage,villa, semi,terrace; 
                   u - unit, duplex; 
                   t - townhouse; 
                   dev site - development site; 
                   o res - other residential.
    SellerG        Real Estate Agent
    Date           Date sold
    Distance       Distance from CBD
    Regionname     General Region (West, North West, North, North east...etc)
    Bedroom2       Scraped # of Bedrooms (from different source)
    Bathroom       Number of Bathrooms
    Car            Number of carspots
    Landsize       Land Size
    BuildingArea   Building Size
    YearBuilt      Year the house was built
    CouncilArea    Governing council for the area
    Lattitude      Self explanitory
    Longtitude     Self explanitory
    Propertycount  Number of properties that exist in the suburb.
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


