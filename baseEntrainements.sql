CREATE TABLE IF NOT EXISTS entrainements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL,
    seance TEXT NOT NULL,
    duree TEXT NOT NULL,
    repetitions TEXT NOT NULL,
    intensite INTEGER NOT NULL
);