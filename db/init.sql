CREATE TABLE participants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE weekly_competitaion(
    winner_id int references participants(id),
    winner_score int 
);

CREATE TABLE leader_board(
    winner_id int references participants(id),
    winner_name VARCHAR(255) NOT NULL
);