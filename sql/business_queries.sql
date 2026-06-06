-- Average closing price
SELECT AVG(close_price)
FROM stock_data;

-- Highest traded volume
SELECT *
FROM stock_data
ORDER BY volume DESC
LIMIT 10;
