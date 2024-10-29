
# The Spark-Delta Lakehouse Project

This project demonstrates the use of the **Spark ecosystem** to build a Business Intelligence (BI) solution for a big data environment, showcasing the effectiveness of Spark in handling large-scale data processing and analysis. It incorporates **Delta Lake** for data storage, **PySpark** for ETL processes, **MDX-like** queries using **Spark SQL** for BI analytics, and **Bokeh** for interactive data visualization.

## Project Steps

1. **Defining Business Intelligence Structures**
    - Creating Data Marts using Delta Lake storage.
    - Building ETL Integration Services for populating Data Marts using PySpark.
    - Testing Slowly Changing Dimension (SCD) capabilities.

2. **Working with a Multidimensional BI Semantic Model**
    - Modeling and building a BI cube (Measures and Dimensions) using Spark.
    - Executing MDX-like queries with Spark SQL.

3. **Modeling and Visualizing with Bokeh**
    - Connecting Spark data to Bokeh for interactive visualizations, enabling drill-down and roll-up features.




## Requirements

- Docker
- Python 3.8+
- Spark (configured via Docker)
- Delta Lake
- JupyterLab (for working with notebooks)

To install Python dependencies, run:

```bash
pip install -r requirements.txt
```

## Setup and Usage

1. **Build and Run the Docker Image:**

   ```bash
   docker build -t spark-deltalake-lakehouse .
   docker run -it -p 8888:8888 spark-deltalake-lakehouse
   ```

   This will set up the Spark and Delta Lake environment and expose Jupyter Notebook on port 8888.

2. **Run Jupyter Notebooks:**

   Open the Jupyter Notebook interface in your browser by visiting `http://localhost:8888`.

3. **Execute ETL and Transformations:**

   Inside `notebooks/Healthcare.ipynb`, run the cells to perform ETL operations, data cleansing, and transformation.

4. **Run BI Queries:**

   Execute MDX-like queries stored in `queries.sql` using Spark SQL. You can either load them directly or run the example queries in the script files.

5. **Visualize with Bokeh:**

   You can run the cells of `notebooks/Healthcare.ipynb` corresponding to visualization, to generate 3D visualizations for different MDX-like queries.



## Project Overview

This project demonstrates how to create a complete data pipeline and BI environment using Spark and Delta Lake, with a focus on scalability and interactive visualization. It's designed to handle large datasets, manage changing data dimensions, and deliver insights through accessible visualizations.

