# READ ME

### 將檔案搬離暫存/倉庫區

- git rm --cached filename

### 檢視目前分支

- git branch

### 新增分支

- git branch <branch-name>

### 切換分支

- git checkout <branch-name>

### 切換+新增分支(二合一)

- git checkout -b <branch-name>

### 更改分支名稱

- git branch -m <old-branch-name> <new-branch-name>

### 刪除分支

- git branch -D <branch-name>

### 合併分支 (自已不能合併自已)

( - git checkout <another-branch-name>

- git merge <branch-name>

### 衝突處理

- 確認修改狀態

### 切換 commit

- git checkout <commit-object (七位英數字 d157a68)>

###

- git commit -a (進入 vim)

### 列出當下 commit 歷程

- git reglog

### 恢復 commit 指令

- git reset -mixed (預設不用打) <commit-object (七位英數字 d157a68)>
- git reset --soft <commit-object (七位英數字 d157a68)>
- git reset --hard <commit-object (七位英數字 d157a68)>

### 恢復雲端 git url

- git remote add origin <https://github.com/christyfeifei/git-demo2>

### 推送指令

- git push -u origin <master> (第一次建立分支) - git push (第二次之後的同步檔案)
