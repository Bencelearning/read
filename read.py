data = []
count = 0
with open('reviews.txt', 'r') as f: #以讀取模式開啟檔案 reviews.txt 並將開啟的檔案於程式碼中命名為f
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) #透過 count 了解資料寫入 data 的進度
print('讀取完成, 共計', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均字元長度為', sum_len / len(data)) #計算所有留言的平均字元長度

hundred = []
for d in data:
	if len(d) < 100:
		hundred.append(d)
print('一共有', len(hundred), '筆資料字元少於100') #篩選字元少於100的留言筆數

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料提到good') #篩選留言提到 good 的筆數

bad = [1 for d in data if 'bad' in d] # 清單 data 中每筆留言提到 bad 就將 1 存入清單 bad
print('一共有',len(bad), '筆資料提到bad')
