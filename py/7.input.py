가격 = input('가격?')
가격 = float(가격)
부가가치세율 = 0.1
부가가치세 = 가격 * 0.1
열린파일 = open('result.txt', 'a')
열린파일.write(str(부가가치세)+'\n')
열린파일.close()