import pandas as pd
import numpy as np

np.random.seed(4)
st = pd.read_csv("sample_table.csv", index_col=0)
#st = st[st["seq_dir"] == "NGS/20-09-02-cov2-ex12/"]
st = st
sams = []

for exp, exp_st in st.groupby("seq_dir"):
    print("\n\n", exp, "##############\n\n")
    for ps, ps_st in st.groupby("patient_status"):
        participants = list(set(ps_st["participant_ID"]))
        print(ps, len(participants), participants)
        
#import sys
#sys.exit()

# choose library controls
for ba, ba_st in st.groupby("library_batch"):
    if ba not in ["MEGSUB", "SUB2"]: continue
    lib_s = ba_st[ba_st["control_status"]=="library"].index.values
    sams.append(np.random.choice(lib_s))

# choose empirical samples
for ps, ps_st in st.groupby("patient_status"):
    if ps not in ["conv outpatient 30d", "healthy adult"]: continue
    participants = list(set(ps_st["participant_ID"]))
    choice = np.random.choice(participants)
    part_st = ps_st[ps_st["participant_ID"]==choice]
    print(f"part choice for {ps} is {choice}")
    for ba, ba_st in part_st.groupby("library_batch"):
        sams.append(np.random.choice(ba_st.index.values))

sams_st = st.loc[sams, :]
sams_st.to_csv("sample_table_subset.csv", index=True, na_rep="NA")
print(sams_st)
#print(sams_st["reads mapped:"])
print("                  ", sams)
