-- Task A: A CEO pediu uma lista dos nomes e de todos os produtos e seus preços

SELECT ProductName, UnitPrice 
FROM Product p;
-- Agora, vamos organizar os produtos por preço em ordem decrescente
order by UnitPrice DESC;