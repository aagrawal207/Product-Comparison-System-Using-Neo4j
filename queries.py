from neo4j.v1 import GraphDatabase, basic_auth
from check_error import *

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "ayush@12"))
session = driver.session()

def add_queries(name, website, price, stock, rating, type1):
    if int_check(stock) == False:
        error_msg()
        return False
    else:
        stock = int(stock)
    if float_check(price):
        price = float(price)
    else:
        error_msg()
        return False
    session.run("""merge (site:website{name:$website}) merge(a:product{name:$name}) merge(a)-[r:sold_by]->(site)
                on create set r.price=$price ,r.stock=$stock,r.rating=$rating
                on match set r.price =$price,r.stock = r.stock +$stock,r.rating=$rating""",name=name,
                rating=rating,price = price,stock = stock,website=website)
    session.run("match (x:product{name:$name}) merge(b:product_type{type:$type}) merge(x)-[:of_type]->(b)",
                name=name,type=type1)

def show_all_queries():
    result = session.run("""match(a:product)-[r:of_type]->(b:product_type),(a)-[x:sold_by]->(site:website)
                            return distinct a.name as name,b.type as type
                            order by b.type""")
    return result

def delete_queries(name, website, stock):
    if int_check(stock) == False:
        error_msg()
        return False
    else:
        stock = int(stock)
    result = session.run('''match(a:product{name:$name})-[r:sold_by]->(b:website{name:$website}) return r.stock as p''',name=name,website=website)
    cnt = 0
    for record in result:
        result = record["p"]
        cnt = cnt + 1
    if cnt == 0:
        print("Empty")
    elif result > stock:
        session.run('''match(a:product{name:$name})-[r:sold_by]->(b:website{name:$website}) set r.stock=r.stock-$stock''', name=name, website=website,stock=stock)
    elif result > 0:
        session.run('''match(a:product{name:$name})-[r:sold_by]->(b:website{name:$website}) delete r''', name=name, website=website)

def go_queries(prod, min_price, max_price, rating):
    if float_check(min_price) and float_check(max_price):
        min_price = float(min_price)
        max_price = float(max_price)
    else:
        error_msg()
        return False, False
    result1 = session.run("""match (t:product_type)<-[:of_type]-(a:product)-[r:sold_by]->(b:website)
                          where r.price <= $max_price and r.rating>=$rating and r.price >=$min_price
                           return a.name as name,r.price as price,r.rating as rating,b.name as website,
                          t.type as type order by r.rating desc""",
                         name = prod,min_price=min_price,max_price=max_price,rating=rating)

    result2 = session.run("""match (a:product_type{type:$name})<-[:of_type]-(b:product)-[r:sold_by]
                      -> (c:website) where r.price <= $max_price and r.rating>=$rating and r.price >=$min_price
                        return b.name as name,r.price as price,r.rating as rating,c.name as website,
                        a.type as type order by r.rating desc""",
                      name=prod, min_price=min_price, max_price=max_price, rating=rating)
    return result1, result2
