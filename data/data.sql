CREATE TABLE customers (
    user_id TEXT PRIMARY KEY,
    age INTEGER,
    occupation TEXT,
    income_tier TEXT,
    marital_status TEXT,
    household_size INTEGER,
    preferred_language TEXT,
    products TEXT,
    tenure_years INTEGER,
    avg_balance FLOAT,
    cc_limit_util TEXT,
    mortgage_outstanding FLOAT,
    investments_aum FLOAT,
    monthly_salary FLOAT,
    top_mcc TEXT,
    ecom_pos_ratio FLOAT,
    overseas_share FLOAT,
    avg_bill_pay_amt FLOAT,
    cash_wd_freq INTEGER,
    mobile_login_freq INTEGER,
    days_since_push INTEGER,
    preferred_channel TEXT,
    offer_ctr FLOAT,
    offer_accepts INTEGER,
    offer_fatigue FLOAT,
    declined_offer_cat TEXT,
    day_time TEXT,
    season_flag TEXT,
    geo_region TEXT,
    weather TEXT,
    rt_spending_trigger BOOLEAN,
    clv_score FLOAT,
    churn_risk FLOAT,
    propensity_scores TEXT,
    price_sensitivity FLOAT,
    peer_cluster_vec TEXT,
    usage_journey TEXT
);

CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    category TEXT,
    tier TEXT,
    apr FLOAT,
    reward_type TEXT,
    reward_value FLOAT,
    eligibility TEXT,
    tenor_months INTEGER,
    risk_adj_margin FLOAT,
    hist_conv_rate FLOAT,
    hist_profit FLOAT,
    budget_remaining FLOAT,
    max_redemptions INTEGER,
    offer_dates TEXT,
    launch_recency_days INTEGER,
    compliance_tag TEXT,
    channels TEXT,
    target_segments TEXT,
    geo_applic TEXT,
    merchant_industry TEXT,
    cost_to_bank FLOAT,
    expected_utility FLOAT,
    cross_sell_score FLOAT,
    bundle_depth INTEGER,
    valid_window TEXT,
    popularity_trend TEXT
);

CREATE TABLE adoption_logs (
    adopted BOOLEAN,
    tenure_days INTEGER,
    recency_days INTEGER,
    activity_intensity INTEGER,
    monetary_volume FLOAT,
    utilisation_ratio FLOAT,
    reward_redemption_rate FLOAT,
    risk_flag BOOLEAN,
    PRIMARY KEY (user_id, product_id),
	user_id TEXT REFERENCES customers(user_id),
    product_id TEXT REFERENCES products(product_id)
);

