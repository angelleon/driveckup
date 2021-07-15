CREATE TABLE IF NOT EXISTS File (
    id INTEGER IDENTITY,
    name TEXT,
    checksum TEXT,
    size INTEGER,
    uploaded BOOLEAN DEFAULT 0,
    dateAdded DATETIME DEFAULT CURRENT_TIMESTAMP,
    dateModiefied DATETIME DEFAULT NULL
)