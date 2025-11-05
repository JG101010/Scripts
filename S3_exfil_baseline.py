import pandas as pd
df = pd.read_csv("s3_daily_counts.csv", parse_dates=["date"])
df - df.sort_values(["user","date"])

#30 day rolling baseline (excluding current day)
df["mu"] = df.groupby("user")["s3_getobject_count"].transform(lambda s: s.shift(1).rolling(30,min_periods=7).mean())
df["sigma"] = df.groupby("user")["s3_getobject_count"].transform(lambda s: s.shift(1).rolling(30,min_periods=7).std())
df["threshold"] = df["mu"] + 3*df["sigma"]
alerts = df[(df["mu"].notna()) & (df["s3_getobject_count"] > df["threashold"])]
print(alerts[["user", "date", "s3_getobject_count", "threshold"]].head())
