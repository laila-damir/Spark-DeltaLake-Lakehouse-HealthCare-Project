# The Spark-Delta Lakehouse Project

This project demonstrates the use of the **Spark ecosystem** to build a comprehensive Business Intelligence (BI) solution for a big data environment, showcasing Spark's capabilities in large-scale data processing, structured streaming, and interactive visualization. It incorporates **Delta Lake** for data storage, **PySpark** for ETL processes, **MDX-like queries** using **Spark's cube methods** for BI analytics, and interactive visualizations using **Bokeh** and **Plotly**.

## Project Steps

1. **Defining Business Intelligence Structures**
   - Creating Data Marts using Delta Lake storage.
   - Building ETL Integration Services for populating Data Marts using PySpark.
   - Testing Slowly Changing Dimension (SCD) capabilities to manage data history effectively.

2. **Working with a Multidimensional BI Semantic Model**
   - Modeling and building a BI cube (Measures and Dimensions) using Spark's `.cube` methods for aggregating data across multiple dimensions.
   - Performing multidimensional analyses by using `.cube` operations in PySpark for BI reporting and analytics.

3. **Structured Streaming**
   - Utilizing Spark's structured streaming capabilities with a dataset of 10,000 rows to perform real-time data processing and updates, demonstrating Spark's flexibility with large data volumes.

4. **Modeling and Visualizing with Bokeh and Plotly**
   - Creating interactive visualizations for healthcare data analysis:
     - **Bar Charts**: Displaying billing amounts segmented by year, gender, and medical condition.
     - **Line Charts**: Representing monthly and quarterly trends in billing amounts over time.
     - **3D Visualizations**: Visualizing `.cube` query results in a 3D space for an in-depth view.
   - Both Bokeh and Plotly were used to enable drill-down, filtering, and other interactive features in visualizations.

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

4. **Run BI Cube Aggregations:**

   Use Spark's `.cube` methods within PySpark to perform multidimensional analyses, exploring measures across various dimension combinations.

5. **Visualize with Bokeh and Plotly:**

   - Use `notebooks/Healthcare.ipynb` to generate visualizations for analysis. Run the cells for:
     - **Bokeh visualizations**: 3D and interactive visuals for `.cube` query results.
     - **Plotly visualizations**: Interactive bar and line charts for billing trends over time, with drill-down options for monthly and quarterly views.

## Project Overview

This project demonstrates how to create a complete data pipeline and BI environment using Spark and Delta Lake, with a focus on scalability, real-time data handling, and interactive visualization. It's designed to handle large datasets, manage changing data dimensions, and deliver insights through accessible visualizations.
