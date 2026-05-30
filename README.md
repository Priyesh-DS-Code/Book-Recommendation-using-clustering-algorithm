## 🧠 How It Works
1. Data is collected from the **Book-Crossing Dataset**
2. A **pivot table** is created with books as rows and users as columns
3. **KNN algorithm** finds the most similar books based on user ratings
4. **Streamlit** displays the recommendations with book cover images

## 📊 Dataset
- **BX-Books.csv** — Book details (title, author, image URL)
- **BX-Book-Ratings.csv** — User ratings for books
- **BX-Users.csv** — User information

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Priyesh-DS-Code/Book-Recommendation-using-clustering-algorithm.git
cd Book-Recommendation-using-clustering-algorithm
```

### 2. Create virtual environment
```bash
conda create --prefix ./env python=3.11 -y
conda activate ./env
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

## 🛠️ Tech Stack
- **Python**
- **Pandas** — Data manipulation
- **NumPy** — Numerical operations
- **Scikit-learn** — KNN Model
- **Streamlit** — Web application
- **Pickle** — Model serialization

## 📦 Requirements
