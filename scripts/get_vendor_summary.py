import pandas as pd
import sqlite3
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename=logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s -%(levelname)s  -%(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    ''' this function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS(
    SELECT
        VendorNumber,
        SUM(Freight) AS FreightCost
    FROM vendor_invoice
    GROUP BY VendorNumber        
),
PurchaseSummary AS(
    SELECT
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        p.Description,
        p.PurchasePrice,
        pp.Price AS ActualPrice,
        pp.Volume,
        SUM(p.Quantity) AS TotalPurchaseQuantity,
        SUM(p.Dollars) AS TotalPurchaseDollars
    FROM purchases p
    JOIN purchase_prices pp
        ON p.Brand=pp.Brand
    WHERE p.PurchasePrice >0
    GROUP BY p.VendorNumber , p.VendorName , p.Brand , p.Description , p.PurchasePrice, pp.Price, pp.Volume
),
salesSummary AS (
    SELECT 
        VendorNo,
        Brand,
        SUM(SalesQuantity) AS TotalSalesQuantity,
        SUM(SalesDollars) AS TotalSalesDollars,
        SUM(SalesPrice) AS TotalSalesPrice,
        SUM(ExciseTax) AS TotalExciseTax
    FROM sales
    GROUP BY VendorNo, Brand
)
SELECT
    ps.VendorNumber,
    ps.VendorName,
    ps.Brand,
    ps.Description,
    ps.PurchasePrice,
    ps.ActualPrice,
    ps.Volume,
    ps.TotalPurchaseQuantity,
    ps.TotalPurchaseDollars,
    ss.TotalSalesQuantity,
    ss.TotalSalesDollars,
    ss.TotalSalesPrice,
    ss.TotalExciseTax,
    fs.FreightCost
FROM PurchaseSummary ps
LEFT JOIN SalesSummary ss
    ON ps.vendorNumber = ss.VendorNo
    AND ps.Brand = ss.Brand
LEFT JOIN FreightSummary fs
    ON ps.VendorNumber = fs.VendorNumber
ORDER BY ps.TotalPurchaseDollars DESC""",conn)
    return vendor_sales_summary

def clean_data(df):
    ''' this function clean the data'''

       # changing the datatype of vulume
      df['Volume'] = df['Volume'].astype('float64')

      # Filling missing values with zero 
      df.fillna(0, inplace = True)

      # removes spaces from categorical data
      df['VendorName'] = df['VendorName'].str.strip()


     # creating new column for analysis

     # gross profits of vendors
     df['Gross Profit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']

     # Profit margin of vanders
        df['ProfitMargin'] = (df['Gross Profit'] /df['TotalSalesDollars'])*100 

    # Stock Turnover of vendors
      df['StockTurnover'] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']

    # Sales Purchase ratio of venders
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars']/df['TotalPurchaseDollars']

  return df

if  __name__ == '__main__':
    # creating database connection
    conn = sqlite3.connect('inventory.db')

    logging.info('creating Vendor Summary Table...')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleaning Data....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())


    logging.info('Ingestion data .....')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')

        
    