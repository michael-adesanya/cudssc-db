"""Assemble CuDSSC-DB draft records and run QA.

Values below were read by Claude from the open-access PDFs (or, where noted, from
publisher web pages) and were checked by the author against the sources (see docs/VERIFICATION.md).
Nothing is calculated into a record; a value the paper does not state is left empty.
Run: python3 code/02_build.py   (from the repository root)
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "processed")

COLS = ["doi", "year", "status", "mediator", "dye", "electrolyte_additives",
        "counter_electrode", "mask_area_cm2", "voc_mV", "jsc_mA_cm2", "ff", "pce_pct",
        "value_type", "spread", "light", "stability", "locator", "license_on_page",
        "source_read", "flags"]

R = []


def add(**k):
    R.append({c: k.get(c, "") for c in COLS})


add(doi="10.1021/acs.energyfuels.4c06413", year=2025, status="INCLUDED",
    mediator="[Cu(dsbtmp)2]2+/+ (dsbtmp = 2,9-di(sec-butyl)-3,4,7,8-tetramethyl-1,10-phenanthroline); 0.1 M Cu(I) PF6 / 0.05 M Cu(II) (PF6)2 in acetonitrile",
    dye="none (single-component: the copper complex in solution is sensitizer and shuttle)",
    electrolyte_additives="0.1 M LiPF6; 0.5 M 4-tert-butylpyridine (TBP)",
    counter_electrode="not extracted", mask_area_cm2="not extracted",
    voc_mV=650, jsc_mA_cm2=0.097, ff="", pce_pct=0.045,
    value_type="mean (batch of 5 cells)", spread="Voc +/-23 mV; Jsc +/-0.020 mA/cm2; PCE spread not reported",
    light="AM1.5G 100 mW/cm2", stability="NOT REPORTED (text search)",
    locator="Results, paragraph on Figure 3a", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="Author is co-author of this paper; proof-of-concept efficiency; FF not stated; without TBP Voc 0.2 V and Jsc 0.03 mA/cm2")

add(doi="10.1039/c6ra25676g", year=2017, status="INCLUDED",
    mediator="[Cu(dmbp)2]2+/1+; 0.10 M Cu(dmbp)2BF4 / 0.05 M Cu(dmbp)2(BF4)2 in acetonitrile",
    dye="Y123", electrolyte_additives="0.50 M TBP; 0.10 M LiBF4",
    counter_electrode="not extracted", mask_area_cm2=0.126,
    voc_mV=1048, jsc_mA_cm2=14.4, ff=0.681, pce_pct=10.3,
    value_type="mean +/- SD (number of cells not extracted)",
    spread="Voc +/-7 mV; Jsc +/-0.2; FF +/-0.5 %; PCE +/-0.1",
    light="AM1.5G 100 mW/cm2", stability="NOT REPORTED (text search)",
    locator="Table 1; Results text", license_on_page="CC BY 3.0 Unported (PDF statement)",
    source_read="PDF", flags="I3-/I- and Co(bpy)3 comparison cells in same table are not Cu and are not recorded")

add(doi="10.1021/acs.jpcc.9b11778", year=2020, status="INCLUDED",
    mediator="[Cu(tmby)2]TFSI 0.2 M / [Cu(tmby)2](TFSI)2 0.04 M",
    dye="Y123 (0.2 mM CDCA in dye bath)", electrolyte_additives="0.1 M LiTFSI; 0.6 M TBP",
    counter_electrode="not extracted", mask_area_cm2=0.16,
    voc_mV=1080, jsc_mA_cm2=10.57, ff=0.75, pce_pct=8.55,
    value_type="champion (best cell, untreated Y123)", spread="same condition average: PCE 8.01 +/-0.18",
    light="AM1.5G (Newport 91160); 100 mW/cm2 not stated in the text read", stability="NOT REPORTED (text search)",
    locator="Table 1 (Y123, pristine, best cell)", license_on_page="CC-BY (PDF statement)",
    source_read="PDF", flags="Table 1 also lists D205 and D205Si dyes and MC and CB7 treatments; the highest-PCE Cu cell was chosen")

add(doi="10.1016/j.electacta.2024.144221", year=2024, status="INCLUDED",
    mediator="Cu(II/I)-based redox electrolyte (composition not in main text; see SI)",
    dye="not stated in main text", electrolyte_additives="not stated in main text",
    counter_electrode="dry-deposited SWCNT (Pt-CE comparison 5.18 %)", mask_area_cm2=0.35,
    voc_mV=1030, jsc_mA_cm2=9.35, ff=0.5474, pce_pct=5.30,
    value_type="mean +/- SD (6 cells)", spread="Voc +/-0.02 V; Jsc +/-0.20; FF +/-3.35 %; PCE +/-0.26",
    light="'Full sun' (intensity not stated as 100 mW/cm2 in the table)",
    stability="ISOS-D-1 dark storage >650 h; ISOS-L-1 light soaking at 1500 lux; retention in Table 5 (not extracted)",
    locator="Table 2", license_on_page="CC BY (PDF statement)",
    source_read="PDF", flags="Counter-electrode study; mediator and dye identity need the SI; champion cell values only in Figure 3")

add(doi="10.1016/j.jpowsour.2025.237019", year=2025, status="INCLUDED",
    mediator="[Cu(dmp)2]2+/+; 0.2 M CuI(dmp)2TFSI / 0.04 M CuII(dmp)2(TFSI)2 in acetonitrile",
    dye="Y123 (0.3 mM)", electrolyte_additives="0.1 M LiTFSI; 0.6 M 4TBP; 0.5 wt% Ti3C2 MXene (CLEM device)",
    counter_electrode="carbon (Elcocarb B/SP)", mask_area_cm2=0.35,
    voc_mV=991, jsc_mA_cm2=10.94, ff=0.69, pce_pct=7.45,
    value_type="champion", spread="average of 8 devices: PCE 6.02 +/-1.04; control without MXene champion PCE 6.96",
    light="100 mW/cm2 simulated 1-Sun", stability="MPP tracking 20 h; stabilized current ~90 % at 100 mW/cm2 and ~99 % at 10 mW/cm2",
    locator="Table 1 (CLEM, 100 mW/cm2)", license_on_page="CC BY (PDF statement)",
    source_read="PDF", flags="MXene-additive device chosen as the best cell; control (CLE) also available")

add(doi="10.1021/acsaem.6c01356", year=2026, status="INCLUDED",
    mediator="Cu(I)(tmby)2TFSI 0.1 M / Cu(II)(tmby)2(TFSI)2 0.04 M in acetonitrile",
    dye="Y123 + XY1b (dye solution mixed in equal volume; confirm)", electrolyte_additives="0.1 M LiTFSI; 0.6 M N-methylbenzimidazole (NMB)",
    counter_electrode="carbon (Elcocarb B/SP)", mask_area_cm2=0.071,
    voc_mV=920, jsc_mA_cm2=12.8, ff=0.745, pce_pct=9.0,
    value_type="mean +/- SD (3 identical devices)", spread="Voc +/-0.001 V; Jsc +/-0.1; FF +/-0.001; PCE +/-0.1",
    light="AM1.5G 100 mW/cm2", stability="not extracted",
    locator="Table 3 (ACN solvent)", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="Monolithic cell; other solvents (MPN, NMP, PC, GBL) gave 2.2 to 3.5 %; indoor data (300 to 1000 lx) not recorded")

add(doi="10.1021/acssuschemeng.4c07717", year=2025, status="INCLUDED",
    mediator="Cu(dmby)2TFSI / Cu(dmby)2TFSI2 in acetonitrile (Liquid-1: 0.2 M / 0.06 M; Liquid-2: 0.1 M / 0.03 M; which one is in Table 1 to confirm)",
    dye="Y123 + CDCA", electrolyte_additives="NMBI (1.1 M Liquid-1; 0.9 M Liquid-2); 0.1 M LiTFSI",
    counter_electrode="PEDOT", mask_area_cm2="not found",
    voc_mV=1050, jsc_mA_cm2=14.39, ff=0.643, pce_pct=9.69,
    value_type="mean +/- SD (liquid electrolyte, sandwich cell)", spread="Voc +/-0.002 V; Jsc +/-0.369; FF +/-0.013; PCE +/-0.287",
    light="1-Sun (value not stated as 100 mW/cm2 in the text read)", stability="not extracted",
    locator="Table 1 (liquid electrolyte)", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="The paper's headline 'over 36 %' is not a 1-sun value; quasi-solid gel cells give 9.54 % and 9.18 % at 1 sun")

add(doi="10.1021/acssuschemeng.4c00909", year=2024, status="INCLUDED",
    mediator="CuI/II(dmby)2 acetate salts, aqueous; 0.1 M CuI / 0.05 M CuII",
    dye="C106", electrolyte_additives="0.1 M LiOAc; 2.3 M HNMBI+OAc-; 1 % PEG-200; pH ~5 (electrolyte E2)",
    counter_electrode="not extracted", mask_area_cm2=0.283,
    voc_mV=736, jsc_mA_cm2=2.49, ff=0.57, pce_pct=1.05,
    value_type="mean of 4 identical sets", spread="Voc +/-5 mV; Jsc +/-0.05; FF and PCE spread not reported",
    light="1 Sun 100 mW/cm2", stability="reported under constant ambient light (details not extracted)",
    locator="Table 2 (E2)", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="Aqueous electrolyte; low 1-sun efficiency; the paper's emphasis is ambient light")

add(doi="10.1021/acsaem.1c02789", year=2022, status="INCLUDED",
    mediator="Cu(I)(dc-dmbpy)2Cl 0.1 M / Cu(II)(dc-dmbpy)2Cl2 0.05 M in water",
    dye="C106", electrolyte_additives="0.1 M KCl; 0.1 M LiClO4; 0.5 % Triton X-100; pH 5.6 to 5.8",
    counter_electrode="not extracted", mask_area_cm2="0.25 active (0.36 mask)",
    voc_mV=559, jsc_mA_cm2=2.6, ff=0.43, pce_pct=0.63,
    value_type="unspecified", spread="not reported", light="AM1.5G 100 mW/cm2", stability="not extracted",
    locator="Table 1 (C106)", license_on_page="CC BY 4.0 (Crossref license record, checked 2026-11-22; not printed in the PDF)",
    source_read="PDF", flags="Value type not stated in paper; aqueous Cu(I/II) mediator")

add(doi="10.1021/acsaem.3c02067", year=2023, status="HOLD_SI_NEEDED",
    mediator="Cu(I)(dmby)2 TFMSI / Cu(II)(dmby)2Cl TFMSI in ethylisopropyl sulfone",
    dye="XY1b / MS5 co-sensitized", electrolyte_additives="NMBI and others (devices A to E)",
    counter_electrode="not extracted", mask_area_cm2="not extracted",
    voc_mV="", jsc_mA_cm2="", ff="", pce_pct=0.82,
    value_type="maximum across devices A to E (abstract)", spread="",
    light="1 sun AM1.5G 100 mW/cm2 (values in SI Table S1)", stability="not extracted",
    locator="Abstract; SI Table S1 not available", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="Main text is indoor 1000 lx; 1-sun parameters only in the SI; excluded until the SI is read")

add(doi="10.3390/inorganics6020053", year=2018, status="INCLUDED",
    mediator="Cu(oxabpy) 0.2 M Cu(I) / 0.04 M Cu(II); ligand 6,6'-bis(4-(S)-isopropyl-2-oxazolinyl)-2,2'-bipyridine",
    dye="Y123", electrolyte_additives="0.1 M LiTFSI; 0.6 M TBP",
    counter_electrode="not extracted", mask_area_cm2="not extracted",
    voc_mV=920, jsc_mA_cm2=9.75, ff="", pce_pct=6.2,
    value_type="unspecified", spread="not reported", light="AM1.5G 100 mW/cm2",
    stability="NOT REPORTED (web text)", locator="Abstract; Sec 1; Sec 2.3",
    license_on_page="CC BY 3.0 (page metadata)", source_read="web page text only; not yet checked against the PDF",
    flags="FF not stated in text; Table 2 not visible in the web text")

add(doi="10.3390/en16196913", year=2023, status="INCLUDED",
    mediator="[Cu(tmby)2]2+/1+ 0.20 M Cu(I) / 0.04 M Cu(II) in acetonitrile",
    dye="D35 (0.1 mM dye bath)", electrolyte_additives="0.1 M LiTFSI; 0.6 M TBP",
    counter_electrode="not extracted", mask_area_cm2="not extracted",
    voc_mV=1002, jsc_mA_cm2=10.22, ff=0.63, pce_pct=6.50,
    value_type="mean +/- (SD or SE and cell count not stated)", spread="Voc +/-3 mV; Jsc +/-0.25; FF +/-0.01; PCE +/-0.25",
    light="AM1.5G 100 mW/cm2", stability="not fully checked (web text truncated)",
    locator="Table 1; Sec 3.1", license_on_page="CC BY 3.0 (page metadata)", source_read="web page text only; not yet checked against the PDF",
    flags="Discussion gives Voc as 1000 mV; Table 1 value used; Table 1 re-read from full web text 2026-11-22 (values match); text says FF unchanged but Table 1 shows FF rising with dye concentration")

add(doi="10.1038/s41467-021-21945-3", year=2021, status="INCLUDED",
    mediator="[Cu(tmby)2]2+/+ (tmby = 4,4',6,6'-tetramethyl-2,2'-bipyridine); 0.2 M Cu(I) / 0.1 M Cu(II) TFSI salts",
    dye="MS5 + XY1b co-sensitized", electrolyte_additives="0.6 M N-methylbenzimidazole; 0.1 M LiTFSI",
    counter_electrode="not extracted", mask_area_cm2="not extracted",
    voc_mV=1050, jsc_mA_cm2=15.84, ff=0.813, pce_pct=13.5,
    value_type="single device quoted in text (champion or mean not stated)", spread="", light="AM1.5G 100 mW/cm2",
    stability="light soaking 1000 h, 45 C, open circuit; 93 % retention",
    locator="Results (co-sensitized cells); Fig 3b and 3d; Suppl Table 2",
    license_on_page="Open access; CC license NOT shown in page text (confirm on publisher page)", source_read="web page text only; not yet checked against the PDF",
    flags="Headline Voc 1.24 V refers to MS5 alone; values re-read from web text 2026-11-22 (Voc, Jsc, FF, PCE match); Table 1 for Jsc not visible; PCE histogram of 16 samples in Fig 3c")


add(doi="10.1039/c9dt01448a", year=2019, status="INCLUDED",
    mediator="E1/E2 homoleptic Cu(I)/Cu(II) with 2-n-butyl-1,10-phenanthroline; 0.085 M E1 / 0.0085 M E2 in acetonitrile",
    dye="D1 copper(I) heteroleptic dye (2,9-dimesityl-1,10-phenanthroline + 6,6'-dimethyl-2,2'-bipyridine-4,4'-dibenzoic acid anchor)",
    electrolyte_additives="0.1 M LiTFSI; 0.28 M 4-tert-butylpyridine (tBuPy)",
    counter_electrode="not extracted", mask_area_cm2="0.16 (4 x 4 mm2 opening)",
    voc_mV=622, jsc_mA_cm2=5.77, ff=0.701, pce_pct=2.51,
    value_type="single cell per entry (champion or mean not stated)", spread="not reported",
    light="AM1.5 100 mW/cm2", stability="NOT REPORTED (text search)",
    locator="Table 1, entry 8 (highest of seven Cu-mediator entries)", license_on_page="CC-BY 3.0 (PDF statement)",
    source_read="PDF", flags="Copper dye with copper mediator; N719 with iodide control (6.87 %) is not Cu and not recorded")

add(doi="10.1021/acs.jpcc.5c03857", year=2025, status="INCLUDED",
    mediator="0.2 M [Cu(tmby)2]TFSI / 0.04 M [Cu(tmby)2](TFSI)2 in acetonitrile",
    dye="XY1b (0.1 mM) with 5 mM CDCA", electrolyte_additives="0.6 M TBP; plus 0.1 M of a salt not legible in the extracted text (confirm)",
    counter_electrode="PEDOT (electropolymerized EDOT; confirm)", mask_area_cm2="not found",
    voc_mV=1000, jsc_mA_cm2=7.35, ff=0.70, pce_pct=5.15,
    value_type="best cell tested 1 week after assembly", spread="not reported",
    light="AM1.5G 100 mW/cm2", stability="not extracted (cells measured 1 week after assembly)",
    locator="Table 2 (0.1 mM XY1b, 5 mM CDCA)", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="Dye-mixture and co-adsorbate study; XY1b:L1 mixtures best 4.97 %; L1 alone best 2.74 %")

add(doi="10.1016/j.carbon.2026.121407", year=2026, status="INCLUDED",
    mediator="CuI(dmp)2TFSI 0.2 M / CuII(dmp)2(TFSI)2 0.04 M in acetonitrile, quasi-solid gel",
    dye="Y123", electrolyte_additives="0.1 M LiTFSI; 0.6 M 4TBP; 0.5 wt% Ti3C2 MXene; 9 wt% PEO + 1 wt% PVDF-HFP gel (CLEMPP)",
    counter_electrode="not extracted", mask_area_cm2="not extracted",
    voc_mV=990, jsc_mA_cm2=9.64, ff=0.59, pce_pct=5.63,
    value_type="mean +/- SD (6 cells)", spread="Voc +/-0.01 V; Jsc +/-1.06; FF +/-0.04; PCE +/-0.58; abstract champion PCE 6.21 % at 100 mW/cm2",
    light="1 sun AM1.5G", stability="not extracted",
    locator="Table 2 (CLEMPP)", license_on_page="CC BY (PDF statement)",
    source_read="PDF", flags="Quasi-solid gel electrolyte, not liquid; same group as 10.1016/j.jpowsour.2025.237019")

add(doi="10.1021/acs.inorgchem.4c01046", year=2024, status="HOLD_SI_NEEDED",
    mediator="[Cu(PY5)]OTf 0.10 M / [Cu(PY5)]OTf2 0.05 M in acetonitrile (PY5 pentadentate ligand)",
    dye="Y123", electrolyte_additives="0.1 M LiOTf; TBP at 0, 0.055 or 0.526 M",
    counter_electrode="not extracted", mask_area_cm2=0.07,
    voc_mV="", jsc_mA_cm2="", ff="", pce_pct="",
    value_type="best devices per TBP condition (Figure 4a); full results in SI", spread="",
    light="AM1.5 100 mW/cm2", stability="not extracted",
    locator="Figure 4a; SI table not available", license_on_page="CC-BY 4.0 (PDF statement)",
    source_read="PDF", flags="Text says Jsc is around 9 mA/cm2 for all devices; Voc, FF and PCE are not stated in the text; needs the SI")

add(doi="10.3390/en14020407", year=2021, status="INCLUDED",
    mediator="[Cu(tmby)2](TFSI)1/2; 0.2 M Cu(I) / 0.04 M Cu(II) in acetonitrile",
    dye="Y123", electrolyte_additives="0.1 M LiTFSI; 0.6 M TBP",
    counter_electrode="PEDOT", mask_area_cm2="not extracted",
    voc_mV=1060, jsc_mA_cm2=7.47, ff=0.60, pce_pct=4.7,
    value_type="mean +/- SD (at least 3 devices)", spread="Voc +/-0.01 V; Jsc +/-0.06; FF +/-0.01; PCE +/-0.2",
    light="AM1.5G 100 mW/cm2", stability="30 min continuous irradiation; ratios in Table 2 (not extracted)",
    locator="Table 1 (before irradiation)", license_on_page="CC BY (PDF statement)",
    source_read="PDF", flags="Thin 2-3 um TiO2 without scattering layer for transient absorption, so not an optimized device; Co(bpy)3 cells not recorded")


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def qa(rows):
    lines = ["QA REPORT (generated by code/02_build.py)", ""]
    lines.append(f"Records: {len(rows)}")
    by = {}
    for r in rows:
        by[r["status"]] = by.get(r["status"], 0) + 1
    lines.append("By status: " + "; ".join(f"{k}={v}" for k, v in sorted(by.items())))
    lines.append("")
    lines.append("Consistency check: reported PCE vs Voc x Jsc x FF / 100 (flag if more than 10 % apart)")
    for r in rows:
        v, j, f, p = (num(r["voc_mV"]), num(r["jsc_mA_cm2"]), num(r["ff"]), num(r["pce_pct"]))
        if None in (v, j, f, p):
            lines.append(f"  {r['doi']}: skipped (a value is missing)")
            continue
        implied = v / 1000.0 * j * f * 100.0 / 100.0
        dev = abs(implied - p) / p * 100.0
        flag = "FLAG" if dev > 10 else "ok"
        lines.append(f"  {r['doi']}: reported {p:g} %, implied {implied:.3g} %, difference {dev:.1f} % [{flag}]")
    lines.append("")
    lines.append("Range checks (Voc 200 to 1300 mV; Jsc 0 to 25 mA/cm2; FF 0 to 1; PCE 0 to 15 %)")
    for r in rows:
        problems = []
        v, j, f, p = (num(r["voc_mV"]), num(r["jsc_mA_cm2"]), num(r["ff"]), num(r["pce_pct"]))
        if v is not None and not 200 <= v <= 1300:
            problems.append("Voc")
        if j is not None and not 0 <= j <= 25:
            problems.append("Jsc")
        if f is not None and not 0 <= f <= 1:
            problems.append("FF")
        if p is not None and not 0 <= p <= 15:
            problems.append("PCE")
        if problems:
            lines.append(f"  {r['doi']}: out of range: {', '.join(problems)}")
    lines.append("  (no other range problems)")
    lines.append("")
    lines.append("Review first (extremes among included records)")
    d = [r for r in rows if r["status"] == "INCLUDED" and num(r["pce_pct"]) is not None]
    d.sort(key=lambda r: num(r["pce_pct"]))
    lines.append(f"  lowest PCE: {d[0]['doi']} ({d[0]['pce_pct']} %)")
    lines.append(f"  highest PCE: {d[-1]['doi']} ({d[-1]['pce_pct']} %)")
    lines.append("")
    lines.append("Missing values (left empty, never computed)")
    for r in rows:
        miss = [c for c in ("voc_mV", "jsc_mA_cm2", "ff", "pce_pct") if r[c] == ""]
        if miss:
            lines.append(f"  {r['doi']}: {', '.join(miss)}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "records_v1.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(R)
    with open(os.path.join(OUT, "qa_report.txt"), "w", encoding="utf-8") as fh:
        fh.write(qa(R))
    print(open(os.path.join(OUT, "qa_report.txt"), encoding="utf-8").read())
