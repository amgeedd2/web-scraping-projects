\### Arizona Real Estate Scraper



This project is a web scraping solution developed using Scrapy and Playwright to extract real estate listing data from the website:

https://www.arizonarealestate.com

\# Project Overview

The scraper is designed to navigate the website structure and collect property listings across multiple locations. The workflow is as follows:

Access the homepage

Extract all city or location links from the "Get To Know Arizona" section

Visit each location page

Extract listing data for each property

Handle pagination to traverse all available pages

Export the collected data into a structured CSV file

\# Extracted Data Fields

For each property listing, the following information is collected:

Property title

Location including city and ZIP code

Price

Number of photos

Number of bedrooms

Number of bathrooms

Property size in square feet

Neighborhood name

MLS number

Listing detail URL

Image URL

\# Technologies Used

Python

Scrapy

Scrapy-Playwright for handling JavaScript-rendered content

XPath for data extraction

\# Performance

Total pages crawled: approximately 300 pages

Total records extracted: 94,314 listings

Total execution time: approximately 30 minutes



\# Average performance:

Approximately 30 pages per minute

Approximately 7,000 to 8,000 items per minute



