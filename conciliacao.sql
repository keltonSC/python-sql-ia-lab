WITH totals AS (
    SELECT order_id, SUM(amount_cents) AS paid
    FROM payments
    GROUP BY order_id
)
SELECT o.id, o.expected_cents, COALESCE(t.paid, 0) AS paid,
       CASE
           WHEN t.order_id IS NULL THEN 'sem pagamento'
           WHEN t.paid < o.expected_cents THEN 'parcial'
           WHEN t.paid > o.expected_cents THEN 'excesso'
           ELSE 'pago'
       END AS status
FROM orders AS o
LEFT JOIN totals AS t ON t.order_id = o.id
UNION ALL
SELECT t.order_id, 0, t.paid, 'pagamento sem pedido'
FROM totals AS t
WHERE NOT EXISTS (SELECT 1 FROM orders AS o WHERE o.id = t.order_id)
ORDER BY 1;
