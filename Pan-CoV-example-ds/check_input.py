import os
import glob
import pandas
import sys
import copy

# single argument in the sample metadata
df = pandas.read_csv(sys.argv[1])
#ret = copy.deepcopy(df)

for idx, row in df.iterrows():
    print("########################################")
    exp = row["seq_dir"]
    fqp = row["fastq_filename"]
    print(fqp)
    matches = glob.glob(os.path.join(exp, fqp))
    print(f"ID: {idx}")
    print(f"exp: {exp}\n")
    print(f"matches: {matches}")
    assert len(matches) == 1
    #ret.loc[idx, "fastq_filename"] = os.path.basename(matches[0])
    print("########################################\n\n")
#ret.to_csv("child_samples_filenames.csv", index=False, na_rep="NA")
