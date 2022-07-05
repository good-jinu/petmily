import pandas as pd
import requests
from bs4 import BeautifulSoup


__petfac_df = None # 반려동물 판매업체 데이터프레임

def getdataframe():
    # __petfac_df에 api로 받아온 데이터를 저장하는 함수
    startpg = 1
    endpg = 1000
    rows = []
    for _ in range(18):

        url = f"https://openapi.gg.go.kr/AnimalSale?KEY=d74194f4d92a4448beeca37523698f77&Type=xml&pIndex={startpg}&pSize=1000"
        count = 1
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for i in soup.find_all('row'):
            rows.append({"sigun_cd": i.sigun_cd.string,
                         "sigun_nm": i.sigun_nm.string,
                         "bizplc_nm": i.bizplc_nm.string,
                         "licensg_de": i.licensg_de.string,
                         "bsn_state_nm": i.bsn_state_nm.string,
                         "licensg_cancl_de": i.licensg_cancl_de.string,
                         "clsbiz_de": i.clsbiz_de.string,
                         "bsn_state_div_cd": i.bsn_state_div_cd.string,
                         "sfrmprod_procsbiz_div_nm": i.sfrmprod_procsbiz_div_nm.string,
                         "stockrs_duty_div_nm": i.stockrs_duty_div_nm.string,
                         "locplc_faclt_telno": i.locplc_faclt_telno.string,
                         "locplc_ar_info": i.locplc_ar_info.string,
                         "roadnm_zip_cd": i.roadnm_zip_cd.string,
                         "refine_lotno_addr": i.refine_lotno_addr.string,
                         "refine_roadnm_addr": i.refine_roadnm_addr.string,
                         "refine_zip_cd": i.refine_zip_cd.string,
                         "refine_wgs84_logt": i.refine_wgs84_logt.string,
                         "refine_wgs84_lat": i.refine_wgs84_lat.string,
                         "bizcond_div_nm_info": i.bizcond_div_nm_info.string,
                         "x_crdnt_vl": i.x_crdnt_vl.string,
                         "y_crdnt_vl": i.y_crdnt_vl.string,
                         "stockrs_idntfy_no": i.stockrs_idntfy_no.string,
                         "right_mainbd_idntfy_no": i.right_mainbd_idntfy_no.string
                         })
        startpg += 1
    columns = ["시군코드", "시군명", "사업장명", "인허가일자", "영업상태명", "인허가취소일자", "폐업일자", "영업상태구분코드", "축산물가공업구분명", "축산업무구분명",
               "소재지시설전화번호", "소재지면적정보", "도로명우편번호", "소재지지번주소", "소재지도로명주소", "소재지우편번호", "경도", "위도", "업태구분명정보", "x좌표", "y좌표",
               "축산고유번호", "권리주체일련번호"]
    df = pd.DataFrame(rows, columns=columns)
    __petfac_df = pd.DataFrame(['판매업체', 200, 300])


if __name__=='__main__':
    getdataframe()
    print(__petfac_df.head())
    print(__petfac_df.tail())