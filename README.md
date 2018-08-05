```
let
    Source = Table.NestedJoin(#"order_products__train (3)",{"product_id"},products,{"product_id"},"products",JoinKind.LeftOuter),
    #"Expanded products" = Table.ExpandTableColumn(Source, "products", {"product_name", "aisle_id", "department_id"}, {"products.product_name", "products.aisle_id", "products.department_id"})
in
    #"Expanded products"
```	
	
	
```	
	let
    Source = Table.NestedJoin(#"order_products__train (2)",{"product_id"},products,{"product_id"},"products",JoinKind.LeftOuter),
    #"Expanded products" = Table.ExpandTableColumn(Source, "products", {"product_id", "product_name", "aisle_id", "department_id"}, {"products.product_id", "products.product_name", "products.aisle_id", "products.department_id"})
in
    #"Expanded products"
```
```	
	
	let
    Source = Table.NestedJoin(order_products__train,{"order_id"},orders,{"order_id"},"orders",JoinKind.LeftOuter),
    #"Expanded orders" = Table.ExpandTableColumn(Source, "orders", {"order_id", "user_id", "eval_set", "order_number", "order_dow", "order_hour_of_day", "days_since_prior_order"}, {"orders.order_id", "orders.user_id", "orders.eval_set", "orders.order_number", "orders.order_dow", "orders.order_hour_of_day", "orders.days_since_prior_order"}),
    #"Grouped Rows" = Table.Group(#"Expanded orders", {"orders.days_since_prior_order"}, {{"meanreordered", each List.Average([reordered]), type number}})
in
    #"Grouped Rows"
```	
	
```	
	let
    Source = Table.NestedJoin(#"order_products__train (2)",{"product_id"},products,{"product_id"},"products",JoinKind.LeftOuter),
    #"Expanded products" = Table.ExpandTableColumn(Source, "products", {"product_id", "product_name", "aisle_id", "department_id"}, {"products.product_id", "products.product_name", "products.aisle_id", "products.department_id"}),
    #"Sorted Rows" = Table.Sort(#"Expanded products",{{"pct", Order.Descending}})
in
    #"Sorted Rows"
	
```	
```	
	let
    Source = Csv.Document(File.Contents("C:\Users\Sandy\Documents\instacart\order_products__train.csv"),[Delimiter=",", Columns=4, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
in
    #"Promoted Headers"
```	
	
	
```	
	let
    Source = Table.NestedJoin(#"order_products__train (5)",{"product_id"},order_products__train,{"product_id"},"order_products__train",JoinKind.LeftOuter),
    #"Expanded order_products__train" = Table.ExpandTableColumn(Source, "order_products__train", {"order_id", "add_to_cart_order", "reordered"}, {"order_products__train.order_id", "order_products__train.add_to_cart_order", "order_products__train.reordered"})
in
    #"Expanded order_products__train"
	
```	
	
```	
	let
    Source = Table.NestedJoin(#"products (2)",{"department_id"},#"departments (2)",{"department_id"},"departments (2)",JoinKind.LeftOuter)
in
    Source
```	

```	
	let
    Source = Table.NestedJoin(Merge1,{"aisle_id"},#"aisles (2)",{"aisle_id"},"aisles (2)",JoinKind.LeftOuter)
in
    Source
```	
```	
	let
    Source = Table.NestedJoin(Merge1,{"aisle_id"},#"aisles (2)",{"aisle_id"},"aisles (2)",JoinKind.LeftOuter)
in
    Source
```
```	
	let
    Source = Table.NestedJoin(#"order_products__train (2)",{"product_id"},products,{"product_id"},"products",JoinKind.LeftOuter),
    #"Expanded products" = Table.ExpandTableColumn(Source, "products", {"product_id", "product_name", "aisle_id", "department_id"}, {"products.product_id", "products.product_name", "products.aisle_id", "products.department_id"}),
    #"Grouped Rows" = Table.Group(#"Expanded products", {"products.department_id", "products.aisle_id"}, {{"Count", each List.Sum([Count]), type number}})
in
    #"Grouped Rows"

```	
```	
	let
    Source = Table.NestedJoin(Merge3,{"products.aisle_id", "products.department_id"},Merge2,{"aisle_id", "department_id"},"Merge2",JoinKind.LeftOuter)
in
    Source
	
	
```	
	
	let
    Source = Csv.Document(File.Contents("C:\Users\Sandy\Desktop\data_assigns\project\instacart\aisles.csv"),[Delimiter=",", Columns=2, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"aisle_id", Int64.Type}, {"aisle", type text}})
in
    #"Changed Type"
	
```
```	
	let
    Source = Csv.Document(File.Contents("C:\Users\Sandy\Desktop\data_assigns\project\instacart\departments.csv"),[Delimiter=",", Columns=2, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"department_id", Int64.Type}, {"department", type text}})
in
    #"Changed Type"
```
```	

	
	let
    Source = Csv.Document(File.Contents("C:\Users\Sandy\Desktop\data_assigns\project\instacart\products.csv"),[Delimiter=",", Columns=4, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"product_id", Int64.Type}, {"product_name", type text}, {"aisle_id", Int64.Type}, {"department_id", Int64.Type}})
in
    #"Changed Type"
	
```	
	-------------------------
	
	
```	
	let
    Source = Csv.Document(File.Contents("C:\Users\Sandy\Desktop\data_assigns\project\instacart\order_products__prior.csv"),[Delimiter=",", Columns=3, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"order_id", Int64.Type}, {"product_id", Int64.Type}, {"reordered", Int64.Type}}),
    #"Grouped Rows" = Table.Group(#"Changed Type", {"order_id"}, {{"m", each List.Median([reordered]), type number}})
in
    #"Grouped Rows"

```
```	
	let
    Source = Csv.Document(File.Contents("C:\Users\Sandy\Desktop\data_assigns\project\instacart\orders.csv"),[Delimiter=",", Columns=4, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"order_id", Int64.Type}, {"user_id", Int64.Type}, {"eval_set", type text}, {"order_number", Int64.Type}}),
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each [order_number] > 2)
in
    #"Filtered Rows"
	```
```
	
	let
    Source = Table.NestedJoin(#"order_products__prior (2)",{"order_id"},#"orders (2)",{"order_id"},"orders (2)",JoinKind.RightOuter),
    #"Expanded orders (2)" = Table.ExpandTableColumn(Source, "orders (2)", {"order_id", "user_id", "eval_set", "order_number"}, {"orders (2).order_id", "orders (2).user_id", "orders (2).eval_set", "orders (2).order_number"}),
    #"Filtered Rows" = Table.SelectRows(#"Expanded orders (2)", each ([m] = 1)),
    #"Grouped Rows" = Table.Group(#"Filtered Rows", {"orders (2).user_id"}, {{"n_equal", each List.Sum([m]), type number}})
in
    #"Grouped Rows"
```
```	
	let
    Source = Table.NestedJoin(#"order_products__prior (2)",{"order_id"},#"orders (2)",{"order_id"},"orders (2)",JoinKind.RightOuter),
    #"Expanded orders (2)" = Table.ExpandTableColumn(Source, "orders (2)", {"order_id", "user_id", "eval_set", "order_number"}, {"orders (2).order_id", "orders (2).user_id", "orders (2).eval_set", "orders (2).order_number"}),
    #"Filtered Rows" = Table.SelectRows(#"Expanded orders (2)", each ([m] = 1)),
    #"Grouped Rows" = Table.Group(#"Filtered Rows", {"orders (2).user_id"}, {{"n_equal", each List.Sum([m]), type number}})
in
    #"Grouped Rows"
```