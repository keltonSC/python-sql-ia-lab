CREATE TABLE orders (id TEXT PRIMARY KEY NOT NULL, expected_cents INTEGER NOT NULL CHECK (expected_cents > 0));
CREATE TABLE payments (id TEXT PRIMARY KEY NOT NULL, order_id TEXT NOT NULL, amount_cents INTEGER NOT NULL CHECK (amount_cents > 0));
CREATE INDEX payments_order_id ON payments (order_id);

INSERT INTO orders VALUES ('A01', 10000), ('A02', 8000), ('A03', 6000), ('A04', 5000);
INSERT INTO payments VALUES ('P1', 'A01', 4000), ('P2', 'A01', 6000), ('P3', 'A02', 1000),
                            ('P4', 'A04', 5500), ('P5', 'A05', 3500);
