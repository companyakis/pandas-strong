import pandas as pd

fake_data = {
    "names": ["Mustafa", "Aygun", "Hakan", "Kutluk"],
    "departments": ["FinTech", "Operations", "Sales", "Finance"],
    "salary_usd": [5600, 4000, 2900, 4500]
}

df = pd.DataFrame(fake_data)

print(df)

"""
     names departments  salary_usd
0  Mustafa     FinTech        5600
1    Aygun  Operations        4000
2    Hakan       Sales        2900
3   Kutluk     Finance        4500

"""
