n = 3
password = 'a123'
while n > 0 : 
	n = n-1
	p = input('請輸入密碼')
	p = str(p)
	if p == password :
		print('登入成功')
		break
	else :
		if n > 0 :
			print('密碼錯誤!還有', n ,'次機會')
		elif n == 0 :
			print('帳號已鎖定')

	

	



