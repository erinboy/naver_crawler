import requests
import pandas as pd 

url = "https://new.land.naver.com/api/articles/2515781795?complexNo="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3NDMxNjI4MDksImV4cCI6MTc0MzE3MzYwOX0.hhZFRi_C4RevMkCwtTdsM282z6HfAcPM_08R6lHt8YM",
    "Cookie": "NNB=TRAXOPADO2PWO; ASID=70a1b66b00000194d67ceba200000019; SHOW_FIN_BADGE=Y; _fwb=139ka3May2yI053HWCquH4r.1739705787108; landHomeFlashUseYn=Y; _fwb=139ka3May2yI053HWCquH4r.1739705787108; NAC=eTnSCAhFrwpJB; NACT=1; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=4100000000; SRT30=1743162195; BNB_FINANCE_HOME_TOOLTIP_ESTATE=true; BUC=sq_vxAMafy-dQ9dfPGWwFt6cOP42UspRWhwHtEz6f5U=; nid_inf=2016223040; NID_AUT=gUC0lbsOdOgJuy6N/iy+AcJOGW63xl1Z0DHXDkD4fF5n+731aOlm9lMRYFGmB2Ru; NID_SES=AAABtRJExKEQyIFDw8faDgEiYIow/MgQKEATH/OronL//r4bA5BeKDUYCAyIKiaiepFEtK+IxfsK7rFwHzXncUUf5ALUQPEkO4g9q3RYqOzWSwtkKunFK8IY+wRu9qEDLXpgOREVM3aw+wSBikK7KEd3AekhNYZWydpJmAzyALekOToxFx52c48iY6emO34Porh7lQZXT0ARNSUsYv+wINDptjS8RZtv4+fgiLSTJ1jPJq2zYiABO/bnv9GaHEZvea73GUTNc1CYwUD391q4xNPYJjNJJcUh5SL3FakZVZPWJd7boopia9RZOkbN5pHkVFnbwrO/exjl/OuStI5Gfnwrnf0hr/ZkqTJ9LT0p0CGDlXhCXIeeOo7wAXjL0levX2IcabHFfy96YSsrPAZocHC3BuSaBJ/lEq9/1QcHWqULMb22Be5Fq3CDom0vaby0cvodx3xTUFOafhsUWjKFdolW/AQdYhtKjb+KZrkbuSY9PbOlBSaGSXPYJLj1rfDYcqUN4yrGtIxw1+icIWnr924vfCUQD021/3Glds3AZ/XCcc1O3/JNQxqRyl9jE0Bvn/dTOUd9z+Zb+VDzne2TbvTHsIE=; NID_JKL=48fLJmV9SvirkAa8jAt5/M4B++DnH7Vnr3nCeTdqhcA=; REALESTATE=Fri%20Mar%2028%202025%2020%3A53%3A29%20GMT%2B0900%20(Korean%20Standard%20Time)",
    "Referer": "https://new.land.naver.com/",
}

response = requests.get(url, headers=headers, timeout=5)

if response.status_code == 200:
    data = response.json()

    # 최상위 항목들 중 딕셔너리 타입만 모아서 병합
    flat_dict = {}

    for key, value in data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                new_key = f"{key}_{sub_key}"  # 구분을 위해 접두사 붙이기
                flat_dict[new_key] = sub_value
        else:
            # dict가 아닌 경우도 포함하고 싶으면 여기에 추가
            flat_dict[key] = value

    # 한 줄짜리 DataFrame 생성
    df = pd.DataFrame([flat_dict])

    # 엑셀 저장
    df.to_excel("전체_매물_정보_한줄.xlsx", index=False)
    print("✅ 모든 정보가 엑셀로 저장되었습니다!")
else:
    print("❌ 요청 실패:", response.status_code)
