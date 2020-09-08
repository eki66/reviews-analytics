data = [] #建立一個名為data的空清單
count = 0 #建立一個count變數並放入0, 用來計數
with open ('reviews.txt', 'r') as f:  # 讀取名為reviews.txt的留言文字檔當作f
	for line in f: # 將f中每次讀取一筆留言命名為line 的 for 迴圈 (for loop的意思就是把清單中的東西一個一個拿出來)
		data.append(line) # 把讀取後的line append加入到data的空清單內
		count += 1 # count = count + 1 的累加的快寫法
		if count % 10000 == 0: # 如果count計數和10000的餘數是0時, 意即count計數為10000的倍數時(%是用來求餘數)
			print(len(data)) # 印出data清單的長度(即總留言筆數)
print('檔案讀取完了, 總共有', len(data), '筆資料')


sum_len = 0 # 建立一個初始為0, 名為sum_len 加總所有留言的(幾個字母)長度的變數
for d in data: # 將data清單中的每一筆資料命名為d 的 for 迴圈 (for loop的意思就是把清單中的東西一個一個拿出來)
	sum_len = sum_len + len(d) # 每一筆留言的長度len(d), 快寫為 sum_len += len(d), 累加所有留言的長度
print('留言平均長度是', sum_len / len(data)) # 印出留言平均長度 = 總留言長度 / 總留言筆數


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('字母數量小於100的共有', len(new), '筆留言資料')


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])