from collections import defaultdict
from pandas import Series, DataFrame
import itertools as it
import pandas as pd
import math
import csv
import sys
import argparse
import collections
import glob
import os
import re
import requests
import string
import sys

class Armin():
    
    def apriori(self, input_filename, output_filename, min_support_percentage, min_confidence):
        transactions = [] 
        try:
            with open('input filename, 'r') as f: 
                reader = csv.reader(f) 
                for row in reader: 
                    if not row: 
                        continue
                items = [x.strip() for x  in row[1:] if x.strip()]
                if items: 
                transactions.append(set(items))
         except FileNotFoundError:
            print(f"Error: {input_filename} not found.")
            return

        total_transactions = len(transactions)
        if total_transactions == 0: 
            return
        frequent_items = {}

        items_count = defaultdict(int)
        for transaction in transactions: 
            for item in transaction: 
                item_counts[([item])] += 1
        frequent_current = {} 

        for itemset, count in item_count.items(): 
            support = count / total_transactions 
            if support >= min_support_percentage: 
               frequent_current[tuple(sorted(itemset))] = support
        frequent_items.update(frequent_items)

        k=2
        while frequent_current: 
             candidate = set()
             previous_items = list(frequent_current.keys())
       
            for i in range(len(previous_items)):
                for j in range(i + 1, len(previous_items)):
                    union = tuple(sorted(set(prev_itemsets[i]) |
                                         set(prev_itemsets[j])))
                    if len(union) == k:
                        candidates.add(union)
            next_items = {}

            for candidates in candidates: 
                subsets = list(it.combinations(cand, k - 1))
                valid = True
                for s in subsets:
                    if tuple(sorted(s)) not in current_l:
                        valid = False
                        break
                if not valid: 
                    continue 

                candidate_set = set(candidate)
                count = 0 
                for t in transactions: 
                    if candidate_set.issubset(t): 
                        count += 1
                support = count / total_transactions
               
                if support >= min_support_percentage: 
                    next_items[candidates] = support 
         
            if not next_items: 
                break 

            frequent_items.update(next_items)
            current_items = next_items
            k += 1

        rules = [] 
        for items, support in frequent_items.items(): 
            if len(items) < 2: 
                continue 
            for i in range(1, len(items)): 
                 for lhs_tuple in it.combinations(itemset, i):

                    lhs = tuple(sorted(lhs_tuple))
                    rhs = tuple(sorted(set(itemset) - set(lhs)))

                    lhs_support = frequent_items.get(lhs)

                    if lhs_support is None: 
                        continue 

                    confidence = support / lhs_support 

                    if confidence >= min_confidence 
                        rules.append((support, confidence, lhs, rhs))

        with open(output_filename, 'w', newline='') as f: 
            writer = csv.writer(f)
            items_list = list(frequent_items.items())
            items_list.sort(key=len)
            items_list = sort()

            for itemset, support in itemset_list:
                row = ["S", "{:.4f}".format(support)]
                for item in itemset:
                    row.append(item)
                writer.writerow(row)


            rules.sort()
            for support, confidence, lhs, rhs in rules 
                row = ["R",
                       "{:.4f}".format(support),
                       "{:.4f}".format(confidence)]
               
                for item in lhs: 
                    row.append(item)

                row.append("=>")

                for item in rhs: 
                    row.append(item)

                writer.writerow(row)


    
        pass

if __name__ == "__main__":
    armin = Armin()
    armin.apriori('input.csv', 'output.sup=0.5,conf=0.7.csv', 0.5, 0.7)
    armin.apriori('input.csv', 'output.sup=0.5,conf=0.8.csv', 0.5, 0.8)

    armin.apriori('input.csv', 'output.sup=0.6,conf=0.8.csv', 0.6, 0.8)
