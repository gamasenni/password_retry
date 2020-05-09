n = 3
password = 'a123'
while True : 
	p = input('請輸入密碼')
	p = str(p)
	if p == password :
		print('登入成功')
		break
	else :
		n = n-1
		print('密碼錯誤!還有', n ,'次機會')
		if n == 0 :
			print('帳號已鎖定')
			break

	

	



