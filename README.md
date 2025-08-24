
# Git & GitHub Complete Guide (VS Code / CMD)

Ye guide aapko Git aur GitHub ka **complete step-by-step process** samjhaata hai jaise aap VS Code ya CMD me kaam kar rahe ho.

---

## Step 1: GitHub Account Aur Repository Banaye

1. GitHub par login karo.  
2. “New Repository” create karo:  
   - Name: `MyProject` (ya jo bhi chaho)  
   - Public/Private: apne hisaab se choose karo  
   - Initialize with README ✅  

💡 Analogy: “Notebook create kar liya, jisme aap homework rakhenge.”

---

## Step 2: Git Install Aur Setup

1. Git install karo: [https://git-scm.com/](https://git-scm.com/)  
2. VS Code terminal / CMD khol ke check karo:
```bash
git --version
````

3. Apna naam aur email configure karo:

```bash
git config --global user.name "Haroon"
git config --global user.email "haroon@example.com"
```

💡 Analogy: “Notebook me apna naam aur ID likh di.”

---

## Step 3: Repository Clone Karna

```bash
git clone https://github.com/username/MyProject.git
cd MyProject
```

💡 Analogy: “Notebook ka copy apne laptop par la liya.”

---

## Step 4: Nayi Branch Banao Aur Switch Karo

```bash
git branch feature-login   # Nayi branch banai
git checkout feature-login # Us branch par switch kiya
```

💡 Analogy: “Extra page banaya notebook me aur uspe kaam shuru kiya.”

---

## Step 5: Changes Karo Aur Commit Karo

* Apna text/file edit karo ya naya file add karo.

```bash
git add .
git commit -m "Added login feature"
```

💡 Analogy: “Homework ready ho gaya, sticky note lagaya ke ready hai.”

---

## Step 6: Branch GitHub Par Push Karo

```bash
git push origin feature-login
```

💡 Analogy: “Page teacher ko online dikhaya.”

---

## Step 7: Pull Request (PR) Banana

1. GitHub website par repository open karo.
2. “Compare & Pull Request” par click karo.
3. Message likho: “Added login feature”
4. Submit PR

💡 Analogy: “Teacher se poochha: ‘Mera homework theek hai, main notebook me add kar doon?’”

---

## Step 8: PR Review Aur Merge

* Team ya teacher review karenge.
* Agar approve ho gaya, to **Merge PR** button click karo.

💡 Analogy: “Teacher ne homework check karke main notebook me paste kar diya.”

---

## Step 9: Branch Delete (Optional)

```bash
git branch -d feature-login
```

💡 Analogy: “Extra page hata diya, kyunki kaam main notebook me aa gaya.”

---

## Step 10: Full Flow Summary

1. Repository clone karo
2. Nayi branch banao
3. Code changes karo
4. Changes stage aur commit karo
5. Branch GitHub par push karo
6. Pull Request create karo
7. PR review aur merge
8. Branch delete karo (optional)

💡 Next Step: Naye features add karne ke liye step 4 se repeat karo.

---

## Step 11: Example Merge Notification

```
Merge pull request #1 from itxHaroonKhan/feature-login
```

* Ye batata hai ki `feature-login` branch ka code **main branch me merge** ho gaya.
* `#1` = pull request number
* `itxHaroonKhan/feature-login` = username aur branch ka naam

💡 Analogy: “Teacher ne homework approve karke main notebook me paste kar diya.”

```

---

✅ **Kaise use kare:**  

1. VS Code me naya file create karo.  
2. Naam rakho: `README.md`  
3. Upar wala content paste karo.  
4. Save karo.  
5. VS Code me Markdown preview (`Ctrl+Shift+V`) se guide dekh sakte ho.  

---

# Git & GitHub Guide: Branches, PR, PR Review

Ye guide aapko **Branches, Pull Requests (PR), aur PR Review** ke concepts aur commands step by step samjhaata hai.

---

## Branches

Branches Git ka feature hai jisme aap **main project se alag ek copy** bana ke kaam karte ho.

### Commands:
```bash
git branch                    # Sab branches list karo
git branch feature-login      # Nayi branch banai
git checkout feature-login    # Us branch par switch kiya
git checkout -b feature-login # Branch banate hi us par switch kar do
git branch -d feature-login   # Branch delete karo (optional)
````

💡 Analogy: “Notebook me extra page banaya aur uspe naya kaam shuru kiya.”

---

## Pull Request (PR)

Pull Request (PR) ek request hai jo aap **apni branch ka code main branch me merge karne ke liye** bhejte ho.

### Steps:

1. GitHub par repository open karo.
2. “Compare & Pull Request” par click karo.
3. PR message likho jaise: `"Added login feature"`
4. Submit PR

### Commands (local se push karna):

```bash
git add .
git commit -m "Added login feature"
git push origin feature-login
```

💡 Analogy: “Teacher se poochha: ‘Mera homework theek hai, main notebook me add kar doon?’”

---

## PR Review

PR Review me team ya reviewer aapke code ko **check karte hai**.

* Agar sab sahi ho, approve karte hai.
* Fir merge kar sakte ho main branch me.

### Example Merge Command (local se update lene ke liye):

```bash
git checkout main
git pull origin main
```

### Example GitHub Merge Notification:

```
Merge pull request #1 from itxHaroonKhan/feature-login
```

* `#1` = Pull Request number
* `itxHaroonKhan/feature-login` = username aur branch ka naam

💡 Analogy: “Teacher ne homework check karke main notebook me paste kar diya.”

```

---

✅ **Kaise use kare:**

1. VS Code me naya file create karo.  
2. Naam rakho: `README.md`  
3. Upar wala content paste karo.  
4. Save karo.  
5. VS Code me Markdown preview (`Ctrl+Shift+V`) se steps aur commands easily dekh sakte ho.

---

Agar chaho, mai **ye complete Git + GitHub workflow (Branches, PR, PR Review + full commands + examples)** ek **full README ready-to-use version** bhi bana doon, jisme sab commands aur steps ek saath ho, jisse aap class me dikha sako aur practice bhi kar sako.  

Chahte ho mai wo bana doon?
```

