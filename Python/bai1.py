def tach_chuoi(s):
    chuoi_chu = ""
    chuoi_so = ""
    for ky_tu in s:
        if ky_tu.isalpha(): 
            chuoi_chu += ky_tu
        elif ky_tu.isdigit(): 
            chuoi_so += ky_tu
    if not chuoi_chu:
        chuoi_chu = "-"
    if not chuoi_so:
        chuoi_so = "-"
    return chuoi_chu, chuoi_so
def xu_ly_file():
    try:
        with open('chuoi.inp', 'r', encoding='utf-8') as file_in:
            s = file_in.read().strip()
        chuoi_chu, chuoi_so = tach_chuoi(s)        
        with open('chuoi.out', 'w', encoding='utf-8') as file_out:
            file_out.write(chuoi_chu + '\n')
            file_out.write(chuoi_so + '\n')
        print("Tách chuỗi thành công!")
        print(f"Chuỗi gốc: '{s}'")
        print(f"Chuỗi chữ: '{chuoi_chu}'")
        print(f"Chuỗi số: '{chuoi_so}'")
    except FileNotFoundError:
        print("Không tìm thấy file 'chuoi.inp'")
    except Exception as e:
        print(f"Lỗi: {e}")
xu_ly_file()