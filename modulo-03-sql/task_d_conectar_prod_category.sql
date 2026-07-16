-- Task D: Product + Category
SELECT Product.ProductName, Product.CategoryId, Category.CategoryName
FROM product
inner join Category
	on Product.CategoryId = Category.Id
order by Category.CategoryName;