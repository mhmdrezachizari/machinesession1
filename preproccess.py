import pandas as pd
def count_missing(df, check_nan=True, check_empty=True, check_none=True, check_whitespace=True, ignore_case=True):
    """
    بررسی مقادیر مفقود یا مشکل‌دار در دیتافریم
    پارامترها:
        Author:MohamamdrezaChizari
        df: pandas DataFrame
        check_nan: بررسی NaN
        check_empty: بررسی رشته خالی ''
        check_none: بررسی None
        check_whitespace: بررسی رشته‌های فقط فاصله '   '
        ignore_case: برای رشته‌ها حروف را نادیده بگیرد
    خروجی:
        result: DataFrame شامل تعداد هر نوع در هر ستون
        total_missing: مجموع کل مقادیر مفقود
    """
    
    def count_cell_missing(col):
        count = 0
        # تبدیل به str برای بررسی رشته‌ها
        col_str = col.astype(str) if ignore_case else col
        
        if check_nan:
            count += col.isna().sum()
        if check_none:
            count += col.isnull().sum()
        if check_empty:
            count += (col_str == '').sum()
        if check_whitespace:
            count += col_str.str.strip().eq('').sum()
        return count

    total_missing_per_col = df.apply(count_cell_missing)
    
    result = pd.DataFrame({
        'Total_missing': total_missing_per_col
    })
    
    total_missing = total_missing_per_col.sum()
    
    return result, total_missing