# Famous Paintings & Museum Dataset Analysis

## Overview

This project involves analyzing the Famous Paintings & Museum dataset to extract insights using SQL queries. The dataset was loaded into PostgreSQL from CSV files using SQLAlchemy in Python.

## Setup

- **Data Loading**: CSV files were imported into PostgreSQL using SQLAlchemy.
- **Tables**:
  - `paintings`
  - `museums`
  - `work`
  - `product_size`
  - `subject`
  - `image_link`
  - `museum_hours`

## Analysis

1. **Paintings Not Displayed in Museums**: Identified paintings not shown in any museum.
2. **Museums Without Paintings**: Found museums with no paintings displayed.
3. **Paintings with Higher Asking Price**: Counted paintings where asking price > regular price.
4. **Paintings with Asking Price < 50% of Regular Price**: Found paintings with asking price less than 50% of regular price.
5. **Most Expensive Canvas Size**: Determined which canvas size costs the most.
6. **Remove Duplicates**: Cleaned duplicate records in `work`, `product_size`, `subject`, and `image_link`.
7. **Museums with Invalid City Info**: Identified museums with missing or invalid city info.
8. **Invalid Entry in Museum Hours**: Detected and removed an invalid entry in `museum_hours`.
9. **Top 10 Painting Subjects**: Listed the top 10 most popular painting subjects.
10. **Museums Open on Sunday and Monday**: Found museums open on both Sunday and Monday.
11. **Museums Open Every Day**: Counted museums open all seven days.
12. **Top 5 Popular Museums**: Identified the top 5 museums by number of paintings.
13. **Top 5 Popular Artists**: Listed the top 5 artists by number of paintings.
14. **Least Popular Canvas Sizes**: Displayed the 3 least popular canvas sizes.
15. **Museum Open for Longest Duration**: Found the museum open the longest each day.
16. **Museum with Most Popular Style**: Identified the museum with the most popular painting style.
17. **Artists with Paintings in Multiple Countries**: Listed artists with paintings in multiple countries.
18. **City and Country with Most Museums**: Displayed the city and country with the most museums.
19. **Most and Least Expensive Paintings**: Identified the artist and museum for the most and least expensive paintings.
20. **Country with 5th Highest Number of Paintings**: Found the country with the 5th highest number of paintings.
21. **Most and Least Popular Painting Styles**: Listed the top 3 most and least popular painting styles.
22. **Artist with Most Portraits Outside USA**: Identified the artist with the most portrait paintings outside the USA.

## Tools & Technologies

- **Database**: PostgreSQL
- **Data Loading**: SQLAlchemy (Python)
- **Query Language**: SQL

## Conclusion

This project showcases skills in SQL querying and data analysis, handling real-world data challenges effectively.

