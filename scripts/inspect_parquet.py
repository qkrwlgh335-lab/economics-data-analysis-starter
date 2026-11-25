"""Run manually in an approved environment. Never share output without review."""
import argparse
from pathlib import Path
import duckdb

def inspect(path, count=False):
    p = Path(path).expanduser().resolve(strict=True)
    if not p.is_file():
        raise ValueError("Select a single file.")
    with duckdb.connect() as con:
        con.execute("SET threads = 2")
        con.execute("SET memory_limit = '512MB'")
        rel = con.read_parquet(str(p))
        print(list(zip(rel.columns, map(str, rel.types))))
        if count:
            print("Rows:", rel.aggregate("count(*)").fetchone()[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", action="store_true")
    args = parser.parse_args()
    path = input("Local Parquet file path: ").strip().strip('"')
    inspect(path, args.count)
