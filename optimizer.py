# optimizer.py

from scipy.optimize import linprog

def optimize_risol(profit_mayo, profit_sayur, A, b):
    """
    Melakukan optimasi jumlah produksi risol mayo dan sayur
    untuk memaksimalkan keuntungan, dengan batasan A dan b.

    Parameter:
    - profit_mayo: keuntungan per risol mayo
    - profit_sayur: keuntungan per risol sayur
    - A: matriks kendala, contoh [[2, 1], [1, 2]]
    - b: batasan kendala, contoh [100, 80]

    Return:
    - x_opt: jumlah risol mayo optimal
    - y_opt: jumlah risol sayur optimal
    - total_profit: keuntungan maksimal
    """

    # Fungsi objektif (dinegasikan karena linprog meminimalkan)
    c = [-profit_mayo, -profit_sayur]

    # Batasan variabel (tidak negatif)
    bounds = [(0, None), (0, None)]

    # Solusi optimasi
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    if result.success:
        x_opt = result.x[0]
        y_opt = result.x[1]
        total_profit = -(result.fun)
        return x_opt, y_opt, total_profit
    else:
        return None, None, None
