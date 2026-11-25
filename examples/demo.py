"""Synthetic transactions only. No external files or network."""
import duckdb
import statsmodels.api as sm

def demo():
    with duckdb.connect() as con:
        con.execute("""
            CREATE TABLE synthetic AS
            SELECT i AS id, i % 12 + 1 AS month,
                   100 + 2 * i + (i % 7) * 3 AS amount,
                   i % 2 AS group_id
            FROM range(1, 241) t(i)
        """)
        print(con.sql("SELECT month, count(*) AS n, sum(amount) AS total FROM synthetic GROUP BY month ORDER BY month").df())
        df = con.sql("SELECT id, amount, group_id FROM synthetic ORDER BY id").df()
        model = sm.OLS(df["amount"], sm.add_constant(df[["id", "group_id"]])).fit(cov_type="HC3")
        print(model.summary())
        return len(df), float(model.params["id"])

if __name__ == "__main__":
    demo()
