# CS634 Data Mining Midterm Project

## Data Mining Techniques for Transaction Database Analysis

This project applies various data mining techniques to analyze transaction databases typically found in retail environments, such as supermarkets. The focus is on employing and comparing different algorithms, including brute force, Apriori, and FP-Growth, to discover frequent itemsets and derive association rules.

### Author
Tarun Deshmukh Tetapally (tt362)

### Instructor
Dr. Yasser Abduallah

### Institution
Department of Computer Science, New Jersey Institute of Technology

### Date
29th February 2024

## Repository Contents

- **Project Files:**
  - Python script (project.py)
  - Jupyter Notebook (project.ipynb)
- **Datasets:**
  - Amazon Transactions (amazon_transactions.csv)
  - BestBuy Transactions (bestbuy_transactions.csv)
  - Kmart Transactions (kmart_transactions.csv)
  - Nike Transactions (nike_transactions.csv)
  - Generic Transactions (generic_transactions.csv)
- **Documentation:**
  - Midterm Project Report (Midterm Project Report.pdf)

## Prerequisites

Ensure you have Python 3.6 or newer installed. The following packages are required to run the project:

- mlxtend
- pyfpgrowth
- pandas
- csv

Install them using pip:

```bash
pip install mlxtend pyfpgrowth pandas
```

## Running the Program

### Using Python File

Navigate to the project directory in your terminal and execute:

```bash
python project.py
```

Follow the prompts to select a dataset, and input the support and confidence values.

### Using Jupyter Notebook

First, install Jupyter Lab:

```bash
pip install jupyterlab
```

Then, launch Jupyter Lab:

```bash
jupyter lab
```

Navigate to project.ipynb, open it, and execute the cells in sequence by pressing Shift + Enter. Provide the necessary inputs when prompted.

## Dataset Creation

Five datasets, each with 20 transactions from retailers like Amazon, Kmart, BestBuy, Nike, and a generic dataset, are included. These datasets are integral for running the Apriori algorithm and are stored in CSV format.

## Algorithm Comparison

The project evaluates the efficiency and effectiveness of brute force, Apriori, and FP-Growth algorithms in identifying frequent itemsets and generating association rules from the transaction databases. The comparison focuses on the algorithms' execution time and the accuracy of the results.

## GitHub Repository

Visit the project's GitHub repository for the latest updates and to view the source code:

https://github.com/TarunDeshmukhTetapally/CS634_DataMining_MidTerm
