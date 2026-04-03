import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # Exercise 3: Plotting Visualizations 📊

    **Plot Visuals!**

    **What you'll do:**

    - Create visualizations

    **Instructions:**

    - Complete each TODO section
    - Run cells to see your results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Your First Plot - Bar Chart
    """)
    return


@app.cell
def _():
    import plotly.express as px
    import polars as pl
    sales = pl.read_json("../data/raw/sales.json")
    students = pl.read_csv("../data/raw/students.csv")
    # TODO: Create a bar chart showing sales by category
    # Use plotly express (px.bar)
    # - x-axis: product_category
    # - y-axis: total sales
    # - Add a title
    # - Color the bars

    # Hint: Make sure category_sales is a valid dataframe first!
    category_sales = (
        sales
        .with_columns(pl.col("product_category").str.to_lowercase()) # I noticed some categories were uppercase, so I made them all lowercase for consistency. 
        .group_by("product_category")
        .agg([pl.col("total_amount").sum().alias("total_sales")])
    )


    ex_fig1 = px.bar(
        category_sales,
        x = "product_category",
        y = "total_sales",
        title = "Sales by category",
        color = "product_category"
    )  # Create your plot here

    # Uncomment when ready:
    ex_fig1.show()
    return category_sales, pl, px, sales, students


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Line Chart - Sales Over Time
    """)
    return


@app.cell
def _(pl, px, sales):
    # TODO: Create a line chart showing sales trends by month
    # Use px.line
    # - x-axis: month
    # - y-axis: total revenue
    # - Add markers to the line
    # - Add a title
    sales_trends = (
        sales
        .with_columns(pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed"))
        .with_columns(pl.col("date_parsed").dt.month().alias("month"))
        .group_by("month")
        .agg([                         
            pl.col("total_amount").sum().alias("total_revenue")
        ])                           
        .sort("month")
    )
     # Create your plot here
    ex_fig2 = px.line(
        sales_trends,
        x = "month",
        y = "total_revenue",
        title = "Sales trends by month",
        markers=True
    ) 
    # Uncomment when ready:
    ex_fig2.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Scatter Plot - Exploring Relationships
    """)
    return


@app.cell
def _(px, students):
    # TODO: Create a scatter plot showing the relationship between
    # attendance_rate (x-axis) and test_score (y-axis)
    # - Color points by grade_level
    # - Add a trendline (trendline="ols")
    # - Add appropriate title and labels

    ex_fig3 = px.scatter(
        students,
        x ="attendance_rate",
        y = "test_score",
        color = "grade_level",
        title = "Attendance Rate vs Test Score by Grade Level",
        trendline="ols",
        labels={"attendance_rate": "Attendance Rate", "test_score": "Test Score"}
    )

    # Uncomment when ready:
    ex_fig3.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Histogram - Distribution Analysis
    """)
    return


@app.cell
def _(px, sales):
    # TODO: Create a histogram of transaction amounts (total_amount)
    # - Use 30 bins
    # - Add a title
    # - Label the axes
    # - Try adding nbins=30 parameter
    ex_fig4 = px.histogram(
        sales,
        x = "total_amount",
        nbins=30,
        title = "Distribution of Transaction Amounts",
        labels={"total_amount": "Transaction Amount"}
    )

    # Uncomment when ready:
    ex_fig4.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Advanced - Multiple Subplots
    """)
    return


@app.cell
def _(category_sales, pl, sales):
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    # TODO: Create a dashboard with 2 subplots:
    # 1. Top plot: Bar chart of sales by category (reuse category_sales)
    # 2. Bottom plot: Bar chart of sales by region (reuse region_summary)

    # Hint: Use go.Figure() with make_subplots or add multiple traces
    # This is challenging - check the solution if you get stuck!

    ex_fig5 = make_subplots(
        rows = 2,
        cols = 1,
        subplot_titles = ("Category_sales", "Region_summary")
    )
    ex_fig5.add_trace(
        go.Bar(x=category_sales["product_category"], y=category_sales["total_sales"], name="Sales by Category"),
        row=1, col=1
    )
    region_summary = (
        sales
        .group_by("region")
        .agg(pl.col("total_amount").sum().alias("total_sales"))
    )
    ex_fig5.add_trace(
        go.Bar(x=region_summary["region"], y=region_summary["total_sales"], name="Sales by Region"),
        row=2, col=1
    )
    # Uncomment when ready:
    ex_fig5.show()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the plotting exercises!

    **What you practiced:**

    - ✅ Bar charts
    - ✅ Line charts
    - ✅ Scatter plots
    - ✅ Histograms
    - ✅ Advanced: Subplots
    - ✅ Multiple chart types (bar, line, scatter, histogram)
    - ✅ Combining data analysis with visualization

    **What's next?**

    - Try creating your own visualizations with the data!

    **Pro Tips:**

    - Plotly charts are interactive - hover, zoom, pan!
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
