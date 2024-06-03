# Problem 1 : Not Boring Movies (Mock Problem)

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    df = cinema[(cinema.id%2==1) & ~(cinema.description.str.contains('boring'))]
    return df.sort_values(by=['rating'],ascending=False)
    


#  Problem 2 : Biggest Single Number (Mock Problem)

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df1=my_numbers['num'].drop_duplicates(keep=False)

    return pd.DataFrame({'num': [max(df1,default=None)] })


# Problem 3 :Sales Analysis III (Mock Problem)

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales[(sales.sale_date < '2019-01-01' ) | (sales.sale_date > '2019-03-31')]
    df1 = sales[(sales.sale_date >= '2019-01-01' ) & (sales.sale_date <= '2019-03-31')]
    df1 = df1[~df1.product_id.isin(df.product_id)]
    return product[product.product_id.isin(df1.product_id)][['product_id','product_name']]



# Problem 4 : Market Analysis I (Mock Problem)

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders.order_date >= '2019-01-01') & (orders.order_date <= '2019-12-31')].groupby('buyer_id')['order_id'].count().reset_index()
    df = users.merge(orders, how='left', left_on = 'user_id', right_on='buyer_id')
    df['order_id'] = df['order_id'].fillna(0)
    return df[['user_id','join_date','order_id']].rename(columns = {'user_id': 'buyer_id', 'order_id': 'orders_in_2019'})
    