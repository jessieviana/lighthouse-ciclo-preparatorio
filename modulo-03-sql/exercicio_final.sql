-- A CEO quer saber: quais são as 3 categorias de produtos que geraram mais receita? 
SELECT c.CategoryName, SUM(od.UnitPrice * od.Quantity) AS valorTotal
FROM OrderDetail od
inner join Product p
    on od.ProductId = p.Id
inner join Category c
    on p.CategoryId = c.Id
GROUP BY c.CategoryName
order by valorTotal DESC
LIMIT 3;