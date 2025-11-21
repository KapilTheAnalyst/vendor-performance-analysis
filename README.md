End-to-End Sales Analytics Pipeline

Overview

This project presents a complete end-to-end sales analytics pipeline built using Python, SQLite, Jupyter Notebook, SQL, and Power BI. The purpose of the project is to analyze large-scale vendor sales data, uncover performance patterns, and generate actionable insights that can help improve overall company revenue by developing strong relationships with high-performing vendors.

Problem Statement

The company receives millions of sales records across multiple vendors and product categories but lacks a unified system to analyze vendor performance, identify strengths and weaknesses, and make data-driven decisions. The goal was to consolidate the data, transform it into meaningful tables, and generate insights that can help improve vendor relationships and increase revenue.

Dataset

The dataset was obtained from an authentic global retail data repository widely used by organizations for analytics and benchmarking. It contains over 16 million transactional records distributed across six files, capturing vendor details, product details, orders, inventory, and sales performance.

Tools & Technologies

- Python (Pandas, SQLite)

- Jupyter Notebook

- SQL (SQLite)

- Power BI

Methods

1. Data Ingestion: Loaded six large files (~16 million rows) into a SQLite database using Python. 2. Database Creation: Built a structured relational database inside Jupyter using SQLite. 3. Data Exploration: Queried raw tables, validated schema, and assessed data quality. 4. Transformation: Cleaned data, removed inconsistencies, merged tables, and created a comprehensive summary table containing all relevant information. 5. EDA: Performed exploratory data analysis using Python to understand trends and patterns. 6. Insights Generation: Identified top-performing vendors, brands, slow movers, revenue trends, and inventory patterns. 7. Dashboard Creation: Built an interactive Power BI dashboard to visualize KPIs and

trends. 8. Reporting: Compiled findings and explanations into this project report.

Key Insights

- Top-performing vendors significantly contributed to total revenue. - Several low-performing vendors and brands were identified as potential improvement areas. - Inventory insights highlighted which products sold the most and which had slow inventory movement. - Seasonal and monthly sales patterns revealed demand fluctuations. - Vendor relationship strengthening opportunities emerged from performance compariso
Dashboard

An interactive Power BI dashboard was built displaying: - Vendor-wise revenue and performance ranking - Brand analysis (top & low performers) - Inventory movement and sales frequency - Category-level contribution - Time-based sales trends
How to Run This Project

1. Clone or download the project files.
2. Install required Python libraries (Pandas, SQLite3). 
3. Load the dataset files into the SQLite database using the provided Jupyter Notebook.
4. Run SQL queries to create summary tables and insights tables.
5. Use Jupyter Notebook for EDA and insight generation.
6. Import the SQLite database into Power BI using a direct connection.
7. Refresh the dataset and generate the dashboard visualizations.

Result & Conclusion

· Re-evaluate pricing for-sales, high-margin brands to boosts sales volume without sacrificing profitability.

· Diversify vendor partnership to reduce dependency on a few suppliers and mitigate supply chain risks.

· Leverage bulk purchasing advantages to maintain competitive pricing while optimizing inventory management.

· Optimize slow-moving inventory by adjusting purchase qualities, launching clearance sales, or revising storage strategies.

· Enhance marketing and distribution strategies for low-performing vendors to drive higher sales volumes without compromising profit margins.

By implementing these recommendations, the company can achieve sustainable profitability, mitigate risks, and enhance overall operational efficiency.

Future Work

· Convert the manual ETL steps into an automated pipeline using Python scripts or workflow tools like Apache Airflow.

· Schedule automatic data refreshes and database updates.

· Move the dataset (16M+ rows) to MySQL, PostgreSQL, or a cloud data warehouse such as BigQuery or Snowflake to handle larger loads efficiently.

Author Contact Portfolio : https://kapiltheanalyst.github.io/KapilTheAnalyst1.github.io/

Linkedin : www.linkedin.com/in/kapil-kumar11
