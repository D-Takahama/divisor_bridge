def sieve_of_eratosthenes(x):#n以下の素数
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

#[0,0,0,0....,0,0](m=len(p)個),[0,0,0,0...,0,1]....[p1,p2,p3,p4,...,pm-1,pm]と羅列していく再帰関数
def prime_digit(d,pmodlist,p,limit):#d:上記のリストで左からd桁、d = 0,1,2,...,len(p)-1
  #print(d)
  #print(len(pmodlist))
  j = 0
  for i in range(limit):
    if pmodlist[i] != p[i]-1:
      j = 1
      break
  if j == 0:
    pmodlist = [0]*limit
    return pmodlist

  pmodlist[d] = (pmodlist[d]+1) % p[d]



  if pmodlist[d] == 0:
    prime_digit(d+1,pmodlist,p,limit)#再帰したときにpmodlistのindexがオーバーする。
  return pmodlist

def canlink(k,primes,remalign):
  for i in reversed(range(len(primes))):
    if remalign[i]+primes[i] >= k and remalign[i]-primes[i] < 0:
      return 0#公約数ブリッジ不可
  return 1#公約数ブリッジができる可能性あり

from tqdm import tqdm
import time
import sys
K = 100 #捜索最大列数
p = sieve_of_eratosthenes(K)
numArray = []
for k in tqdm(range(29, K)):#k=17で最初の候補発見 #第一引数は3にする。
  num = 0
  for i in range(len(p)):
    if k <= p[i]:
      limit = i
      break
  pmodlist = [0] * limit
  print("列の長さk =:"+str(k))
  print("limit is:"+ str(limit))
  #pmodlist[0] = 1
  while 1:#pmodlist == [0,0,0,0....,0,0]の時、k個の列の左から二番目が必ず0~k*のどの素数にも違いに素となるので調べる必要がない。
    marker = [0]*k
    #k個列の全てに何らかのマーカーがついているか否か確認し、全てについていれば記録する。
    for i in range(limit):
      j = 0
      while j+pmodlist[i] < k:
        marker[j+pmodlist[i]] = 1
        j = j + p[i]
    if sum(marker) == k:
      if canlink(k,p[:limit],pmodlist) == 1:
        print(k)
        print("素数"+str(p[:limit]))
        print("剰余ズレ"+str(pmodlist))
        print("中国剰余定理より上記を満たす連続した自然数が存在する")
        num = num + 1
        #if num >= 10: #最大10個まで見つけることにする。
          #sys.exit()
    pmodlist = prime_digit(0,pmodlist,p,limit)
    #print(pmodlist)
    if sum(pmodlist) == 0:
      numArray.append(num)
      break

    #print("rewhile")
  print(numArray)