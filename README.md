git_github_guide:
  title: "Git & GitHub Step by Step (VS Code / CMD)"
  description: "Ye guide aapko Git aur GitHub ka complete process step by step samjhaata hai jaise aap VS Code me kaam kar rahe ho."
  steps:
    - step: 1
      title: "GitHub Account Aur Repository Banaye"
      actions:
        - "GitHub par login karo"
        - "New Repository create karo"
        - "Name: MyProject (ya jo bhi chaho)"
        - "Public/Private choose karo"
        - "Initialize with README ✅"
      analogy: "Notebook create kar liya, jisme aap homework rakhenge"

    - step: 2
      title: "Git Install Aur Setup"
      actions:
        - "Git install karo: https://git-scm.com/"
        - "CMD / VS Code terminal me check karo: git --version"
        - "Apna naam configure karo: git config --global user.name 'Haroon'"
        - "Apna email configure karo: git config --global user.email 'haroon@example.com'"
      analogy: "Notebook me apna naam aur ID likh di"

    - step: 3
      title: "Repository Clone Karna"
      commands:
        - "git clone https://github.com/username/MyProject.git"
        - "cd MyProject"
      analogy: "Notebook ka copy apne laptop par la liya"

    - step: 4
      title: "Nayi Branch Banao Aur Switch Karo"
      commands:
        - "git branch feature-login   # Nayi branch banai"
        - "git checkout feature-login # Us branch par switch kiya"
      analogy: "Extra page banaya notebook me aur uspe kaam shuru kiya"

    - step: 5
      title: "Changes Karo Aur Commit Karo"
      actions:
        - "Apna text/file edit karo ya naya file add karo"
      commands:
        - "git add ."
        - "git commit -m 'Added login feature'"
      analogy: "Homework ready ho gaya, sticky note lagaya ke ready hai"

    - step: 6
      title: "Branch GitHub Par Push Karo"
      commands:
        - "git push origin feature-login"
      analogy: "Page teacher ko online dikhaya"

    - step: 7
      title: "Pull Request (PR) Banana"
      actions:
        - "GitHub website par repository open karo"
        - "Compare & Pull Request par click karo"
        - "Message likho: 'Added login feature'"
        - "Submit PR"
      analogy: "Teacher se poochha: ‘Mera homework theek hai, main notebook me add kar doon?’"

    - step: 8
      title: "PR Review Aur Merge"
      actions:
        - "Team ya teacher review karenge"
        - "Agar approve ho gaya, Merge PR button click karo"
      analogy: "Teacher ne homework check karke main notebook me paste kar diya"

    - step: 9
      title: "Branch Delete (Optional)"
      commands:
        - "git branch -d feature-login"
      analogy: "Extra page hata diya, kyunki kaam main notebook me aa gaya"

  full_flow_summary:
    - "Repository clone karo"
    - "Nayi branch banao"
    - "Code changes karo"
    - "Changes stage aur commit karo"
    - "Branch GitHub par push karo"
    - "Pull Request create karo"
    - "PR review aur merge"
    - "Branch delete karo (optional)"
    - "Naye features add karne ke liye step 4 se repeat karo"

  example_merge_notification:
    text: "Merge pull request #1 from itxHaroonKhan/feature-login"
    explanation:
      - "#1 = pull request number"
      - "itxHaroonKhan/feature-login = username aur branch ka naam"
      - "Teacher ne homework approve karke main notebook me paste kar diya"
