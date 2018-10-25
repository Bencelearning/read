data = []
count = 0
with open('reviews.txt', 'r') as f: #以讀取模式開啟檔案 review.txt 並將開啟的檔案於程式碼中命名為f
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) #透過 count 了解資料寫入 data 的進度