<p align="center">
  <img src= logo.png alt="Sublime's custom image"/>
</p>

# Business Problem

The company Fome Zero is a restaurant marketplace. In other words, its core business is to facilitate meetings and negotiations with customers and restaurants. Restaurants register within the Fome Zero platform, which provides information such as address, type of cuisine served, if they have reservations, if they make deliveries and also an evaluation note of the restaurant's services and products, among other information.


The company's CEO was recently hired and needs to understand the business better to be able to make the best strategic decisions and further leverage Zero Hunger. For this, he needs an analysis of the company's data and the generation of dashboards, based on these analyses, in order to map the base of registered restaurants and understand the progress of the business through the following information:

**📋 Overview**

  1. Number of registered restaurants and where they are located;
   2. Number of countries and cities where Fome Zero operates;
   3. Number of cuisines offered;
   4. Number of restaurants according to their characteristics:
      * Do you accept reservation?
      * Do you accept online orders?
      * Do you deliver?
   5. Number of assessments made on the platform;
   6. Best restaurants (highest ratings).
    
**🌍 Country Vision**

  1. Number of registered restaurants in each country of operation;
  2. Number of cities where Fome Zero is present in the countries where it operates;
  3. Gastronomic diversity of each country (number of unique cuisines offered);
  4. Countries with the highest number of evaluations performed;
  5. Average evaluation score of the services in each country;
  6. Average cost across countries.
    
**🏨 City View**

  1. Which cities in each country of operation have the highest number of registered restaurants?
  2. Cities with the best and worst average ratings and which countries they are in;
  3. Cities with greater gastronomic diversity;
  4. Cities with higher costs and worse evaluations;
  5. Cities with lower costs and better ratings.
    
**🍴 Gastronomic Vision**

  1. Types of dishes that are the basis of Fome Zero's offer;
  2. Worst and best evaluated dishes;
  3. Most expensive and worst evaluated dishes;
  4. Cheapest and best rated dishes.

The challenge is to answer these questions and turn your results into dashboards that allow a quick understanding of the business progress. Company data can be obtained from the Kaggle link below (zomato.csv file):
https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv

# Business Assumptions

1. The assumed business model is a Marketplace;
2. The database does not contain date information, therefore the analyzes do not include the temporal dimension;
3. The analytical views adopted were: country, city and gastronomy;
4. Restaurants that had an average cost of a dish for two equal to 0 were excluded from the base because it did not make sense for the analysis;
5. Given that the countries in which Fome Zero operates have different currencies, it was decided not to standardize the financial data - the definition of how cheap or expensive a restaurant can be was given by the variable “prince_range”, from which the variable “ price_type” with the following values:
     * 1 - Cheap ;
     * 2 - Normal;
     * 3 - Expensive;
     *4 - Gourmet.
6. Any analysis that includes financial data in the country's currency will be presented together with the data.

# Solution Strategy

 1. The analyzes started from the resolution of the questions proposed by the CEO segmented by the visions of country, city and gastronomy;
 2. In terms of tooling, the following were used:
     * Jupyter Notebook - Preview analysis and final script draft;
     * Data manipulation libraries - Pandas and Numpy;
     * Data visualization libraries - Matplotlib, Plotly, Folium;
     * Jupyter Lab - Ultimate Python Script;
     * Streamlit and Streamlit Cloud- Visualization of the dashboard and put it in production.

# Top 3 Data Insights

1. Only about half of the restaurants that accept online orders also deliver;
2. Brazil has the worst operation: only 3 cities registered, all appearing in the top 5 of the worst evaluated cities, which also places it as the country with the worst average evaluation score. It is the only one in South America;
3. None of the 10 most offered cuisines are among the best evaluated, on the contrary, 6 of them are among the 20 most expensive and worst evaluated (seafood, continental, pizza, Italian, cafe and American).

# The Final Product of the Project

Online dashboard hosted on Streamlit Cloud which can be accessed through the link:

https://jhmartire-fome-zero-home.streamlit.app/

# Conclusion

The objective of the project was to create a data visualization that would allow the monitoring of the main characteristics of the business and how they are geographically distributed.

The Fome Zero marketplace has a global presence with a strong presence in Asia and North America, offering significant gastronomic diversity with dishes from North India as the basis of its menu.

# Next Steps

1. Specialize analysis by country, generating more local business monitoring metrics in order to make decision-making processes more precise according to geographic particularities;
2. Standardize financial and evaluation data in order to make the comparison between restaurants and countries more fair/accurate in the analysis;
3. Analyze the cost and/or benefit of expanding or contracting gastronomic diversity considering the price of the dishes and the evaluations of the restaurants.
