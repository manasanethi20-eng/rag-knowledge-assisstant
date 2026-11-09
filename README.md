# Project 1: RAG Knowledge Assistant

## 1. Company & Problem
Company: Arrowstack Foods Pvt Ltd
Problem: New employees and HR team have many questions about company policies like leave, work from home, salary. They waste time searching in many PDF files.

Solution: A RAG Knowledge Assistant. User asks a question in simple English, assistant searches only in company policy documents and gives answer with citation.

## 2. Target User / Stakeholder
Primary User: New Employees and HR Team
Decision Enabled: Employee can quickly know leave rules, WFH rules without asking HR.

## 3. Inputs and Outputs
Input: User question in English. Example: "How many sick leaves do I have?"
Output: Short answer + Source citation. Example: "You have 12 sick leaves per year. Source: Leave Policy, Page 1"

## 4. Scope
In Scope:
- Only 5 company policy documents
- Only English questions
- Answer only from documents, no outside knowledge

Out of Scope:
- No salary calculation for a specific person
- No legal advice

## 5. Success Metrics
- Answer should be correct for 8 out of 10 test questions
- Every answer must have a citation
- If answer is not in documents, assistant must say "Not found in policy documents"

## 6. Safety Controls
- No hallucination: Do not guess answer
- No personal data: No employee names, phone numbers in documents
- If question is unclear, ask for clarification

## 7. How to Run
1. Install Python 3.12 from Microsoft Store
2. Open this folder in VS Code
3. In Terminal, run:
python app.py

## 8. Testing Results
| Question | Source | Result |
| How many sick leaves do I have? | leave_policy.txt | PASS |
| Can I work from home? | wfh_policy.txt | PASS |
| When is salary credited? | salary_policy.txt | PASS |
| When is salry credited? (spelling mistake) | - | PASS - Safe failure, said Not found |

## 9. Known Limitation
Sometimes it returns title line instead of detail line, because it counts matching words. Example: Salary question returned title line. This is Version 1 limitation.