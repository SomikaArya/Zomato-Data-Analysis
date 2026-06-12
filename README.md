# Zomato Data Analysis Using Python

## Project Overview

This project focuses on analyzing Zomato restaurant data using Python to understand customer preferences, restaurant trends, and ordering behavior. Through data cleaning, visualization, and exploratory data analysis (EDA), the project uncovers valuable insights that can help restaurant owners and business analysts make informed decisions.

The analysis aims to answer questions such as:

* Do more restaurants provide online ordering compared to offline services?
* Which restaurant categories are most popular among customers?
* What is the preferred dining budget for couples?
* How do restaurant ratings vary between online and offline order services?
* Which restaurants receive the highest customer votes?

## Dataset Description

The dataset contains information about restaurants listed on Zomato, including their ratings, order availability, pricing, customer votes, and restaurant categories.

### Columns Description

### Name

**Description:** Name of the restaurant.
**Type:** Text

### Online Order

**Description:** Indicates whether the restaurant accepts online orders.
**Values:**

* Yes
* No
  **Type:** Text

### Book Table

**Description:** Indicates whether table booking is available.
**Values:**

* Yes
* No
  **Type:** Text

### Rate

**Description:** Average customer rating of the restaurant.
**Type:** Numeric (converted from text format)

### Votes

**Description:** Number of customer votes received by the restaurant.
**Type:** Number

### Approx Cost (for Two People)

**Description:** Estimated cost for two people dining together.
**Type:** Number

### Listed In (Type)

**Description:** Category of the restaurant.
**Examples:**

* Dining
* Café
* Buffet
* Desserts
* Drinks & Nightlife
* Pubs and Bars
* Delivery

**Type:** Text

## Project Workflow

### 1. Import Required Libraries

The project uses the following Python libraries:

* Pandas
* NumPy
* Matplotlib
* Seaborn

### 2. Load the Dataset

The CSV dataset is imported into a Pandas DataFrame for analysis.

### 3. Data Cleaning and Preparation

* Converted the `rate` column from string format (e.g., `4.2/5`) to floating-point values.
* Verified dataset structure using `info()`.
* Checked for missing or null values.
* Ensured data consistency before analysis.

### 4. Exploratory Data Analysis

The project includes several analyses:

* Distribution of restaurant categories.
* Total customer votes by restaurant type.
* Identification of the restaurant with the highest number of votes.
* Comparison of online and offline ordering availability.
* Distribution of restaurant ratings.
* Analysis of preferred spending range for couples.
* Comparison of ratings between online-order and offline-order restaurants.
* Relationship between restaurant type and online ordering using heatmaps.

## Key Insights

* Most restaurants belong to the **Dining** category.
* Dining restaurants receive the highest number of customer votes.
* A majority of restaurants do **not** offer online ordering.
* Most restaurant ratings fall between **3.5 and 4.0**.
* Couples generally prefer restaurants with an approximate cost of **₹300 for two people**.
* Restaurants that provide online ordering generally receive better customer ratings than those relying only on offline orders.
* Customers tend to prefer **offline dining at restaurants** while **cafés receive more online orders**, indicating different customer behavior across restaurant types.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook / Google Colab

## Conclusion

This project demonstrates how Exploratory Data Analysis (EDA) can transform raw restaurant data into actionable business insights. By analyzing customer preferences, pricing trends, restaurant categories, and online ordering behavior, businesses can better understand market demand and improve their services based on data-driven decisions.
operational strategies.

The findings provide valuable information for restaurant owners, food delivery platforms, and business analysts looking to understand consumer preferences and optimize their services.
