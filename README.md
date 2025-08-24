# Git & GitHub Complete Guide

Ye guide aapko Git aur GitHub ka complete step-by-step process samjhaati hai jaise aap apni laptop par VS Code me kaam kar rahe ho.

1. GitHub par login karo aur “New Repository” create karo. Name: MyProject (ya jo bhi chaho), Public/Private choose karo, Initialize with README ✅. Ye aapki notebook create karne ke barabar hai jisme aap homework rakhenge.

2. Git install karo: https://git-scm.com/ . CMD/Terminal me check karo git --version. Apna naam aur email configure karo: git config --global user.name "Haroon" aur git config --global user.email "haroon@example.com". Ye notebook me apna naam aur ID likhne ke barabar hai.

3. Repository clone karo: git clone https://github.com/username/MyProject.git aur cd MyProject. Ye notebook ka copy apne laptop par laane ke barabar hai.

4. Nayi branch banao aur switch karo: git branch feature-login aur git checkout feature-login. Ye extra page banane ke barabar hai aur uspe kaam shuru karna.

5. Apna text ya code file edit karo ya naya file add karo. Changes stage karo: git add . aur commit karo: git commit -m "Added login feature". Ye homework ready karne aur sticky note lagane ke barabar hai.

6. Branch GitHub par push karo: git push origin feature-login. Ye page teacher ko online dikhane ke barabar hai.

7. Pull Request (PR) GitHub website par banao: repository open karo, “Compare & Pull Request” par click karo, message likho “Added login feature”, submit PR. Ye teacher se poochhne ke barabar hai: “Mera homework theek hai, main notebook me add kar doon?”

8. PR review aur merge: Team ya teacher check karenge. Agar approve ho gaya, to Merge PR button click karo. Ye teacher ne homework check karke main notebook me paste karne ke barabar hai.

9. Branch delete (optional): git branch -d feature-login. Ye extra page hata dene ke barabar hai kyunki kaam main notebook me aa gaya.

10. Full flow summary: Repository clone karo → Nayi branch banao → Code changes karo → Changes stage aur commit karo → Branch GitHub par push karo → Pull Request create karo → PR review aur merge → Branch delete (optional). Naye features add karne ke liye step 4 se repeat karo.

11. Example merge notification: Merge pull request #1 from itxHaroonKhan/feature-login. Ye batata hai ki feature-login branch ka code main branch me merge ho gaya. #1 = pull request number, itxHaroonKhan/feature-login = username aur branch ka naam. Ye teacher ne homework approve karke main notebook me paste karne ke barabar hai.
