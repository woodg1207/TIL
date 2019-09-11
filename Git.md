# Git

- git 브랜치는 매우 가볍다.
- 순식간에 브랜치를 만들고 브랜치 사이를 이동 할 수 있다. 
- git 이 갖고온 혁신 중 하나는 브랜치 기능을 매우 쓸만한 수준까지 만들었다는 것. 

```bash
touch file 파일 생성

git branch : 브랜치 탐색
$ git branch
* master


git branch branch_name
git checkout branch_name
--> git checkout -b branch_name  : 만들면서 브랜치로 이동


마스터에서 
git branch -d branch_name :: 삭제
git branch -D branch_name  

git merge branch_name  : 병합
```



### **fast - fowartd 상황**

- branch가 최신이 되는 상황  
- 가장 평범한 상황 

```bash
git checkout -b feature/test
$ (feature/test)
```

작업완료후 commit

```bash
touch test.md
git add .
git commit -m "complete test.md"
```

master이동

```bash
git checkout master
$ (master)
```

master에서 병합

```bash
git merge feature/test
```

- 결과

단순히 HEAD가 최신 COMMIT으로 이동

feature/test branch 생성 이후 master branch 의 이력에 변화가 없었기 때문에

branch 삭제

```bash
git branch -d feature/test
```



###  **merge-commit 상황**

- 3-way-merge

1. feature/login branch 이동

```bash
git checkout -b feature/login
```

2. 작업 완료후 commit

```bash
touch login.md
git add .
git commit -m "complete login.md"
```

3. master로 이동

```bash
git checkout master
```

4. master에 추가  commit 생성

```bash
touch master.md
git add .
git commit -m "fix master.md"
```

5. master에 병합

```bash
git merge feature/login
```

6. 자동으로 merge commit 발생

```bash
Merge branch 'feature/login'
```

- vim 에디터로 열림
- 메세지를 수정하고자 하면 `i`로 편집 모드로 바꾼다음에 commit을 수정하고
- `esc`+`:wq`를 통해 저장및 종료

7. commit 그래프 확인하기 

```bash
$ git log --oneline --graph
*   1330df2 (HEAD -> master) Merge branch 'feature/signout'
|\
| * 8862688 (feature/signout) complete login.txt
| * eff9621 complete signout.txt
* | b9a6639 Make master.txt
|/
* d3a4904 test.txt
* a0eca0e c
```

8.branch 삭제

```bash
git barnch -d feature/login
```

###  **merge-conflict**

최악의 상황 -- 사람이 직접 수정을 해줘야한다. 

수정 후 git commit만 치면 된다. 

1. feature/article branch 생성 및 이동

```bash
git checkout -b feature/article
```

2. 작업 완료후 commit

```bash
#충돌을 만들어 낼 파일에 코드를 작성
git add .
git commit -m "fix minor update"
```

3. master로 이동

```bash
git checkout master
```

4. master에 추가 commit 만드릭

```bash
#feature/article branch 에서 수정한 파일과 동일 파일의 같은 위치를 수정
git add .
git commit -m "fixed master update"
```

5. master에 병합

```bash
git merge feature/article
```

6. merge confict발생

```bash
git merge feature/article

error
Auto-mergin a.txt
CONFLICT ...	
```

7. 충돌 확인 및 해결

```bash
#충돌이 일어난 파일 열기
<<<<HEAD
master 에서 작성한 내용
==========
feature/article에서 작성한 내용
>>>>>feature/article
```

8.merge commit 진행

```bash
git add .
git commit
```

9. log 확인

```bash
$ git log --oneline --graph
*   560d5f0 (HEAD -> master) Merge branch 'feature/article'
|\
| * b8da78c (feature/article) fix a.txt
* | e7d3121 fix a.txt in master
|/
*   1330df2 Merge branch 'feature/signout'
|\
| * 8862688 complete login.txt
| * eff9621 complete signout.txt
* | b9a6639 Make master.txt
|/
* d3a4904 test.txt
* a0eca0e c

```

10. branch 삭제

```bash
git branch -d feature/article
```



### feature branch workflow(소규모)

**Pull request**

- 기능개발을 끝내고 master에 바로 병합 시키는게 아니라, 브랜치를 중앙 원격저장소에 올리고(push) master에 병합을 요청(merge)

-- 주의 사항 

중앙에서 병합을 했다면, 다른 팀원들은 master 브랜치를 pull받아야한다.

### forking workflow

master를 fork함(github내에서 한다.)  --> fork한 master를 clone 

--> git remote add upstream[master의 주소] --> git checkout - b feature/login --수정--> git push -u origin feature/login