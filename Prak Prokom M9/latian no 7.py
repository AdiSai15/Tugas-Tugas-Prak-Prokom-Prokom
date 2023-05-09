def vokal(teks):
    vokal_list = ['a','i','u','e','o']
    teks = list(teks.lower())
    for i in vokal_list:
        print(f"Huruf {i} ada : ",teks.count(i))
vokal("fakultas teknik, teknik geodesi")