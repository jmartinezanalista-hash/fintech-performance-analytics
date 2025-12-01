
SELECT 
    p.prestamo_id,
    c.edad,
    c.score_crediticio,
    p.monto,
    p.estado,
    SUM(pg.monto_pagado) AS total_pagado,
    (p.monto - SUM(pg.monto_pagado)) AS saldo
FROM prestamos p
LEFT JOIN clientes c ON c.cliente_id = p.cliente_id
LEFT JOIN pagos pg ON pg.prestamo_id = p.prestamo_id
GROUP BY 
    p.prestamo_id, c.edad, c.score_crediticio, 
    p.monto, p.estado;
