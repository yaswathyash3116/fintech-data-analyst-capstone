CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    stock_name VARCHAR(100),
    trade_date DATE,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume BIGINT
);
