import sys
from search import search
import json
from termcolor import colored
from time import time

if len(sys.argv) != 2:
    print("Usage: python main.py <path_to_data_json>")
    sys.exit(1)

data_json_path = sys.argv[1]

testcases = json.loads(open(data_json_path, encoding="UTF8").read())
print(len(testcases))
corrects = 0
wrongs = 0
wrong = []
cnt = 0

overal_time = 0

for testcase in testcases:
    cnt += 1
    # if cnt > 500:
    #     break
    print("-------------------------------------------")
    print("searching in doc number ", testcase["document_id"])
    start = time()
    ans = search(testcase["query"], testcase["candidate_documents_id"])
    end = time()
    overal_time += (end - start) * 1000

    check = []
    for i in range(5):
        check.append(ans[i][0])

    if int(testcase["document_id"]) in check:
        corrects += 1
        print(colored("PASSED", 'green'))
    else:
        wrongs += 1
        wrong.append((testcase["document_id"], testcase["query"], int(ans[0][0])))
        print(colored("WRONG", 'red'))
    print("-------------------------------------------")

print("the accuracy is: ", corrects / (corrects + wrongs) * 100)
print(f"overall time consumed for {corrects + wrongs} docs: ", overal_time)
