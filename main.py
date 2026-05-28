import streamlit as st
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

global final_actions_to_take
st.title("Yamaaan Faraz YF BTC and GOLD predictor")
st.text("not 100% but possible it's best because i used KNN and LogReg.")

choose_market = st.selectbox("Choose Market", ["BTC", "GOLD"])
if choose_market == "BTC":
    choose_time = st.selectbox("Choose Time"
        , ["after 1 day"
        , "after 1 hour"
        , "after 1 minute"
        , "after 1 month"
        , "after 1 week"
        , "after 2 hours"
        , "after 3 days"
        , "after 3 minutes"
        , "after 4 hours"
        , "after 5 minutes"
        , "after 6 hours"
        , "after 8 hours"
        , "after 12 hours"
        , "after 15 minutes"
        , "after 30 minutes"], key=1)
    if choose_time == "after 1 day":
        df = pd.read_csv("BTCUSDT_1day.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        # 2. Then display the correctly styled text inside your Streamlit interface
        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 1 hour":
        df = pd.read_csv("BTCUSDT_1hour.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 1 minute":
        df = pd.read_csv("BTCUSDT_1minute.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 1 month":
        df = pd.read_csv("BTCUSDT_1month.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 1 week":
        df = pd.read_csv("BTCUSDT_1week.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 2 hours":
        df = pd.read_csv("BTCUSDT_2hours.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 3 days":
        df = pd.read_csv("BTCUSDT_3days.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 3 minutes":
        df = pd.read_csv("BTCUSDT_3minutes.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 4 hours":
        df = pd.read_csv("BTCUSDT_4hours.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 5 minutes":
        df = pd.read_csv("BTCUSDT_5minutes.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 6 hours":
        df = pd.read_csv("BTCUSDT_6hours.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 8 hours":
        df = pd.read_csv("BTCUSDT_8hours.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 12 hours":
        df = pd.read_csv("BTCUSDT_12hours.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 15 minutes":
        df = pd.read_csv("BTCUSDT_15minutes.csv")
        # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['timestamp', 'close']]
        y = df['Target_Class']

        knn = KNeighborsClassifier(n_neighbors=5)

        LNN = LogisticRegression()

        LNN.fit(x, y)

        Predic = LNN.predict(x)

        knn.fit(x, y)

        tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

        predic = knn.predict(x)

        lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

        if Predic[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")

        if predic[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown(":red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 30 minutes":
            df = pd.read_csv("BTCUSDT_30minutes.csv")
            # 1. Create the target: 1 if the NEXT candle's price is higher than CURRENT price, else 0
            df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

            # 2. Drop the very last row of your dataset
            df = df.dropna()

            x = df[['timestamp', 'close']]
            y = df['Target_Class']

            knn = KNeighborsClassifier(n_neighbors=5)

            LNN = LogisticRegression()

            LNN.fit(x, y)

            Predic = LNN.predict(x)

            knn.fit(x, y)

            tn, fp, fn, tp = confusion_matrix(y, knn.predict(x)).ravel()

            predic = knn.predict(x)

            lnnpredi = "BUY" if Predic[-1] > 0.95 else "SELL"
            knnpredi = "BUY" if predic[-1] > 0.95 else "SELL"

            if Predic[-1] > 0.95:
                st.markdown("The LogReg Model outputted: :green[Buy]")
            else:
                st.markdown(":red[Sell]")

            if predic[-1] > 0.95:
                st.markdown("The KNN Model outputted: :green[Buy]")
            else:
                st.markdown("The KNN Model outputted: :red[Sell]")
            final_actions_to_take = lnnpredi, knnpredi
if choose_market == "GOLD":
    choose_time = st.selectbox("Select Time", ["after 5 min"
        , "after 10 min"
        , "after 15 min"
        , "after 20 min"
        , "after 25 min"
        , "after 30 min"
        , "after 35 min"
        , "after 40 min"
        , "after 45 min"], key=2)
    if choose_time == "after 5 min":
        df = pd.read_csv("gold5.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 10 min":
        df = pd.read_csv("gold10.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 15 min":
        df = pd.read_csv("gold15.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 20 min":
        df = pd.read_csv("gold20.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 25 min":
        df = pd.read_csv("gold25.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 30 min":
        df = pd.read_csv("gold30.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 35 min":
        df = pd.read_csv("gold35.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
    if choose_time == "after 40 min":
        df = pd.read_csv("gold40.csv")
        df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

        # 2. Drop the very last row of your dataset
        df = df.dropna()

        x = df[['Unix', 'close']]
        y = df['Target_Class']

        LNN = LogisticRegression()
        KNN = KNeighborsClassifier(n_neighbors=5)

        LNN.fit(x, y)
        KNN.fit(x, y)

        lnnpred = LNN.predict(x)
        knnpred = KNN.predict(x)

        tn, fp, fn, tp = confusion_matrix(y, knnpred).ravel()

        lnnpredi = "BUY" if lnnpred[-1] > 0.95 else "SELL"
        knnpredi = "BUY" if knnpred[-1] > 0.95 else "SELL"

        if lnnpred[-1] > 0.95:
            st.markdown("The LogReg Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        if knnpred[-1] > 0.95:
            st.markdown("The KNN Model outputted: :green[Buy]")
        else:
            st.markdown("the knn model outputted: :red[Sell]")
        final_actions_to_take = lnnpredi, knnpredi
if choose_time == "after 45 min":
    df = pd.read_csv("gold45.csv")
    df['Target_Class'] = (df['close'].shift(-1) > df['close']).astype(int)

    # 2. Drop the very last row of your dataset
    df = df.dropna()

    # NOTE: Ensure your gold45.csv strictly contains a column named 'Unix' rather than 'timestamp'
    x = df[['Unix', 'close']]
    y = df['Target_Class']

    LNN = LogisticRegression()
    KNN = KNeighborsClassifier(n_neighbors=5)

    LNN.fit(x, y)
    KNN.fit(x, y)

    # FIXED LOGIC: Grab decision classification probabilities matrix arrays to evaluate threshold checks
    lnn_probs = LNN.predict_proba(x)[:, 1]
    knn_probs = KNN.predict_proba(x)[:, 1]

    lnnpredi = "BUY" if lnn_probs[-1] > 0.95 else "SELL"
    knnpredi = "BUY" if knn_probs[-1] > 0.95 else "SELL"

    if lnn_probs[-1] > 0.95:
        st.markdown("The LogReg Model outputted: :green[Buy]")
    else:
        st.markdown("The LogReg Model outputted: :red[Sell]")

    if knn_probs[-1] > 0.95:
        st.markdown("The KNN Model outputted: :green[Buy]")
    else:
        st.markdown("The KNN Model outputted: :red[Sell]")

    # Stored explicitly as a standard string tuple structure
    final_actions_to_take = (lnnpredi, knnpredi)