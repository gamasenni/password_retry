n = 3
while True : 
	p = input('請輸入密碼')
	p = str(p)
	if p == 'a123' :
		print('登入成功')
		break
	elif p != 'a123' :
		print('密碼錯誤')
		n = n-1
		print('還有', n ,'次機會')
		if n == 0 :
			print('帳號已鎖定')
			break

	

	



