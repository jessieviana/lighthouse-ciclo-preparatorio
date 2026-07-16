-- Task B: Produtos com mais de 20 unidades no estoque, custam mais de 50 reais
-- Vamos usar operadores de comparação para filtrar os produtos que atendem a esses critérios
-- e operadores lógicos para combinar as condições.

SELECT ProductName,  UnitPrice, UnitsInStock
FROM Product p 
WHERE UnitsInStock > 20
AND UnitPrice > 50