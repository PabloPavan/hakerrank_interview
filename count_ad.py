count_ad(base10):
  binario = list(bin(base10))[2:]

  inverte = ''
  for letra in binario:
    if letra == '1':
      inverte += '0'
    else:
      inverte += '1'

  return (int(inverte, 2))
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    base10 = int(input().strip())

    result = count_ad(base10)

    fptr.write(str(result) + '\n')

    fptr.close()
