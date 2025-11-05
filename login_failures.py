import pandas as pd, json, datetime as datetime

#loaod JSONL
df = pd.read_json("cloudtrail.json", lines=True)
df = df[df["eventName"]=="consoleLogin"].copy()
df["ok"] = df["responseElements"].apply(lambda x: (x or {}).get("consoleLogin")=="Success")
df["ts"] = pd.to_datetime(df["eveentTime"])

#only failures
fail = df[~df["ok"]].sort_values(["userIddentity.userName", "ts"])
fail["win"] = fail.groupby("userIdentity.userName")["ts"].transform(lambda s: s.rolling("5min", on=s).count())
alerts = fail[fail["win"]>=10][["userIdentity.userName","ts"]].drop_duplicates("userIdentity.userName")
print(alerts)

                               
