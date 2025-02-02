# Housing Prices Analysis in San Francisco  

## Overview  
This project analyzes housing prices in San Francisco using a **Venn diagram** to categorize properties based on three features:  
- **Square footage** (`A`)  
- **Number of rooms** (`B`)  
- **Parking availability** (`C`)  

The Venn diagram visually represents price distributions for different housing feature combinations.  

## Features  
- **Uses a dataset of housing prices** with various attributes.  
- **Categorizes properties into binary groups** based on square footage, room count, and parking availability.  
- **Calculates the average price** for each category.  
- **Visualizes results using a Venn diagram** with **Matplotlib** and **matplotlib_venn**.  

## Technologies Used  
- **Python**  
- **Matplotlib** (for visualization)  
- **matplotlib_venn** (for Venn diagram representation)  

## How to Run  
1. Install the required libraries:  
   ```bash
   pip install matplotlib matplotlib_venn
2. Run the script:
   ```bash
   python housing_prices_analysis.py
3. A Venn diagram will display the average housing prices for different feature combinations.

## Visualization
- The **three-circle Venn diagram** represents housing categories.
- Each section displays the **average housing price** for properties in that category.
- Helps in understanding **how features affect price variations**.

## Future Improvements
- Expand the dataset with **real housing market data**.
- Include more features like **neighborhoods, year built, and property type**.
- Implement **interactive visualizations** for better exploration.
