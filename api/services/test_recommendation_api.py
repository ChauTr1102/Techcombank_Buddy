from api.services import *

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from joblib import load
from pydantic import BaseModel
from typing import List, Dict, Any
import logging
import uvicorn
# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RecommendationModel:
    def __init__(self):
        """Thiết lập kết nối PostgreSQL"""
        try:
            self.conn = psycopg2.connect(
                database="Buddy",
                user="postgres",
                password="Dataflow123!",
                host="buddy.cy1yg6uaeep7.us-east-1.rds.amazonaws.com",
                port="5432"
            )
        except Exception as e:
            logger.error(f"Lỗi kết nối database: {e}")
            return None

    def load_and_predict(self, df):
        """Tải model đã lưu và dự đoán phân khúc"""
        try:
            scaler = load("./model/scaler_Buddy.joblib")
            kmeans = load("./model/kmeans_model_Buddy.joblib")
            scaled_data = scaler.transform(df)
            clusters = kmeans.predict(scaled_data)
            return clusters
        except Exception as e:
            logger.error(f"Lỗi khi tải model: {e}")
            return None

    def load_customer_data(self):
        """Lấy dữ liệu khách hàng"""
        try:
            query = """
            SELECT 
                user_id, age, income_tier, monthly_salary, churn_risk, clv_score,
                mobile_login_freq, tenure_years, household_size, preferred_channel,
                marital_status, occupation, top_mcc, ecom_pos_ratio, overseas_share,
                offer_accepts
            FROM customers
            """
            return pd.read_sql(query, self.conn)
        except Exception as e:
            logger.error(f"Lỗi khi lấy dữ liệu khách hàng: {e}")
            return pd.DataFrame()

    def load_product_data(self):
        """Lấy 8 sản phẩm ngẫu nhiên từ bảng products"""
        try:
            query = """
            SELECT product_id, category, tier, reward_type, reward_value
            FROM products
            ORDER BY RANDOM()
            LIMIT 8
            """
            return pd.read_sql(query, self.conn)
        except Exception as e:
            logger.error(f"Lỗi khi lấy dữ liệu sản phẩm: {e}")
            return pd.DataFrame()

    def preprocess_for_segmentation(self, df):
        """Tiền xử lý dữ liệu cho phân khúc"""
        try:
            income_map = {'Low': 1, 'Lower-Middle': 2, 'Upper-Middle': 3, 'High': 4, 'Affluent': 5}
            channel_map = {'Mobile': 1, 'Web': 2, 'Branch': 3, 'ATM': 4, 'CallCenter': 5}
            marital_map = {'Single': 1, 'Married': 2, 'Divorced': 3, 'Widowed': 4}

            df['income_tier_num'] = df['income_tier'].map(income_map)
            df['channel_num'] = df['preferred_channel'].map(channel_map)
            df['marital_num'] = df['marital_status'].map(marital_map)

            features = [
                'age', 'income_tier_num', 'monthly_salary', 'churn_risk', 'clv_score',
                'mobile_login_freq', 'tenure_years', 'household_size', 'channel_num',
                'marital_num', 'ecom_pos_ratio', 'overseas_share', 'offer_accepts'
            ]
            return df[features].dropna()
        except Exception as e:
            logger.error(f"Lỗi tiền xử lý: {e}")
            return pd.DataFrame()

    def get_customer_segment_from_existing(self, segmented_data, products_data, user_id: str):
        """Lấy thông tin phân khúc và gợi ý sản phẩm"""
        try:
            if user_id not in segmented_data['user_id'].values:
                raise ValueError(f"Không tìm thấy khách hàng với user_id: {user_id}")

            customer_data = segmented_data[segmented_data['user_id'] == user_id].iloc[0]
            segment = customer_data['segment']
            segment_info = segmented_data[segmented_data['segment'] == segment]

            segment_stats = {
                'total_customers': len(segment_info),
                'demographics': {
                    'avg_age': segment_info['age'].mean(),
                    'common_marital_status': segment_info['marital_status'].mode()[0],
                    'common_occupation': segment_info['occupation'].mode()[0],
                    'avg_household_size': segment_info['household_size'].mean()
                },
                'financial': {
                    'avg_salary': segment_info['monthly_salary'].mean(),
                    'common_income_tier': segment_info['income_tier'].mode()[0],
                    'avg_clv': segment_info['clv_score'].mean()
                },
                'behavior': {
                    'avg_mobile_logins': segment_info['mobile_login_freq'].mean(),
                    'common_channel': segment_info['preferred_channel'].mode()[0],
                    'avg_online_ratio': segment_info['ecom_pos_ratio'].mean()
                },
                'risk': {
                    'avg_churn_risk': segment_info['churn_risk'].mean()
                }
            }

            return {
                'user_id': user_id,
                'segment': int(segment),
                'customer_info': {
                    'age': customer_data['age'],
                    'marital_status': customer_data['marital_status'],
                    'occupation': customer_data['occupation'],
                    'household_size': customer_data['household_size'],
                    'monthly_salary': customer_data['monthly_salary'],
                    'income_tier': customer_data['income_tier']
                },
                'segment_stats': segment_stats,
                'product_recommendations': [
                    {
                        'product_id': product['product_id'],
                        'category': product['category'],
                        'tier': product['tier'],
                        'reward_type': product['reward_type'],
                        'reward_value': product['reward_value']
                    } for _, product in products_data.iterrows()
                ]
            }

        except Exception as e:
            logger.error(f"Lỗi khi lấy thông tin phân khúc: {e}")
            raise


