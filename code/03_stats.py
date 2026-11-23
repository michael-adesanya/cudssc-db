"""Write data/processed/stats.json from records_v1.csv. README numbers come from this file."""
import csv, json, statistics, collections
rows = list(csv.DictReader(open("data/processed/records_v1.csv", encoding="utf-8")))
inc = [r for r in rows if r["status"] == "INCLUDED"]
pce = sorted((float(r["pce_pct"]), r["doi"]) for r in inc if r["pce_pct"])
vals = [p for p, _ in pce]
stats = {
    "records_total": len(rows),
    "records_included": len(inc),
    "records_held_si_needed": sum(r["status"] == "HOLD_SI_NEEDED" for r in rows),
    "pce_min_pct": pce[0][0], "pce_min_doi": pce[0][1],
    "pce_max_pct": pce[-1][0], "pce_max_doi": pce[-1][1],
    "pce_median_pct": round(statistics.median(vals), 2),
    "records_with_all_four_parameters": sum(all(r[k] for k in ("voc_mV", "jsc_mA_cm2", "ff", "pce_pct")) for r in inc),
    "years": dict(sorted(collections.Counter(r["year"] for r in inc).items())),
}
json.dump(stats, open("data/processed/stats.json", "w"), indent=2)
print(json.dumps(stats, indent=2))
