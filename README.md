# 🍽️ Zomato Data Analysis Using Python

## 📌 Project Overview

This project focuses on analyzing Zomato restaurant data using Python to understand customer preferences, restaurant trends, and ordering behavior. Through data cleaning, exploratory data analysis (EDA), and data visualization, the project uncovers valuable insights that can help restaurants improve their services and make data-driven business decisions.

The analysis aims to answer questions such as:

* Do more restaurants provide online ordering compared to offline services?
* Which restaurant categories are most popular among customers?
* What price range do couples prefer for dining?
* How do restaurant ratings differ between online and offline ordering?
* Which restaurants receive the highest customer votes?

---

# 📊 Dataset Description

The dataset contains information about restaurants listed on Zomato, including ratings, customer votes, pricing, restaurant categories, and online ordering facilities.

## 📋 Columns Description

| Column Name                      | Description                                      | Data Type |
| -------------------------------- | ------------------------------------------------ | --------- |
| **Name**                         | Name of the restaurant                           | Text      |
| **Online Order**                 | Whether online ordering is available (Yes/No)    | Text      |
| **Book Table**                   | Whether table booking is available (Yes/No)      | Text      |
| **Rate**                         | Customer rating of the restaurant                | Numeric   |
| **Votes**                        | Total number of customer votes                   | Number    |
| **Approx Cost (for Two People)** | Estimated dining cost for two people             | Number    |
| **Listed In (Type)**             | Restaurant category (Dining, Café, Buffet, etc.) | Text      |

---

# 🛠️ Project Workflow

## 1️⃣ Import Required Libraries

The project uses the following Python libraries:

* Pandas
* NumPy
* Matplotlib
* Seaborn

## 2️⃣ Load the Dataset

The Zomato dataset is imported into a Pandas DataFrame for further analysis.

## 3️⃣ Data Cleaning and Preparation

The following preprocessing steps are performed:

* Converted the `rate` column from text format (e.g., `4.2/5`) into numeric values.
* Verified dataset structure using `info()`.
* Checked for missing or null values.
* Ensured data consistency before analysis.

## 4️⃣ Exploratory Data Analysis (EDA)

Several analyses were performed, including:

* Distribution of restaurant categories.
* Total customer votes by restaurant type.
* Identification of the restaurant with the highest number of votes.
* Comparison of online and offline ordering availability.
* Distribution of restaurant ratings.
* Analysis of preferred spending range for couples.
* Comparison of ratings between restaurants with and without online ordering.
* Relationship between restaurant type and online ordering using a heatmap.

---

# 📈 Key Insights

* 🍴 The majority of restaurants belong to the **Dining** category.
* ⭐ Dining restaurants receive the highest number of customer votes.
* 🚫 Most restaurants do **not** offer online ordering facilities.
* 📊 The majority of restaurant ratings fall between **3.5 and 4.0**.
* 💰 Couples generally prefer restaurants with an approximate cost of **₹300 for two people**.
* 📱 Restaurants offering online ordering tend to receive higher customer ratings than offline-only restaurants.
* ☕ Customers prefer ordering online from cafés, while dining restaurants are more commonly visited in person.

---

# 💻 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook / Google Colab

---

# 🎯 Conclusion

This project demonstrates the power of Exploratory Data Analysis (EDA) in extracting meaningful insights from restaurant data. By analyzing customer behavior, pricing patterns, restaurant categories, and online ordering trends, businesses can make informed decisions to enhance customer satisfaction and improve operational strategies.

The findings provide valuable information for restaurant owners, food delivery platforms, and business analysts looking to understand consumer preferences and optimize their services.
