import sqlite3
import sys
import os
import shutil
import shlex
from itertools import islice

def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", default="~/.local/share/atuin/history.db")
    args = parser.parse_args()

    dbfile = args.db.replace("~", os.getenv("HOME"))
    shutil.copyfile(dbfile, dbfile + ".bak", follow_symlinks=False)

    db = sqlite3.connect(dbfile)

    to_remove = set()
    seen = set()

    cursor = db.execute("SELECT * FROM history ORDER BY timestamp DESC")
    for row in cursor:
        id = row[0]
        _timestamp = row[1]
        _duration = row[2]
        _exit = row[3]
        command = row[4]
        _cwd = row[5]
        _session = row[6]
        _hostname = row[7]

        try:
            parts = shlex.split(command)
        except ValueError:
            to_remove.add(id)
            continue

        if len(parts) == 0 or len(parts) == 1:
            to_remove.add(id)
            continue

        if len(parts[0]) > 256:
            to_remove.add(id)
            continue

        if command in seen:
            to_remove.add(id)
            continue
        seen.add(command)

    for batch in batched(to_remove, 512):
        cond = ','.join('?' * len(batch))
        db.execute(f"DELETE FROM history WHERE id in ({cond})", batch)
    db.commit()



if __name__ == '__main__':
    main()
