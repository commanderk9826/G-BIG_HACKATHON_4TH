import pandas as pd
import numpy as np
from pycaret.regression import *
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler  # 이상치에 둔감한 Scaling 기법

get_ipython().run_line_magic('matplotlib', 'inline')
normalizer = RobustScaler()

train= pd.read_csv('서울시 차량도로 데이터_train_set.csv',encoding='EUC-KR')

data_norm = train.copy() 

train.head() 

train.info()           # 데이터 정보 확인

train.isnull().sum()   #각 Column별 NULL 값 개수 확인  

train_min_val=train['ROAD_LT'].min()

def missing_data(x):
    if x==0:
        x=2          # NULL값 데이터 식별/ 해당 columns의 데이터 속성 고려하여 최소값 2 대입 
    return x

def missing_data_mean(x):
    if x.isnull():
        x=freeze_area['km'].mean()          # NULL값 데이터 식별
                                            # 해당 columns의 데이터 속성 고려하여 최소값 2 대입 
    return x

def missing_data_median(x):
    if x.isnull():
        x=median_val          
    return x


def train_drop(data_norm):
    return data_norm.drop(['NTFC_DE','index','ROAD_BT','ROAD_LT','PK','RN','SIG_CD_PK','RDS_MAN_NO_PK','RN_CD','SOIL_INCLN'],axis=1,inplace=False)


def test_drop(data_norm):
    return data_norm.drop(['NTFC_DE','index','ROAD_BT','ROAD_LT','PK','RN','SIG_CD_PK','RDS_MAN_NO_PK','RN_CD','SOIL_INCLN','dan_lvl'],axis=1,inplace=False)


def log_preprocessing(data_norm,name):
    data_array = normalizer.fit_transform(np.log(data_norm.iloc[:,data_norm.columns==name])) #log함수 적용
    df_data_array=pd.DataFrame(data_array)
    return df_data_array


train['ROAD_LT']=train['ROAD_LT'].apply(missing_data)
train['ROAD_BT']=train['ROAD_BT'].apply(missing_data)

train['ROAD_BT']=log_preprocessing(train,'ROAD_BT')
train['ROAD_LT']=log_preprocessing(train,'ROAD_LT')

train_final=train_drop(train)

train_final


reg = setup(data =train_final, target = 'dan_lvl',categorical_features = ['ROA_CLS_SE','RDS_DPN_SE','DNGR_RD','SOIL_INCL_'])

best_3 = compare_models(sort='MAE')

exp_name = setup(data = train_final, target = 'dan_lvl',numeric_features = ['JSH_NO','SPD_LMT'],categorical_features = ['ROA_CLS_SE','RDS_DPN_SE','DNGR_RD','SOIL_INCL_'])
lightgbm = create_model('lightgbm')
evaluate_model(lightgbm)

lgbm_final = finalize_model(lightgbm)

test = pd.read_csv('서울시 차량도로 데이터_test_set.csv',encoding="EUC-KR")

test['ROAD_LT']=test['ROAD_LT'].apply(missing_data)
test['ROAD_BT']=test['ROAD_BT'].apply(missing_data)
test['ROAD_BT']=log_preprocessing(test,'ROAD_BT')
test['ROAD_LT']=log_preprocessing(test,'ROAD_LT')

test_final=test_drop(test)

prediction= predict_model(lgbm_final,test_final)

test['dan_lvl'] = prediction['Label']

test.head()

test.to_csv('서울시 차량도로 데이터_test_result.csv', encoding="EUC-KR" ,index = False)

a = train_final.drop(['dan_lvl'],axis=1,inplace=False)



plt.figure(figsize = (15, 10))    # 히트맵 사이즈 설정

plt.pcolor(a.corr())

plt.xticks(np.arange(0.5, len(a.columns), 1), a.columns)

plt.yticks(np.arange(0.5, len(a.columns), 1), a.columns)

plt.colorbar()

plt.show()



