-- Add migration script here
-- I am not entirely sure if this would always run, so it just stays here as is.

PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

DROP INDEX idx_history_timestamp;
DROP INDEX idx_history_command;
DROP INDEX idx_history_command_timestamp;

ALTER TABLE history RENAME TO history2;
CREATE TABLE history (
        id text primary key,
        timestamp integer not null,
        duration integer not null,
        exit integer not null,
        command text not null,
        cwd text not null,
        session text not null,
        hostname text not null,
        deleted_at integer,

        unique(command)
);

INSERT OR IGNORE INTO history SELECT * FROM history2 ORDER BY timestamp DESC;

CREATE INDEX idx_history_timestamp on history(timestamp);
CREATE INDEX idx_history_command on history(command);
CREATE INDEX idx_history_command_timestamp on history(
        command,
        timestamp
);

DROP TABLE history2

COMMIT;

PRAGMA foreign_keys=on;
