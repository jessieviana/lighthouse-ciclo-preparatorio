-- Task C: Valor total vendido por produto
SELECT ProductId, SUM(UnitPrice * Quantity)  AS valorTotal
FROM OrderDetail
GROUP BY ProductId;

--Valor médio dos pedidos
SELECT avg(UnitPrice * Quantity) AS valorMedio
FROM OrderDetail;
  