from csv import reader
from collections import defaultdict
from itertools import combinations, chain
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import pyfpgrowth
import time


dataset_choice = input("choose dataset ( amazon, bestbuy, kmart, nike, generic): ")
# User input for minimum support and confidence
support = float(input("Enter minimum support: "))
confidence = float(input("Enter minimum confidence: "))
# Reading the file and initializing sets
with open(dataset_choice + "_transactions.csv", 'r') as file:
    csv_reader = reader(file)
    item_set = set()
    item_sets = []
    for line in csv_reader:
        cleaned_line = [value for value in line if value]
        record_set = set(cleaned_line)
        for item in record_set:
            item_set.add(frozenset([item]))
        item_sets.append(record_set)

start_time_brute_force = time.time()

# Initializing variables for the main algorithm
global_freq_item_set = dict()
global_item_set_with_sup = defaultdict(int)

# getting items above minimum support
freq_item_set = set()
local_item_set_with_sup = defaultdict(int)

for item in item_set:
    for item_set in item_sets:
        if item.issubset(item_set):
            global_item_set_with_sup[item] += 1
            local_item_set_with_sup[item] += 1

for item, sup_count in local_item_set_with_sup.items():
    support_value = float(sup_count / len(item_sets))
    if support_value >= support:
        freq_item_set.add(item)

L1_item_set = freq_item_set
current_lset = L1_item_set
k = 2

while current_lset:
    global_freq_item_set[k - 1] = current_lset
    # Self-joining Lk
    candidate_set = set([i.union(j) for i in current_lset for j in current_lset if len(i.union(j)) == k])

    # Pruning
    temp_candidate_set = candidate_set.copy()
    for item in candidate_set:
        subsets = combinations(item, k - 1)
        for subset in subsets:
            if frozenset(subset) not in current_lset:
                temp_candidate_set.remove(item)
                break
    candidate_set = temp_candidate_set

    # Counting support again
    current_lset = set()
    local_item_set_with_sup = defaultdict(int)
    for item in candidate_set:
        for item_set in item_sets:
            if item.issubset(item_set):
                global_item_set_with_sup[item] += 1
                local_item_set_with_sup[item] += 1

    for item, sup_count in local_item_set_with_sup.items():
        support_value = float(sup_count / len(item_sets))
        if support_value >= support:
            current_lset.add(item)
    k += 1

# Association rule generation inlined
rules = []
for k, item_set in global_freq_item_set.items():
    for item in item_set:
        subsets = chain.from_iterable(combinations(item, r) for r in range(1, len(item)))
        for s in subsets:
            confidence_value = float(global_item_set_with_sup[item] / global_item_set_with_sup[frozenset(s)])
            if confidence_value > confidence:
                rules.append([set(s), set(item.difference(s)), confidence_value])

rules.sort(key=lambda x: x[2])

end_time_brute_force = time.time()
print(f"Brute-Force Time: {end_time_brute_force - start_time_brute_force} seconds")
# Printing the results
print("Frequent item sets")
print(global_freq_item_set)

print("Associated Rules:")
for rule in rules:
    print(rule)

print("--Applying Apriori Algo from a python library--")
# Apriori Alogirm from mlxtend
# Preprocess data for mlxtend
start_time_apriori = time.time()
te = TransactionEncoder()
te_ary = te.fit(item_sets).transform(item_sets)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori
frequent_item_sets_apriori = apriori(df, min_support=support, use_colnames=True)

# Generate rules
rules_apriori = association_rules(frequent_item_sets_apriori, metric="confidence", min_threshold=confidence)
end_time_apriori = time.time()
print(f"Apriori Time: {end_time_apriori - start_time_apriori} seconds")

# Print Apriori generated rules
print("Apriori Rules")
print(rules_apriori[['antecedents', 'consequents', 'support', 'confidence']])


print("--Applying FP-Growth Algorith--")
# FP growth algos
# Find frequent patterns
start_time_fpgrowth = time.time()
patterns = pyfpgrowth.find_frequent_patterns(item_sets, support_threshold=int(support * len(item_sets)))

# Generate association rules
rules_fpgrowth = pyfpgrowth.generate_association_rules(patterns, confidence)
end_time_fpgrowth = time.time()
print(f"FP-Growth Time: {end_time_fpgrowth - start_time_fpgrowth} seconds")

# Print FP-Growth generated rules
print("FP-Growth Rules")
for rule, metrics in rules_fpgrowth.items():
    print(f"Antecedent: {rule}, Consequent: {metrics[0]}, Confidence: {metrics[1]}")
