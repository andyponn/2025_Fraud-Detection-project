## -*- coding: utf-8 -*-







# 1. 讀取 CSV
df_card = pd.read_csv(os.path.join(target_dir, "cards_data.csv"))
df_tran = pd.read_csv(os.path.join(target_dir, "transactions_data.csv"))
df_user = pd.read_csv(os.path.join(target_dir, "users_data.csv"))



# 轉換成兩欄的 DataFrame
df_mcc = pd.DataFrame(list(mcc_data.items()), columns=["mcc_code", "description"])


# train_fraud_labels.json
with open(os.path.join(target_dir, "train_fraud_labels.json"), "r") as f:
    fraud_data = json.load(f)

# fraud_data 如果是 dict，轉換成 DataFrame
if isinstance(fraud_data, dict):
    df_fraud = pd.DataFrame(list(fraud_data.items()), columns=["transaction_id", "is_fraud"])
else:
    df_fraud = pd.DataFrame(fraud_data)

# 確認一下每個資料集大小
print("cards_data.csv:", df_card.shape)
print("transactions_data.csv:", df_tran.shape)
print("users_data.csv:", df_user.shape)
print("mcc_codes.json:", df_mcc.shape)
print("train_fraud_labels.json:", df_fraud.shape)

print(df_card.columns)
print(df_tran.columns)
print(df_user.columns)
print(df_mcc.columns)
print(df_fraud.columns)

cars one heart encoding