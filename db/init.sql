CREATE TABLE winners(
    winner_id SERIAL PRIMARY KEY,
    winner_name VARCHAR(255) NOT NULL
);

INSERT INTO winners (winner_name) VALUES ('ido');
INSERT INTO winners (winner_name) VALUES ('ziv');

