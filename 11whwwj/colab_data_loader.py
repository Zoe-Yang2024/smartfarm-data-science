# 과제13 / 2023년 10월 주민등록 인구 데이터 자동 불러오기
import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/Zoe-Yang2024/smartfarm-data-science/main/11whwwj/"

sig_url = BASE_URL + "population_202310_jeonbuk_sig.csv"
emd_url = BASE_URL + "population_202310_korea_emd.csv"

df_pop = pd.read_csv(sig_url, encoding="utf-8", dtype={"행정구역": str})
df_emd = pd.read_csv(emd_url, encoding="utf-8", dtype={"행정구역": str})

for frame in (df_pop, df_emd):
    frame.columns = frame.columns.str.strip()

print("전북 시군구 자료:", df_pop.shape)
print("전국 읍면동 자료:", df_emd.shape)
assert df_pop.shape == (17, 70)
assert df_emd.shape == (3878, 70)

# 집계 코드 확인 (2023년 전국 시도 17개)
df_emd["행정코드"] = df_emd["행정구역"].str.extract(r"\((\d{10})\)", expand=False)
provinces = df_emd[df_emd["행정코드"].str.fullmatch(r"\d{2}0{8}", na=False)].copy()
assert len(provinces) == 17, "2023년 전국 시도 집계 17건을 확인하세요."

# 2023년 전라북도 행정코드는 45로 시작합니다.
print("전라북도 읍면동 및 시군구 행정코드는 45...로 시작합니다.")
