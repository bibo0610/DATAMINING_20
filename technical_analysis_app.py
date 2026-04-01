### 1. Nhập thư viện
import yfinance as yf
import streamlit as st
import datetime
import pandas
import cufflinks as cf
from plotly.offline import iplot

cf.go_offline()

### 2. Định nghĩa một hàm để tải xuống danh sách các cổ phiếu thành phần của chỉ số S&P 500 từ Wikipedia
@st.cache
def get_sp500_components():
    df = pd.read_html("httpd://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = df[0]
    tickers = df["Symbol"].tolist()
    tickers_companies_dict = dict(zip(df["Symbol"], df["Security"]))
    return tickers, tickers_companies_dict

### 3. Định nghĩa một hàm để tải xuống giá cổ phiếu trong quá khứ bằng cách sử dụng yfinance:
@st.cache
def load_data(symbol, start, end):
    return yf.download(symbol, start=start, end=end)

### 4. định nghĩa một hàm để lưu trữ dữ liệu đã tải xuống dưới dạng tệp CSV:
@st.cache
def convert_to_csv(df):
    return df.to_csv().encode("utf-8")

### 5. Định nghĩa phần của thanh bên được sử dụng để chọn mã cổ phiếu và ngày tháng:
st.sidebar.header("Stock Parameters")

available_tickers, tickers_companies_dict = get_sp500_components()
ticker = st.sidebar.selectbox(
    "Ticker",
    available_tickers,
    format_func=tickers_companies_dict.get
)
start_date = st.sidebar.date_input(
    "Start Date",
    datetime.date(2019, 1, 1)
)
end_date = st.sidebar.date_input(
    "End Date",
    datetime.date.today()
)

if start_date > end_date:
    st.sidebar.error("Error: End date must be after start date.")

### 6. Xác định phần của thanh bên được sử dụng để tinh chỉnh các chi tiết của phân tích kỹ thuật:
st.sidebar.header("Technical Analysis Parameters")

volume_flag = st.sidebar.checkbox(label="Add Volume")

### 7. Thêm bộ mở rộng với các thông số của SMA:
exp_sma = st.sidebar.expander("Simple Moving Average (SMA) Parameters")
sma_flag = exp_sma.checkbox(label="Add SMA")
sma_period = exp_sma.slider(
    "SMA Period",
    min_value=1,
    max_value=50,
    value=20,
    step=1
)

### 8. Thêm bộ mở rộng với các thông số của dải Bollinger:
exp_bb = st.sidebar.expander("Bollinger Bands")
bb_flag = exp_bb.checkbox(label="Add Bollinger Bands")
bb_period = exp_bb.slider(
    "Bollinger Bands Period",
    min_value=1,
    max_value=50,
    value=20,
    step=1
)
bb_std = exp_bb.number_input(label="# of standard deviations",
                             min_value=1,
                             max_value=4,
                             value=2.0,
                             step=1)

### 9. Thêm phần mở rộng với các tham số của RSI:
exp_rsi = st.sidebar.expander("Relative Strength Index (RSI)")
rsi_flag = exp_rsi.checkbox(label="Add RSI")
rsi_period = exp_rsi.number_input(
    "RSI Periods",
    min_value=1,
    max_value=50,
    value=20,
    step=1
)
rsi_upper = exp_rsi.number_input(
    "RSI Upper",
    min_value=50,
    max_value=90,
    value=70,
    step=1
)
rsi_lower = exp_rsi.number_input(label = "RSI Lower",
                                min_value=10,
                                max_value=50,
                                value=30,
                                step=1)

### 10. Chỉ định tiêu đề và văn bản bổ sung trong phần thân chính của ứng dụng:
st.title("Technical Analysis App")
st.write("""
         ### User munual
         * you can select a company from the S&P 500 constituents
         """)

### 11. Tải dữ liệu giá cổ phiếu trong quá khứ:
df = load_data(ticker, start_date, end_date)

### 12. Thêm phần mở rộng với bản xem trước dữ liệu đã tải xuống:
data_exp = st.expander("Preview data")
available_cols = df.columns.tolist()
cols_to_show = data_exp.multiselect(
    "Columns",
    available_cols,
    default=available_cols
)
data_exp.dataframe(df[cols_to_show])

csv_file = convert_to_csv(df[cols_to_show])
data_exp.download_button(
    label="Download selected data as CSV",
    data=csv_file,
    file_name=f"{ticker}_stock_prices.csv",
    mime="text/csv"
)

### 13. Tạo biểu đồ nến với các chỉ báo TA đã chọn:
title_str = f"{tickers_companies_dict[ticker]}'s Stock Price"
qf = cf.QuantFig(df, title=title_str)
if volume_flag:
    qf.add_volume()
if sma_flag:
    qf.add_sma(periods=sma_period)
if bb_flag:
    qf.add_bollinger_bands(period=bb_period, boll_std=bb_std)
if rsi_flag:
    qf.add_rsi(periods=rsi_period, upper=rsi_upper, lower=rsi_lower,showbands=True)

fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

# lệnh chạy file: streamlit run technical_analysis_app.py