CREATE TABLE transaction_history(
	transaction_id text primary key,
	sender_card_id text,
	sender_name text,
	sender_bank text default 'TechcomBank',
	receiver_card_id text,
	receiver_name text,
	receiver_bank text default 'TechcomBank',
	note text,
	amount money,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_001', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Thanh toán hóa đơn điện', 1350000, '2025-03-05 10:15:23.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_002', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Chi phí học tập con', 2800000, '2025-03-08 14:30:10.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_003', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Chuyển tiền sinh hoạt', 1900000, '2025-03-12 09:00:55.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_004', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Mua sắm vật tư', 750000, '2025-03-15 16:45:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_005', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền lương tháng 3', 4500000, '2025-03-18 11:20:30.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_006', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Đóng tiền internet', 400000, '2025-03-22 13:00:12.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_007', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua quà sinh nhật', 600000, '2025-03-25 10:40:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_008', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Trả nợ cá nhân', 3200000, '2025-03-28 17:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_009', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Hỗ trợ dự án', 1100000, '2025-04-02 08:30:15.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_010', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Tiền ăn uống', 950000, '2025-04-05 12:10:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_011', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Đóng góp từ thiện', 300000, '2025-04-08 14:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_012', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Tiền gas tháng 4', 280000, '2025-04-10 09:45:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_013', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Sách giáo trình', 500000, '2025-04-14 11:30:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_014', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Thanh toán dịch vụ', 1800000, '2025-04-17 15:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_015', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua sắm đồ dùng', 850000, '2025-04-20 10:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_016', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Hoàn ứng công tác', 2500000, '2025-04-23 16:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_017', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Tiền thưởng hiệu suất', 3000000, '2025-04-26 10:30:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_018', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Phí dịch vụ hàng tháng', 150000, '2025-04-29 11:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_019', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Mua thực phẩm', 700000, '2025-05-03 14:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_020', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Đóng tiền nhà', 4000000, '2025-05-06 09:30:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_021', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Quà tặng bạn bè', 200000, '2025-05-09 10:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_022', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Sửa chữa máy móc', 1200000, '2025-05-12 15:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_023', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền lương tháng 4', 4700000, '2025-05-15 11:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_024', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua mỹ phẩm', 450000, '2025-05-18 13:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_025', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Đầu tư chứng khoán', 5000000, '2025-05-21 16:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_026', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Thanh toán dịch vụ IT', 900000, '2025-05-24 10:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_027', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Học phí ngoại ngữ', 1600000, '2025-05-27 11:30:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_028', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Mua quần áo', 650000, '2025-05-30 14:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_029', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Đồ dùng học tập', 250000, '2025-03-01 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_030', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Phí bảo trì', 180000, '2025-03-04 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_031', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Chi phí di chuyển', 350000, '2025-03-07 14:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_032', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Hỗ trợ gia đình', 2200000, '2025-03-10 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_033', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua sách', 100000, '2025-03-13 16:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_034', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Phí tư vấn', 2000000, '2025-03-16 10:30:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_035', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Đóng góp quỹ', 500000, '2025-03-19 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_036', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Tiền học thêm', 700000, '2025-03-22 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_037', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Thanh toán điện thoại', 150000, '2025-03-25 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_038', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Mua đồ dùng cá nhân', 300000, '2025-03-28 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_039', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Chuyển khoản online', 1500000, '2025-03-31 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_040', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Tiền sửa xe', 400000, '2025-04-03 12:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_041', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền thuê nhà', 3500000, '2025-04-06 08:30:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_042', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua sắm cho bé', 800000, '2025-04-09 14:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_043', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Hoàn trả tiền vay', 1000000, '2025-04-12 16:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_044', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Chi phí quảng cáo', 1700000, '2025-04-15 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_045', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Đóng quỹ lớp', 200000, '2025-04-18 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_046', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Tiền học phí', 1100000, '2025-04-21 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_047', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Thanh toán bảo hiểm', 600000, '2025-04-24 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_048', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Mua đồ dùng gia đình', 900000, '2025-04-27 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_049', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Chi phí vật liệu', 1000000, '2025-04-30 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_050', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền sinh hoạt chung', 1900000, '2025-05-03 08:30:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_051', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua đồ chơi trẻ em', 250000, '2025-05-06 14:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_052', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Đóng tiền điện nước', 450000, '2025-05-09 16:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_053', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Chi phí quảng cáo', 1300000, '2025-05-12 10:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_054', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Tiền khám bệnh', 550000, '2025-05-15 11:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_055', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Mua sắm hàng tháng', 850000, '2025-05-18 13:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_056', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Tiền học phí', 2900000, '2025-05-21 09:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_057', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Hỗ trợ khẩn cấp', 1000000, '2025-05-24 15:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_058', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Phí bảo hiểm xe', 300000, '2025-05-27 10:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_059', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền điện nước', 600000, '2025-05-30 08:30:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_060', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua đồ dùng cá nhân', 400000, '2025-03-02 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_061', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Chi phí dự án', 2100000, '2025-03-05 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_062', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Đóng tiền thuê văn phòng', 4800000, '2025-03-08 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_063', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Tiền học năng khiếu', 800000, '2025-03-11 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_064', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Mua sắm đồ điện tử', 1400000, '2025-03-14 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_065', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Tiền thuốc men', 150000, '2025-03-17 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_066', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Chi phí sửa chữa', 700000, '2025-03-20 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_067', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Hỗ trợ kinh doanh', 2500000, '2025-03-23 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_068', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Đóng quỹ công ty', 300000, '2025-03-26 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_069', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua sắm quần áo', 950000, '2025-03-29 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_070', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Hoàn tiền khách hàng', 1800000, '2025-04-01 12:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_071', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Phí tư vấn pháp lý', 4000000, '2025-04-04 08:30:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_072', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Tiền mừng tuổi', 500000, '2025-04-07 14:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_073', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Đóng tiền nước', 120000, '2025-04-10 16:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_074', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Sửa máy tính', 750000, '2025-04-13 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_075', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Chi phí du lịch', 2300000, '2025-04-16 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_076', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Mua đồ dùng văn phòng', 400000, '2025-04-19 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_077', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền lương tháng 5', 4600000, '2025-04-22 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_078', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Đóng tiền học thêm', 650000, '2025-04-25 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_079', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Chi phí sự kiện', 1600000, '2025-04-28 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_080', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Hỗ trợ phần mềm', 900000, '2025-05-01 12:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_081', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Tiền mừng đám cưới', 1000000, '2025-05-04 08:30:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_082', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Đóng tiền điện', 380000, '2025-05-07 14:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_083', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Mua đồ dùng học tập', 200000, '2025-05-10 16:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_084', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Chi phí ăn uống', 1100000, '2025-05-13 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_085', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Thanh toán hóa đơn', 700000, '2025-05-16 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_086', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Tiền thuê văn phòng', 3000000, '2025-05-19 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_087', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Mua sắm gia dụng', 1200000, '2025-05-22 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_088', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Đầu tư kinh doanh', 4500000, '2025-05-25 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_089', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Hỗ trợ kỹ thuật', 600000, '2025-05-28 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_090', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Đóng phí dịch vụ', 250000, '2025-05-31 12:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_091', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Chi tiêu cá nhân', 500000, '2025-03-03 14:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_092', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRANVA-003', 'Trần Văn An', N'Mua đồ dùng bếp', 800000, '2025-03-06 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_093', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-LETHN-004', 'Lê Thị Hà', N'Tiền quà tặng', 300000, '2025-03-09 16:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_094', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-PHAMVK-005', 'Phạm Văn Khánh', N'Hỗ trợ tiền nhà', 1500000, '2025-03-12 10:30:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_095', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-NGUYENVT-006', 'Nguyễn Thị Tuyết', N'Chi phí sinh hoạt', 2000000, '2025-03-15 11:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_096', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DOANTH-007', 'Đoàn Thị Hương', N'Đóng tiền nước', 180000, '2025-03-18 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_097', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-VOVANP-008', 'Võ Văn Phát', N'Mua sắm đồ dùng cá nhân', 600000, '2025-03-21 09:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_098', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-TRUONGVK-009', 'Trương Văn Khoa', N'Hỗ trợ kinh phí', 900000, '2025-03-24 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_099', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-MAINGA-010', 'Mai Ngọc Anh', N'Tiền ăn sáng', 100000, '2025-03-27 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_100', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', 'TCB-DUONGTM-002', 'Dương Thị Mai', N'Mua đồ dùng gia đình', 1200000, '2025-03-30 12:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_101', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán công nợ', 2500000, '2025-03-01 09:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_102', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền vay mượn', 1500000, '2025-03-03 11:30:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_103', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hoàn tiền cọc', 800000, '2025-03-06 14:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_104', 'TCB-NGUYENVT-014', 'Nguyễn Văn Tiến', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Mua hàng online', 350000, '2025-03-09 10:10:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_105', 'TCB-DUONGVD-015', 'Dương Việt Đức', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Đóng góp quỹ', 500000, '2025-03-12 16:20:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_106', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Trả tiền đồ ăn', 120000, '2025-03-15 08:45:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_107', 'TCB-LETHN-016', 'Lê Thị Ngọc', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền mừng sinh nhật', 600000, '2025-03-18 13:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_108', 'TCB-HOANGNT-017', 'Hoàng Nhật Tuấn', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền học phí', 1800000, '2025-03-21 15:30:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_109', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hoàn tiền mua sách', 250000, '2025-03-24 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_110', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Chuyển tiền mua chung', 900000, '2025-03-27 12:40:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_111', 'TCB-DOANTT-018', 'Đoàn Thanh Thảo', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền đặt cọc', 1000000, '2025-03-30 09:20:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_112', 'TCB-NGUYENVT-014', 'Nguyễn Văn Tiến', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Trả tiền sửa chữa', 400000, '2025-04-02 14:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_113', 'TCB-DUONGVD-015', 'Dương Việt Đức', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Chi phí chung', 700000, '2025-04-05 11:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_114', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán phí dịch vụ', 200000, '2025-04-08 17:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_115', 'TCB-LETHN-016', 'Lê Thị Ngọc', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền vay', 3000000, '2025-04-11 09:30:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_116', 'TCB-HOANGNT-017', 'Hoàng Nhật Tuấn', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hỗ trợ kinh doanh', 4500000, '2025-04-14 14:15:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_117', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hoàn tiền đã ứng', 1000000, '2025-04-17 10:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_118', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Chuyển tiền đầu tư', 5000000, '2025-04-20 11:50:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_119', 'TCB-DOANTT-018', 'Đoàn Thanh Thảo', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền học', 1600000, '2025-04-23 15:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_120', 'TCB-NGUYENVT-014', 'Nguyễn Văn Tiến', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán hóa đơn', 850000, '2025-04-26 13:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_121', 'TCB-DUONGVD-015', 'Dương Việt Đức', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền hỗ trợ', 200000, '2025-04-29 09:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_122', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Trả tiền mua sách', 100000, '2025-05-02 10:30:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_123', 'TCB-LETHN-016', 'Lê Thị Ngọc', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền ăn uống', 400000, '2025-05-05 14:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_124', 'TCB-HOANGNT-017', 'Hoàng Nhật Tuấn', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán hợp đồng', 2800000, '2025-05-08 16:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_125', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền sửa xe', 300000, '2025-05-11 11:20:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_126', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hỗ trợ chi phí', 1200000, '2025-05-14 09:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_127', 'TCB-DOANTT-018', 'Đoàn Thanh Thảo', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền mua đồ', 650000, '2025-05-17 13:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_128', 'TCB-NGUYENVT-014', 'Nguyễn Văn Tiến', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền thưởng', 1900000, '2025-05-20 15:45:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_129', 'TCB-DUONGVD-015', 'Dương Việt Đức', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán điện thoại', 150000, '2025-05-23 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_130', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Trả tiền ăn trưa', 100000, '2025-05-26 12:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_131', 'TCB-LETHN-016', 'Lê Thị Ngọc', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền sinh hoạt', 700000, '2025-05-29 08:30:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_132', 'TCB-HOANGNT-017', 'Hoàng Nhật Tuấn', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Phí tư vấn', 2200000, '2025-03-04 11:00:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_133', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hỗ trợ dự án', 1800000, '2025-03-07 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_134', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán khóa học', 950000, '2025-03-10 10:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_135', 'TCB-NGUYENVT-014', 'Nguyễn Văn Tiến', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền hàng', 400000, '2025-03-13 14:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_136', 'TCB-DUONGVD-015', 'Dương Việt Đức', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Phí bảo trì', 250000, '2025-03-16 16:30:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_137', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hoàn tiền mua đồ', 300000, '2025-03-19 09:10:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_138', 'TCB-LETHN-016', 'Lê Thị Ngọc', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền ăn uống', 150000, '2025-03-22 13:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_139', 'TCB-HOANGNT-017', 'Hoàng Nhật Tuấn', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán dịch vụ', 1100000, '2025-03-25 15:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_140', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Mua đồ dùng', 600000, '2025-03-28 10:40:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_141', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Chi phí chung cư', 3500000, '2025-03-31 11:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_142', 'TCB-DOANTT-018', 'Đoàn Thanh Thảo', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền học thêm', 750000, '2025-04-03 14:20:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_143', 'TCB-NGUYENVT-014', 'Nguyễn Văn Tiến', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán nợ', 2000000, '2025-04-06 09:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_144', 'TCB-DUONGVD-015', 'Dương Việt Đức', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Mua sắm gia đình', 1000000, '2025-04-09 16:00:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_145', 'TCB-VUANH-011', 'Vũ Thị Anh', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền đặt hàng', 500000, '2025-04-12 10:00:00.567890+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_146', 'TCB-LETHN-016', 'Lê Thị Ngọc', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Hoàn ứng', 1500000, '2025-04-15 13:00:00.123456+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_147', 'TCB-HOANGNT-017', 'Hoàng Nhật Tuấn', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Chi phí quảng cáo', 2500000, '2025-04-18 09:30:00.789012+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_148', 'TCB-TRANDT-012', 'Trần Đình Tú', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Thanh toán đồ điện tử', 800000, '2025-04-21 15:00:00.345678+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_149', 'TCB-PHAMTL-013', 'Phạm Thị Lan', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền góp vốn', 4000000, '2025-04-24 10:15:00.901234+07');
INSERT INTO transaction_history (transaction_id, sender_card_id, sender_name, receiver_card_id, receiver_name, note, amount, created_at) VALUES ('tx_150', 'TCB-DOANTT-018', 'Đoàn Thanh Thảo', 'TCB-HOANGNN-001', 'Nguyễn Ngọc Hoàng', N'Tiền sinh hoạt chung', 1300000, '2025-04-27 12:00:00.567890+07');
